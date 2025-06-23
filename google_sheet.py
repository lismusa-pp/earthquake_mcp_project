import gspread
from google.oauth2.service_account import Credentials
from config import CREDENTIALS_FILE, GOOGLE_SHEET_NAME

SCOPES = [    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"]

def connect_to_sheet():
    creds = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=SCOPES)
    client = gspread.authorize(creds)
    sheet = client.open(GOOGLE_SHEET_NAME).sheet1
    return sheet

def write_earthquakes_to_sheet(data_rows):
    sheet = connect_to_sheet()
    sheet.clear()  # Optional: Clear previous data

    headers = ["Time (UTC)", "Location", "Magnitude", "Depth (km)", "More Info"]
    sheet.append_row(headers)

    for row in data_rows:
        sheet.append_row(row)
