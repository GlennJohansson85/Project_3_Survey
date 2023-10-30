import gspread
from google.oauth2.service_account import Credentials
import pandas as pd
from collections import Counter

SCOPE = [
  "https://www.googleapis.com/auth/spreadsheets",
  "https://www.googleapis.com/auth/drive.file",
  "https://www.googleapis.com/auth/drive",
]

CREDS_PATH = "creds.json"

def authorize_gspread():
    """
    Authorize the Google Sheets API using credentials.
    Returns:
        Authorized gspread client or None on error. 
    """
    try:
        creds = Credentials.from_service_account_file(CREDS_PATH, scopes=SCOPE)
        return gspread.authorize(creds)
    except Exception as e:
        print("Error authorizing gspread:", e)
        return None
    
def open_google_sheet(client, sheet_title):
    """
    Open a Google Sheet by title.
    Args:
        client: Authorizede gspread client.
        sheet_title: Title of the Google Sheet.
    Returns:
        gspread Sheet or None if the sheet is not found.
    """
    try:
        return client.open(sheet_title)
    except gspread.exceptions.SpreadsheetNotFound:
        print(f"Spreadsheet '{sheet_title}' not found.")
        return None