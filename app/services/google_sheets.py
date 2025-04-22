from googleapiclient.discovery import build

# defining shets abstraction through class
class GoogleSheetsService:
    
    def __init__(self, credential_data):
        self.sheets_service = build("sheets", "v4", credentials=credential_data).spreadsheets()
        self.drive_service = build("drive", "v3", credentials=credential_data)