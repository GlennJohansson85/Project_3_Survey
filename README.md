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
#### Participant Data Collection
The script collects the following information from participants:
* Name: The participant´s name (validated for non-empty and non-numeric characters).
* Age: The participant´s age (validated to be between 14 and 85 years).
* Gender: The participant´s gender (validated to be 'male' or 'female') in a case-insensitive manner.
* Occupation: The participant´s occupation (validated for non-empty and non-numeric characters) and stored in uppercase format.
* Income: The participant´s yearly income (validated for 5 or 6-digit numeric values).
* Location: The participant´s work location is validated against a list of valid locations("uscities.xlsx") in a case-insensitive manner. The validated location is stored in a
  uppercase format for consistency.
* ![image](https://github.com/GlennJohansson85/p3-survey/assets/139962883/a360022b-aff0-415e-8d1f-bb0db6c4bb07)

#### Participant Input Validation
* Participant inputs are validated to ensure data integrity and correctness. Invalid inputs prompt the participant to re-enter the information.
* Inputs are case-insensitive, allowing the participant to write in both upper- or lowercase.


#### Participant Input Confirmation
* After all questions has been answered, participants are presented with a summary of their inputs and asked if they are satisfied with their input.
  ![image](https://github.com/GlennJohansson85/p3-survey/assets/139962883/e5027dcc-94f3-4279-81d3-c31ba5bb5833)
* If yes = The script updates the dedicated Google Sheet ("survey") in real-time.
  ![image](https://github.com/GlennJohansson85/p3-survey/assets/139962883/c27b3b65-be8c-4cb2-a745-fb8afa22c5ee)

* If no = The script resets, without adding any data to the Google Sheet, making the input more accurate incase of typos.
  ![image](https://github.com/GlennJohansson85/p3-survey/assets/139962883/ef7acf22-b62b-4582-8479-48eaee0dee72)
 
  
#### Data Analysis Made Easy
With a simple menu option, the analyst can instantly access insightful data analysis, including gender distribution, average age, income statistics, most common occupations, and highest-paid occupations for both males and females.

#### User-Friendly Interaction
The intuitive user menu provides a hassle-free experience, allowing you to add new participants, dive into data analysis, or exit the program—all at your fingertips.

#### Error Handling
The script includes robust error handling to address exceptions that may occur during Google Sheets integration or data manipulation, ensuring a smooth and reliable user experience.
After entering their data, participants are presented with a summary of their inputs and asked to confirm. This confirmation step helps avoid mistakes and ensures accurate data entry.

### Credits

#### Code Institute:
* Comparative Programming Languages
* Python Essentials
* Love Sandwiches - Essentials Project
* Slack Forum
#### My Mentor
* Brian Macharia
#### Websites/Cloud Services/Forums
* Google Cloud/Drive/Spreadsheet
* Stack overflow
* https://www.talent.com/salary ("uscites.xlsx")
* https://www.fiverr.com
* https://www.programiz.com
* https://www.reddit.com
* https://www.geeksforgeeks.org
* https://learnpython.org
* https://www.udemy.com
