from googleapiclient.discovery import build
from datetime import datetime as dt
import gspread
import json


class GSheet:
    """Class to interact with Google Sheet"""

    def __init__(self, spreadsheetName) -> None:
        self.__sa = gspread.service_account()
        self.__ss = self.__sa.open(spreadsheetName)

    @property
    def sa(self):
        return self.__sa

    @property
    def ss(self):
        return self.__ss


class GSheetStateSXT(GSheet):
    """Class to interact with Google Sheet corresponds to the SPREADSHEET_NAME"""

    scenarioResult = {}

    def __init__(
        self,
        spreadsheetName,
        folderId,
        testedFilesOnly=True,
    ) -> None:
        super().__init__(spreadsheetName)
        self.curDate = dt.now().strftime("%Y/%m/%d %H:%M:%S")
        self.automationName = "Selenium"
        self.newSpreadsheetName = f"Automation - Release {self.curDate}"
        self.__folderId = folderId
        self.__newSs = None
        self.testedFilesOnly = testedFilesOnly
        self.json_path = "track.json"

    def create_a_copy_of_worksheet_into_new_gsheet_file_and_update_the_values(self, worksheetName, namedRange, values):
        try:  # assuming that the gsheet has already a worksheet with paramater name
            wks = self.__newSs.worksheet(worksheetName)
        except:  # assuming that the gsheet does not have any worksheet the same with the parameter
            oldWks = self.ss.worksheet(worksheetName)
            wks = self.__newSs.worksheet(oldWks.copy_to(self.__newSs.id)["title"])
            wks.update_title(worksheetName)
        wks.update(namedRange, values, value_input_option="USER_ENTERED")

    def create_a_copy_of_gsheet_file(self):
        self.sa.copy(file_id=self.ss.id, title=self.newSpreadsheetName, copy_permissions=True)
        self.__newSs = self.sa.open(self.newSpreadsheetName)
        if self.testedFilesOnly:
            deleteRequests = []
            initialSheets = ["Cover", "Use Cases", "ToC", "Queries", "variables"]
            for wks in self.__newSs.worksheets():
                if wks.title not in initialSheets:
                    deleteRequests.append({"deleteSheet": {"sheetId": wks.id}})
            self.__newSs.batch_update({"requests": deleteRequests})

    def get_values_by_named_range(self, worksheetName, namedRange):
        wks = self.ss.worksheet(worksheetName)
        return wks.get(namedRange)

    def upload_the_gsheet_file_to_folder(self):
        # Move the newly created spreadsheet to the desired folder
        drive_service = build("drive", "v3", credentials=self.sa.auth)
        drive_service.files().update(fileId=self.__newSs.id, addParents=self.__folderId, fields="id,parents").execute()

    def save_data_to_json(self):
        # Write data to the JSON file
        try:
            with open(self.json_path, "w") as json_file:
                json.dump(self.scenarioResult, json_file, indent=4)  # Use indent for pretty formatting
        except Exception as e:
            print(f"An error happened when trying to save the result data to {self.json_path}: \n{e}")

    def get_json(self):
        # Read data from the JSON file
        with open(self.json_path, "r") as json_file:
            return json.load(json_file)

    def update_all_values(self, useJSON=False):
        if useJSON:  # to get the result data from self.json_path
            data = self.get_json()
        else:  # to get the result data from the test execution, and will try to save the data to self.json_path
            data = self.scenarioResult

        if data:
            # create a new file (the duplicate of the target file)
            self.create_a_copy_of_gsheet_file()

            for worksheetName in data:
                for namedRange in data[worksheetName]:
                    values = [
                        [
                            self.curDate,
                            self.automationName,
                            internalCheckResult,
                            externalCheckResult,
                            testerNote,
                        ]
                        for internalCheckResult, externalCheckResult, testerNote in data[worksheetName][namedRange]
                    ]
                    self.create_a_copy_of_worksheet_into_new_gsheet_file_and_update_the_values(worksheetName, namedRange.replace("Data", "Form"), values)
            # remove sheet1, which is the default sheet that is created when creating a new gsheet file
            if self.__newSs.sheet1.title == "Sheet1":
                self.__newSs.del_worksheet(self.__newSs.sheet1)
            self.upload_the_gsheet_file_to_folder()
        else:
            print("No test result when updating all values in Google Sheet")

    def update_worksheet_colors(self, useJSON=False):
        if useJSON:
            data = self.get_json()
        else:
            data = self.scenarioResult

        if data:
            for wksName in data:
                wksId = self.__newSs.worksheet(wksName).id
                noFail = True
                for nr in data[wksName]:
                    if len(list(filter(lambda x: x[0] == "FAILED", data[wksName][nr]))):
                        noFail = False
                        break

                if noFail:
                    requestsBatch = [
                        {
                            "updateSheetProperties": {
                                "properties": {
                                    "sheetId": wksId,
                                    "tabColor": {
                                        "red": 0.0,  # Specify the color values in RGB format (from 0.0 to 1.0)
                                        "green": 1.0,
                                        "blue": 0.0,
                                    },
                                },
                                "fields": "tabColor",
                            }
                        }
                    ]
                else:
                    requestsBatch = [
                        {
                            "updateSheetProperties": {
                                "properties": {
                                    "sheetId": wksId,
                                    "tabColor": {
                                        "red": 1.0,  # Specify the color values in RGB format (from 0.0 to 1.0)
                                        "green": 0.0,
                                        "blue": 0.0,
                                    },
                                },
                                "fields": "tabColor",
                            }
                        }
                    ]

                # Send the batchUpdate request
                self.__newSs.batch_update({"requests": requestsBatch})
        else:
            print("No test result when updating worksheet colors in Google Sheet")
