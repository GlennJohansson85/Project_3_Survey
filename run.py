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
    
    # Variabls to track the highest paid occupation and income for males and females.
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
                except ValueError:
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
    average_age_females = int(total_age_females / valid_age_count_females) if valid_age_count_females > 0 else 0
    
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
        "MOST COMMON OCCUPATION FOR MALES": most_common_occupation_males,
        "MOST COMMON OCCUPATION FOR FEMALES": most_common_occupation_females,
        "HIGHEST PAID OCCUPATION FOR MALES": f"{highest_paid_occupation_males} ({highest_paid_location_male})",
        "HIGHEST PAID OCCUPATION FOR FEMALES": f"{highest_paid_occupation_females} ({highest_paid_location_female})",    
    }
    
    return summary
    
def display_insights(summary):
    """
    Display summary statistics in a user-friendly format.
    Args:
        summary: Dictionary with summary statistics.
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
            formatted_value = f"${value:,.0f}"
        else:
            formatted_value = f"${value.upper() if isinstance(value, str) else value}"
        print(f"{formatted_key} : {formatted_value}")
        
    print("--------------------------------------")
    
def get_valid_NAME():   
    """
    Get a valid name input from user.
    Returns:
        Valid user name.
    """
    while True:
        name = input("Your name: ")
        # Convert name to uppercase ensuring consistency and make comparisons case-insensitive.
        if len(name) >= 2 and not any(char.isdigit() for char in name):
            return name.upper()
        else:
            print("Please use only letter and ensure the name is at lease 2 characters long.")
    
def get_valid_AGE():
    """
    Get a valid age input from user.
    Returns:
        Valid user age.
    """
    while True:
        age = input("Your age (between 14 and 85): ")
        if age.isdigit() and 14 <= int(age) <= 85:
            return int(age)
        else:
            print("Please enter a valid age between 14 and 85.")
            
def get_valid_GENDER():
    """
    Get a valid gender input from user.
    Returns:
        Valid user gender.
    """
    while True:
        gender = input("Your gender (male/female): ").strip().lower()
        if gender in ["male", "female"]:
            return gender
        else:
            print("Pleaser enter either 'male' or 'female'.")
            
def get_valid_OCCUPATION():
    """
    Get a valid occupation input from user.
    Returns:
        Valid user occupation.
    """
    while True:
        occupation = input("Your occupation: ")
        if len(occupation) >= 2 and not any(char.isdigit() for char in occupation):
            return occupation.upper()
        else:
            print("Please use only letters and ensure the name of the occupation is at least 2 characters long.")
            
def get_valid_INCOME():
    """
    Get a valid income input from user.
    Returns:
        Valid user income.
    """
    while True:
        income = input("Your yearly income (5 or 6 digits): ")
        if income.isdigit() and (len(income) == 5 or len(income) ==6):
            return int(income)
        else:
            print("Please enter a valid income with 5 or 6 digits.")
            
def get_valid_LOCATION(valid_locations):
    """
    Get a valid location input from user.
    Args:
        valid_locations: List of valid locations from "uscities.xlsx".
    Retruns:
        Valid user location: 
    (Ensures case-insensitive matching for locations by converting user input and valid locations to uppercase.)
    """
    while True: 
        location = input("In which city do you work: ").strip().upper()
        if location in valid_locations:
            return location
        else:
            print("Where in the US is your work located? In which city?")
            
def get_user_info(valid_locations):
    """
    Get user information from user.
    Args:
        valid_locations: List of valid locations.
    Returns:
        A summary containing user information. 
    """
    user_info = {
        "NAME": get_valid_NAME(),
        "AGE": get_valid_AGE(),
        "GENDER": get_valid_GENDER(),
        "OCCUPATION": get_valid_OCCUPATION(),
        "INCOME": get_valid_INCOME(),
        "LOCATION": get_valid_LOCATION(valid_locations),
    }
    
    return user_info
    
def show_summary_and_confirm(user_info):
    """
    Display user information, confirm = update "survey"(Google Sheet)
    Args:
        user_info: Summary containing user input. 
    Returns: 
        True if user confirms, False outherwise.
    """
    max_key_length = max(len(key) for key in user_info.keys())
    max_value_length = max(len(str(value)) for value in user_info.values())
    
    # Display user input summary
    print("-" * (max_key_length + max_value_length + 20))
    print("-------- SUMMARY --------")
    
    for key, value in user_info.items():
        if key == "GENDER":
            formatted_key = key.upper()
            formatted_value = value.upper()
        elif key == "INCOME":
            formatted_key = key.upper()
            # Format income as currency
            formatted_value = f"${value:,.0f}"
        else:
            formatted_key = key.upper()
            formatted_value = value
            
        print(f"{formatted_key.ljust(max_key_length).upper()} : {formatted_value}")
        
    print("-" * (max_key_length + max_value_length + 20))
    
    while True:
        confirmation = input("Are you satisfied with your answers? (yes/no): ").strip().lower()
        if confirmation == "yes":
            try:
                client = authorize_gspread()
                sheet_title = "survey"
                sheet = open_google_sheet(client, sheet_title)
                worksheet = sheet.get_worksheet(0)
                
                user_values = list(user_info.values())
                worksheet.insert_row(user_values, 2)
                
                print(f"User input added to the survey '{sheet_title}'.")
            except gspread.exceptions.WorksheetNotFound as e:
                print("Worksheet not found:", e)
            except Exception as e:
                print("An error occurred while updating Google sheet", e)
            break
        elif confirmation == "no":
            print("Let´s start over.")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
    
def implement_data():
    valid_locations = load_valid_location()
    user_data = []
    """
    Main function to interact with users and updateGoogle Sheet. 
    """
    while True:
        choice = input("Press 1 = New Participant, Press 2 = Analyst, Press 3 = Exit:").strip()
        if choice == "1":
            user_info = get_user_info(valid_locations)
            if show_summary_and_confirm(user_info):
                user_data.append(user_info)
        elif choice == "2":
            client = authorize_gspread()
            if client:
                sheet_title = "survey"
                try:
                    sheet = open_google_sheet(client, sheet_title)
                    worksheet = sheet.get_worksheet(0)
                except gspread.exceptions.WorksheetNotFound as e:
                    print("Worksheet not found:", e)
                    continue
                    
                records = worksheet.get_all_records()
                if records:
                    summary = calculate_summary(records)
                    display_insights(summary)
                else:
                    print("No data in Google Sheet yet.")
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid input. Please enter 1, 2 or 3.")
    
    if user_data:
        try:
            client = authorize_gspread()
            sheet_title = "survey"
            sheet = open_google_sheet(client, sheet_title)
            worksheet = sheet.get_worksheet(0)
            
            for i, user in enumerate(user_data, start=2):
                user_values = list(user.values())
                worksheeet.insert_row(user_values, i)
                
            print(f"Survey data added to Google Sheet '{sheet_title}'.")
        except gspread.exceptions.WorksheetNotFound as e:
            print("Worksheet not found:", e)
        except Exception as e:
            print("An error occured while updating Google Sheet:", e)
            
if __name__=="__main__":
    implement_data()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    