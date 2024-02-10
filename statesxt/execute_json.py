from utils.gsheet import GSheetStateSXT
from dotenv import load_dotenv
import os


def run():
    gsheet_bbui = GSheetStateSXT(
        spreadsheetName=os.getenv("SPREADSHEET_NAME"),
        folderId=os.getenv("FOLDER_ID"),
        executeJSON=True,
        testedFilesOnly=False,
        usedDomain="MSYS",
    )
    print("updating gsheet with json...")
    gsheet_bbui.update_all_values(useJSON=True)
    gsheet_bbui.update_worksheet_colors(useJSON=True)
    print("updating complete!")


if __name__ == "__main__":
    """
    Basically this file is purposed to execute the track.json file (located on root), which contains the test result of the last test execution. This action is taken regarding to avoid 2 main problems, i.e. request limit and unexpected error during the gsheet upgrade process.
    """

    load_dotenv()
    run()
