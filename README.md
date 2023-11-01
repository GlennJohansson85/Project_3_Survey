# p3-survey

"This Python project serves a specific analytical purpose. It is built to systematically gather user-provided information and employ this data to conduct a comparative study of annual income between male and female individuals. The focus of this analysis narrows down to individuals sharing the same occupation and residing within the United States.

Key Focus:
1. Gender-Based Comparison: The heart of this project is a yearly income comparison between males and females. By collecting and analyzing user data, the script shows if there really are any differences. 

2. Quantitative Insights: Dive deep into the data with key quantitative metrics, such as the number of male and female participants, the average age for both groups, and the average income they earn.

3. Occupation Insights: Discover the most common occupations among males and females based on location. 

4. Earnings at the Peak: Explore the highest-paid occupations for both males and females, coupled with their respective locations. This data paints a vivid picture of earning potential across genders.

Unveil a world of insights as you embark on a gender-based exploration of user data. Whether you're conducting sociological research, labor market analysis, or simply curious about the disparities and similarities between males and females, this script provides the analytical tools you need.

Get started today and gain a fresh perspective of gender-based data analysis. 

## Features
### Participant Data Collection
The script collects the following information from participants:
* Name: The participant´s name (validated for non-empty and non-numeric characters).
* Age: The participant´s age (validated to be between 14 and 85 years).
* Gender: The participant´s gender (validated to be 'male' or 'female') in a case-insensitive manner.
* Occupation: The participant´s occupation (validated for non-empty and non-numeric characters) and stored in uppercase format.
* Income: The participant´s yearly income (validated for 5 or 6-digit numeric values).
* Location: The participant´s work location is validated against a list of valid locations("uscities.xlsx") in a case-insensitive manner. The validated location is stored in a
  uppercase format for consistency.

### Participant Input Validation
* Participant inputs are validated to ensure data integrity and correctness. Invalid inputs prompt the participant to re-enter the information.
* Inputs are case-insensitive, allowing the participant to write in both upper- or lowercase aswell as using spaces or not when entering location (New York/newyork).

### Participant Input Confirmation
* After entering their data, participants are presented with a summary of their inputs and asked to confirm, restart or exit the program. This way we avoid mistakes and ensures
  accurate data entry.

### Google Sheet Integration
* The script automates data storage by updating a dedicated Google Sheet named "survey" in real-time. The collected data is organized for further analysis and reference.

### Data Analysis Made Easy
With a simple menu option, the analyst can instantly access insightful data analysis, including gender distribution, average age, income statistics, most common occupations, and highest-paid occupations for both males and females.

### User-Friendly Interaction
The intuitive user menu provides a hassle-free experience, allowing you to add new participants, dive into data analysis, or exit the program—all at your fingertips.

#### Error Handling
The script includes robust error handling to address exceptions that may occur during Google Sheets integration or data manipulation, ensuring a smooth and reliable user experience.
After entering their data, participants are presented with a summary of their inputs and asked to confirm. This confirmation step helps avoid mistakes and ensures accurate data entry.

## Prerequisites
Before using the script, the following is needed:

1. Google Sheets API Credentials: Create a `creds.json` file with the necessary credentials for the Google Sheets API. Make sure it has the required permissions to access and modify the target Google Sheet.

2. Python Environment: Make sure you have Python installed on your system.

3. Required Libraries: Install the necessary Python libraries using `pip install gspread pandas`.

4. Valid Locations Data: Ensure that you have an XLSX file named `uscities.xlsx` containing a list of valid locations (cities in the USA) for location validation.

## Usage

1. Run the script by executing `python your_script_name.py`.

2. You will be presented with the following options:
   - Enter '1' to add a new participant.
   - Enter '2' to perform data analysis.
   - Enter '3' to exit the program.

3. If you choose to add a new participant, you will be prompted to enter your name, age, gender, occupation, income, and location. The script will validate your inputs and ask for confirmation.

4. If you choose to perform data analysis, the script will provide insights into the collected data, including gender distribution, average age, average income, most common occupation, and highest-paid occupation for both males and females.

5. The script will update a Google Sheet named "survey" with the collected user data.

6. You can exit the program at any time by choosing option '3'.

### Credits
 
