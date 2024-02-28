import pytest
import os

from utils.email import EmailScheduler
from utils.gsheet import GSheetStateSXT
from utils.logger import Logger


@pytest.fixture(scope="session")
def logger():
    lg = Logger()
    yield
    lg.shutdown()


@pytest.fixture(scope="session")
@pytest.mark.usefixtures("use_gsheet")
@pytest.mark.usefixtures("tfo")
def gsheet(request, use_gsheet, tfo):
    usedMarkers = request.config.getoption("-m").split(" and ")
    if "scheduler" in usedMarkers:
        yield None
        return
    gsheet_statesxt = GSheetStateSXT(
        spreadsheetName=os.getenv("SPREADSHEET_NAME"),
        folderId=os.getenv("FOLDER_ID"),
        testedFilesOnly=False if (tfo == "0") else True,
    )
    yield gsheet_statesxt
    gsheet_statesxt.save_data_to_json()
    if use_gsheet == "1":
        print("Updating gsheet...")
        gsheet_statesxt.update_all_values()
        gsheet_statesxt.update_worksheet_colors()


@pytest.fixture(scope="session")
@pytest.mark.usefixtures("use_email")
def email(use_email):
    # create an email instance
    email = EmailScheduler(
        sender_email=os.getenv("SENDER_EMAIL"),
        sender_password=os.getenv("SENDER_PASSWORD"),
        receiver_email=os.getenv("RECEIVER_EMAIL").split(","),
        receiver_name=os.getenv("RECEIVER_NAME").split(","),
    )
    yield email
    print(f"\n\nResults:\n{email.testResult}\n")
    if use_email == "1":
        # send email
        try:
            print("Sending email...")
            email.send()
            print("Email has been sent successfully.")
        except Exception as e:
            print(f"Email failed to send: {str(e)}")
