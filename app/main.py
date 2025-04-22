from fastapi import FastAPI, Depends
from app.dependencies.sheets import get_google_sheet_service
from app.services.google_sheets import GoogleSheetsService

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "hey three!"}

@app.get("/test")
def read_root(service: GoogleSheetsService = Depends(get_google_sheet_service)):
    return {"message": repr(service.sheets_service)}
