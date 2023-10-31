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
    
    # Total income and count for males and females.
    total_income_males = 0
    valid_income_count_males = 0
    total_income_females = 0
    valid_income_count_females = 0
    
    # Iterate through user data to aggregate statistics.
    for user in user_data:
        gender = user.get("GENDER", "").strip().lower()
        income_str = user.get("INCOME")
        location = user.get("LOCATION", "").strip().upper()
        
        if gender == "male":
            num_males += 1
            age_str = user.get("AGE")
            occupation = user.get("OCCUPATION", "").strip()
            
            if age_str:
                try:
                    age = int(age_str)
                    total_age_males += age
                    valid_age_count_males += 1
                except ValueErrir:
                    pass
                
                if occupation:
                    occupation_males.append(occupation)
                    
                if income_str:
                    try:
                        income = int(income_str)
                        total_income_males += income
                        valid_income_count_males += 1
                        if income > highest_paid_income_males:
                            highest_paid_income_males = income
                            highest_paid_occupation_males = occupation
                            highest_paid_location_male = location
                    except ValueError:
                        pass
            elif gender == "female":
                num_females += 1
                age_str = user.get("AGE")
                occupation = user.get("OCCUPATION", "").strip()

                if age_str:
                    try:
                        age = int(age_str)
                        total_age_females += age
                        valid_age_count_females += 1
                    except ValueError:
                        pass
                    
                if occupation:
                    occupation_females.append(occupation)
                    
                if income_str:
                    try:
                        income = int(income_str)
                        total_income_females += income
                        valid_income_count_females += 1
                        if income > highest_paid_income_females:
                            highest_paid_income_females = income
                            highest_paid_occupation_females = occupation
                            highest_paid_location_female = location
                    except ValueError:
                        pass
                    
    # Calculate average age for males and females
    average_age_males = int(total_age_males / valid_age_count_males) if valid_age_count_males > 0 else 0
    average_age_females = int(total_age_females / valid_age_count_males) if valid_age_count_females > 0 else 0
    
    # Calculate average income for males and females
    average_income_males = int(total_income_males / valid_income_count_males) if valid_income_count_males > 0 else 0
    average_income_females = int(total_income_females / valid_income_count_females) if valid_income_count_females > 0 else 0
    
    # Determine the most common occupations for males and females
    most_common_occupation_males = (
        Counter(occupation_males).most_common(1)[0][0].upper() if occupation_males else ""        
    )
    most_common_occupation_females = (
        Counter(occupation_females).most_common(1)[0][0].upper() if occupation_females else ""
    )
    
    # Create a summary dictionary with statistics
    summary = {
        "NUMBER OF MALES": num_males,
        "NUMBER OF FEMALES": num_females,
        "AVERAGE AGE FOR MALES": average_age_males,
        "AVERAGE AGE FOR FEMALES": average_age_females,
        "AVERAGE INCOME FOR MALES": average_income_males,
        "AVERAGE INCOME FOR FEMALES": average_income_females,
        "MOST COMMON OCCUPATION FOR MALES": most_common_occupation_males
        "MOST COMMON OCCUPATION FOR FEMALES": most_common_occupation_females,
        "HIGHEST PAID OCCUPATION FOR MALES": f"{highest_paid_occupation_males} ({highest_paid_location_males})",
        "HIGHEST PAID OCCUPATION FOR FEMALES": f"{highest_paid_occupation_females} ({highest_paid_location_females})",    
    }
    
    return summary
    
def display_insights(summary):
    """
    Display summary statistics in a user-friendly format.
    Args:
        summary: Dictionary with summary statistics
    """
    max_key_length = max(len(key) for key in summary.keys())
    max_value_length = max(len(str(value)) for value in summary.values())
    # Create a line of the same width
    line = '-' * (max_key_length + max_value_length + 20)
    
    print("-------------- INSIGHTS --------------")
    for key, value in summary.items():
        formatted_key = f"{key.ljust(max_key_length)}"
        if key.startswith("AVERAGE INCOME"):
            # Remove ".00" and add "$" and ","
            formatted_value = f"{values:,.0f}"
        else:
            formatted_value = f"{value.upper() if isinstance(value, str) else value}"
        print(f"{formatted_key} : {formatted_value}")
        
    print("--------------------------------------")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    