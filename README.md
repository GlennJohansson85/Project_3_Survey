# p3-survey

This Python project is built to systematically gather user-provided information and employ the data to conduct a comparative study of annual income between male and female individuals. The focus of this analysis narrows down to individuals sharing the same occupation and residing within the United States.
The participants partaking in the survey are fictional.

Key Focus:
1. Gender-Based Income Comparison: At the core of this project lies a analysis of yearly income disparities between males and females. Through the collection and examination of user data, the script presents the differences between males and females income within the same occupation or locatation.  

2. Quantitative Insights: Dive deep into the data with key quantitative metrics, such as the number of male and female participants, the average age for both groups, and the average income they earn.

3. Occupation Insights: Discover the most common occupations among males and females based on location. 

4. Earnings at the Peak: Explore the highest-paid occupations for both males and females, coupled with their respective locations. This data paints a vivid picture of earning potential across genders.

## Features
#### Participant Data Collection
The script collects the following information from participants:
* Name: The participant´s name (validated for non-empty and non-numeric characters).
* Age: The participant´s age (validated to be between 14 and 85 years).
* Gender: The participant´s gender (validated to be 'male' or 'female') in a case-insensitive manner.
* Occupation: The participant´s occupation (validated for non-empty and non-numeric characters) and stored in uppercase format.
* Income: The participant´s yearly income (validated for 5 or 6-digit numeric values).
* Location: The participant´s work location is validated against a list of valid locations("uscities.xlsx") in a case-insensitive manner. The validated location is stored in a
  uppercase format for consistency.<br>
  ![image](https://github.com/GlennJohansson85/p3-survey/assets/139962883/a360022b-aff0-415e-8d1f-bb0db6c4bb07)

#### Participant Input Validation
* Participant inputs are validated to ensure data integrity and correctness. Invalid inputs prompt the participant to re-enter the information.
* Inputs are case-insensitive, allowing the participant to write in both upper- or lowercase.

#### Participant Input Confirmation
* After participants have completed all the questions, they are presented with a summary of their inputs. 
  ![image](https://github.com/GlennJohansson85/p3-survey/assets/139962883/e5027dcc-94f3-4279-81d3-c31ba5bb5833)
* If yes = The script updates the dedicated Google Sheet ("survey") in real-time.
  ![image](https://github.com/GlennJohansson85/p3-survey/assets/139962883/c27b3b65-be8c-4cb2-a745-fb8afa22c5ee)
  ![image](https://github.com/GlennJohansson85/p3-survey/assets/139962883/ff333301-9ccd-4396-be54-8400b19f38ec)

* If no = The script resets, without adding any data to the Google Sheet, making the input more accurate incase of typos.
  ![image](https://github.com/GlennJohansson85/p3-survey/assets/139962883/ef7acf22-b62b-4582-8479-48eaee0dee72)
 
  
#### Data Analysis Made Easy
* With a simple menu option, the analyst can instantly access insightful data analysis, including gender distribution, average age, income statistics,
  most common occupations, andhighest-paid occupations for both males and females.
  ![image](https://github.com/GlennJohansson85/p3-survey/assets/139962883/20bfe092-70da-4e76-bd9b-c68462555747)

### Testing
* CI Python Linter
  ![image](https://github.com/GlennJohansson85/p3-survey/assets/139962883/f13e9cbc-6a30-4fcf-802e-b7bd057a09a4)



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
