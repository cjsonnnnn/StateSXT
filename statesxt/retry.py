from utils.gsheet import GSheetStateSXT
from dotenv import load_dotenv
import os


def run():
    gsheet_statesxt = GSheetStateSXT(
        spreadsheetName=os.getenv("SPREADSHEET_NAME"),
        folderId=os.getenv("FOLDER_ID"),
        testedFilesOnly=True,
    )
    print("updating gsheet with json...")
    gsheet_statesxt.update_all_values(useJSON=True)
    gsheet_statesxt.update_worksheet_colors(useJSON=True)
    print("updating complete!")


if __name__ == "__main__":
    """
    Basically this file is purposed to execute the track.json file (located on root), which contains the test result of the last test execution. This action is taken regarding to avoid 2 main problems, i.e. request limit and unexpected error during the gsheet upgrade process.
    """

    load_dotenv()
    run()
