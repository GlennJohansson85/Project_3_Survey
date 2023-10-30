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

def load_valid_location():
    """
    Load valid locations from an XLSX file.
    Returns:
        List of valid Locations (Cities in USA).
    """
    valid_locations = []
    try:
        df = pd.read_excel("uscities.xlsx")
        valid_locations = df["location"].str.upper().tolist()
    except Exception as e:
        print(f"Error loading valid locations from XLSX file: {e}")
    return valid_locations

def calculate_summary(user_data):
    """
    Calculate summary statistics from user data.
    Args:
        user_data: List of user data dictionaries.
    Returns:
        A dictionary with summary statistics.
    """
    # Initialize variables for data aggregation.
    num_males = 0
    num_females = 0
    
    # Total age and count for males and females.
    total_age_males = 0
    valid_age_count_males = 0
    total_age_females = 0
    valid_age_count_females = 0
    
    # Lists to store occupations for males and females.
    occupation_males = []
    occupation_females = []
    
    # Variabls to track the highest paid occupatiion and income for males and females.
    highest_paid_occupation_males = ""
    highest_paid_income_males = 0
    highest_paid_occupation_females = ""
    highest_paid_income_females = 0
    highest_paid_location_male = ""
    highest_paid_location_female = ""
    
    # Total income and count for males and females
    total_income_males = 0
    valid_income_count_males = 0
    total_income_females = 0
    valid_income_count_females = 0
    
    # Iterate through user data to aggregate statistics
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    