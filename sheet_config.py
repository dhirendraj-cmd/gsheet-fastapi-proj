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

# sheets_service.values().append(
#     spreadsheetId = sheet_id,
#     range = "Sheet1!A1",
#     valueInputOption = "RAW",
#     body = {
#         "values": [
#             ["testing", "test"],
#             ["some"]
#         ]
#     }
# ).execute()


# creating new sheets programatically
response = sheets_service.create(body={
    "properties": {
        "title": "Sheet1"
    }
}).execute()

new_sheet_id  = response['spreadsheetId']
print(new_sheet_id)

sheet_url = response['spreadsheetUrl']
print(sheet_url)

# inserting new value in sheet

sheets_service.values().append(
    spreadsheetId = new_sheet_id,
    range = "Sheet1!A1",
    valueInputOption = "RAW",
    body = {
        "values": [
            ["something new", "test"],
            ["soyes boss me"]
        ]
    }
).execute()


# get values i.e. select in sql
res = sheets_service.values().get(
    spreadsheetId = new_sheet_id,
    range = "Sheet1!A1:Z100",
).execute()

print(res)


# manage permissions through google drive api
drive_service = build("drive", "v3", credentials=creds_data)
print(drive_service)

drive_service.permissions().create(
    fileId=new_sheet_id,
    body={
        "role": "writer",
        "type": "user",
        "emailAddress": os.environ.get("emailAddress"),
    },
    fields="id"
).execute()


