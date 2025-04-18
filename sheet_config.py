import os
from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path=dotenv_path)

creds_data = Credentials.from_service_account_file(
    "credentials.json",
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ]
)

# print(creds_data)

sheets_service = build("sheets", "v4", credentials=creds_data).spreadsheets()
# print(sheets_service)

sheet_id = os.environ.get("sheet_id")
# print(sheet_id)


# inserting new value in sheet

sheets_service.values().append(
    spreadsheetId = sheet_id,
    range = "Sheet1!A1",
    valueInputOption = "RAW",
    body = {
        "values": [
            ["testing", "test"],
            ["some"]
        ]
    }
).execute()



