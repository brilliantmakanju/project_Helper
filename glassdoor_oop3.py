import os
import time
import json
import random
import string
from openai import OpenAI
from functools import wraps
from bs4 import BeautifulSoup
from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException

# Define User Information
user_info = {
    "age_verification": "Yes",  # Or "No"
    "work_authorization": "Yes",  # Or "No"
    "referral_source": "Glassdoor",
    "current_employment_status": "No",  # Or "Yes"
    "relationship_with_employees": "No",  # Or "Yes, Name: Relationship"
    "education": "Yes",  # Or "No"
    "years_of_experience": {
        "business_systems_application": 5,
        "project_lead_or_supervisory": 2
    },
    "certifications": "Yes",  # Or "No"
    "telecommuting_availability": "Yes",  # Or "No"
    "salary_requirements": "Yes",  # Or "No"
    "personal_data": {
        "race_ethnicity": "Asian",
        "gender": "Male",
        "veteran_status": "I AM NOT A PROTECTED VETERAN",
        "disability_status": "No, I do not have a disability and have not had one in the past"
    },
    "contact_information": {
        "phone": "123-456-7890",
        "linkedin": "linkedin.com/in/username"
    },
    "reasons_for_interest": "I am attracted to the company's innovative projects.",
    "location": {
        "americas": "Yes",  # Or "No"
        "visa_sponsorship_required": "No"  # Or "Yes"
    }
}

user_info_dev = {
    "name": "Brilliant Makanju",
    "phone": "09015573136",
    "email": "brilliantmakanju5@gmail.com",
    "role": "Full Stack Developer",
    "address": "123 Main Street, Lagos, Nigeria",
    "linkedin": "https://www.linkedin.com/in/brilliant-makanju",
    "github": "https://github.com/brilliantmakanju",
    "skills": [
        "JavaScript",
        "Python",
        "React",
        "Node.js",
        "Django",
        "HTML",
        "CSS"
    ],
    "experience": [
        {
            "company": "Tech Innovators Ltd",
            "position": "Senior Full Stack Developer",
            "duration": "Jan 2020 - Present",
            "responsibilities": [
                "Lead a team of developers to build and maintain web applications",
                "Implemented new features and optimized existing ones",
                "Collaborated with cross-functional teams to define and design new features"
            ]
        },
        {
            "company": "Code Masters Inc",
            "position": "Full Stack Developer",
            "duration": "Jan 2018 - Dec 2019",
            "responsibilities": [
                "Developed and maintained web applications using JavaScript and Python",
                "Worked with designers to create user-friendly interfaces",
                "Optimized applications for maximum speed and scalability"
            ]
        }
    ],
    "education": [
        {
            "institution": "University of Lagos",
            "degree": "Bachelor of Science in Computer Science",
            "graduation_year": 2017
        }
    ],
    "certifications": [
        {
            "name": "Certified JavaScript Developer",
            "issuing_organization": "JavaScript Institute",
            "issue_date": "Mar 2018"
        },
        {
            "name": "Full Stack Web Development Certification",
            "issuing_organization": "FreeCodeCamp",
            "issue_date": "Nov 2017"
        }
    ],
    "languages": ["English", "Yoruba"],
    "preferred_pronouns": "He/Him",
    "linkedin_profile": "https://www.linkedin.com/in/brilliant-makanju",
    "salary_expectations": "100,000 USD per year",
    "remote_experience_years": 3,
    "adapt_to_california_hours": "Yes",
    "authorized_to_work_in_usa": "No",
    "coding_assessment_consent": "Yes",
    "frontend_experience_years": 5,
    "react_skill_rating": 9,
    "javascript_skill_rating": 9
}


# class="Button_applyButton__pYKk1 Button_greenTheme__EXYIV"
# class="button_Button__MlD2g button-base_Button__knLaX"

# ia-continueButton ia-Question-continue css-sbr3v1 e8ju0x50
# ia-continueButton ia-Question-continue css-sbr3v1 e8ju0x50
# ia-continueButton ia-Question-continue css-sbr3v1 e8ju0x50

# ia-BasePage-component ia-BasePage-component--withContinue
# ia-BasePage-component ia-BasePage-component--withContinue
# ia-BasePage ia-Questions ia-PageAnimation-enter-done
# ia-BasePage ia-Questions ia-PageAnimation-enter-done
# ia-BasePage ia-Questions ia-PageAnimation-enter-done
#
api_keyDetail=''

class JobApplicationAutomation:
    def __init__(self, driver):
        self.driver = driver

    def check_current_section(self):
        print("Checking the current section...")
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "ia-BasePage-component"))
            )
            container_divs = self.driver.find_elements(By.XPATH, "//div[contains(@class, 'ia-BasePage-component--withContinue')]")
            if container_divs:
                print("In the questions section.")
                return True
            else:
                print("In the preview section.")
                return False
        except Exception as e:
            print(f"An error occurred while checking the current section: {e}")
            return None
    
    def click_preview_section(self):
        print("Clicking on the preview section link...")
        preview_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "ia-PreviewSection-link"))
        )
        preview_link.click()

    def click_label(self):
        print("Clicking on the label...")
        label_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "css-mza3f0"))
        )
        label_element.click()

    def click_textarea(self):
        print("Clicking on the textarea...")
        textarea_element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "css-besaou"))
        )
        textarea_element.click()
        return textarea_element
    
    def write_cv(self, cv_text):
        print("Writing CV into the textarea...")
        textarea_element = self.click_textarea()
        textarea_element.clear()
        textarea_element.send_keys(cv_text)
        print("CV written into the textarea.")

    def fill_cv(self, cv_text):
        try:
            self.click_preview_section()
            self.click_label()
            self.write_cv(cv_text)
            print("Waiting for user to review the CV...")
            time.sleep(30)  # Adjust the wait time as needed
        except Exception as e:
            print(f"An error occurred: {e}")


class FormFiller:
    def __init__(self, driver):
        self.driver = driver
        self.user_info = user_info_dev
        # Set up OpenAI API
        self.openai_client = OpenAI(api_key=api_keyDetail)



    def generate_response(self, question, job_description):
        user_info_json = json.dumps(user_info_dev, indent=4)
        prompt = f"""
        You are a highly intelligent assistant helping a candidate to fill out a job application form. Below are examples of questions and their specific answers based on the candidate's information:

        {user_info_json}

            Questions:
            1. How many years of Front-end development experience do you have? (required)
            2. How many years of remote working experience do you have? (optional)
            3. Are you able to adapt to overlap your work day with California hours (i.e., until 4:00 p.m. Pacific Time)? (required)
            4. Are you legally authorized to work in the USA without requiring employer sponsorship now or in the future? (required)
            5. There will be a 60 min coding assessment as one of the steps in our recruitment process. Do you consent to receiving this assessment? (required)
            6. How many years of experience do you have with frontend development languages like JavaScript and/or React? (required)
            7. On a scale of 1-10 (10 being the best) how would you rate your skills with React? (required)
            8. On a scale of 1-10 (10 being the best) how would you rate your skills with JavaScript? (required)
            9. Do you have experience working with databases such as MySQL, PostgreSQL, or MongoDB? (optional)
            10. Are you familiar with version control systems like Git? (required)
            11. Have you worked with Agile methodologies in your previous projects? (optional)
            12. Do you have experience in developing and deploying applications in cloud environments (e.g., AWS, Azure, Google Cloud Platform)? (optional)
            13. Have you ever led a team of developers in a project? (required)
            14. Are you comfortable working in a fast-paced startup environment? (required)
            15. Have you contributed to open-source projects before? (optional)
            16. Are you proficient in using front-end frameworks like Vue.js or Angular? (required)
            17. Have you ever conducted code reviews for other team members? (required)
            18. Are you familiar with continuous integration and continuous deployment (CI/CD) pipelines? (optional)
            19. Have you worked with RESTful APIs in your previous projects? (required)
            20. Are you experienced in using CSS preprocessors like Sass or Less? (optional)
            21. Have you built responsive web applications that work across multiple devices and screen sizes? (required)
            22. Are you comfortable working with UI/UX designers to implement their designs into functional web applications? (optional)
            23. Have you ever implemented authentication and authorization mechanisms in web applications? (required)
            24. Are you familiar with performance optimization techniques for web applications? (optional)
            25. Have you used testing frameworks like Jest or Mocha for unit and integration testing? (optional)
            26. Are you experienced in debugging and troubleshooting issues in web applications? (required)
            27. Have you ever worked on projects involving real-time web communication using WebSockets or similar technologies? (optional)
            28. Are you knowledgeable about web security best practices and common vulnerabilities? (required)
            29. Have you integrated third-party APIs into your web applications before? (optional)
            30. Are you experienced in optimizing web applications for search engine optimization (SEO)? (optional)
            31. Have you worked on projects involving data visualization using libraries like D3.js or Chart.js? (optional)
            32. Are you comfortable working with frontend build tools like Webpack or Parcel? (optional)
            33. Have you ever implemented internationalization (i18n) and localization (l10n) in web applications? (optional)
            34. Are you proficient in using design patterns in your code architecture? (required)
            35. Have you ever conducted technical interviews for hiring new developers? (optional)
            36. Are you experienced in mentoring junior developers and helping them grow their skills? (required)
            37. Have you contributed to documentation efforts for codebases or projects? (optional)
            38. Are you familiar with containerization technologies like Docker? (optional)
            39. Have you ever presented technical topics or projects at conferences or meetups? (optional)
            40. Are you passionate about staying up-to-date with the latest trends and advancements in web development? (required)
            41. What is your annual salary expectation? (required)
            42. How many years of remote working experience do you have? (optional)
            43. How many years of experience do you have with frontend development languages like JavaScript and/or React? (required)
            44. On a scale of 1-10 (10 being the best) how would you rate your skills with React? (required)
            45. On a scale of 1-10 (10 being the best) how would you rate your skills with JavaScript? (required)
            46. Annual salary expectations? (If you do not specify clearly, your application will not be reviewed/considered.) (required)
            
            Answers:
            1. 5
            2. 3
            3. Yes
            4. Yes
            5. Yes
            6. 6
            7. 8
            8. 9
            9. Yes
            10. Yes
            11. Yes
            12. Yes
            13. Yes
            14. Yes
            15. Yes
            16. Yes
            17. Yes
            18. Yes
            19. Yes
            20. Yes
            21. Yes
            22. Yes
            23. Yes
            24. Yes
            25. Yes
            26. Yes
            27. Yes
            28. Yes
            29. Yes
            30. Yes
            31. Yes
            32. Yes
            33. Yes
            34. Yes
            35. Yes
            36. Yes
            37. Yes
            38. Yes
            39. Yes
            40. Yes
            41. 100000
            42. 3
            43. 6
            44. 8
            45. 9
            46. 100000
            
            
            
        For each question, provide an accurate and precise answer.
        For numerical answers, use only numbers without any additional characters or letters.
        When asked about experience, respond with only the number.
        If asked about timing, reply with a random day of the week.
        If asked to list 2-3 dates and time ranges for an interview, pick 2 random days of the week.
        When asked about experience if user does not have experience in that skill, field or space just reply with 0.
        """

        fine_tune = self.openai_client.fine_tuning

        response = self.openai_client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role":"system",
                    "content": prompt,
                },
                {
                    "role": "user",
                    "content": question
                }
            ],
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        return response.choices[0].message.content

    def handle_radio_input(self, label_text):
        return "yes" if "yes" in label_text.lower() else "no"

    def handle_dropdown_input(self, label_text,job_description):
        return self.generate_response(label_text, job_description)

    def fill_input_fields(self, label_text, job_description):
        input_value = self.generate_response(label_text, job_description)
        print(input_value)
        return input_value

    def is_number(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def sanitize_number(self, value):
        if self.is_number(value):
            # Remove any extraneous characters and ensure it's formatted correctly
            sanitized_value = str(int(float(value)))
            return sanitized_value
        return value

    def fill_form_field(self, input_field, input_value):
        if input_value is not None:
            input_field.clear()  # Clear the field before entering new value
            input_field.send_keys(input_value)
            print(f"Input field filled with value: '{input_value}'.")
        else:
            print('Input value is None, skipping input field.')

    def fill_form(self, job_info):
        print('Searching for container div...')
        container_xpaths = [
            "//div[contains(@class, 'ia-BasePage-component') and contains(@class, 'ia-BasePage-component--withContinue')]",
            "//div[contains(@class, 'ia-BasePage') and contains(@class, 'ia-Questions') and contains(@class, 'ia-PageAnimation-enter-done')]"
        ]

        for container_xpath in container_xpaths:
            container_divs = self.driver.find_elements(By.XPATH, container_xpath)
            if container_divs:
                container_div = container_divs[0]  # Use the first found container div
                print('Container div found. Filling form...')
                labels = container_div.find_elements(By.TAG_NAME, 'label')
                print(f'Number of labels found: {len(labels)}')  # Print number of labels found

                for label in labels:
                    print('Processing label...')
                    label_text = self.get_label_text(label)
                    print(f'Label text: {label_text}')

                    # Check if label is optional
                    if "(optional)" in label_text:
                        print("Optional label found. Skipping input field.")
                        continue  # Skip to the next label if it's optional

                    input_id = label.get_attribute('for')
                    if input_id:
                        input_field = self.driver.find_element(By.ID, input_id)
                        if input_field:
                            input_type = input_field.get_attribute('type')
                            if input_type == 'radio':
                                input_value = self.handle_radio_input(label_text)
                                input_field.click()  # Select the radio button
                                print(f"Radio button '{input_value}' clicked.")
                            elif input_type == 'number':
                                input_value = self.fill_input_fields(label_text, job_info)
                                print(f'Input value to be filled: {input_value}')
                                if input_value is not None:  # Check if input_value is not None
                                    input_field.send_keys(int(input_value))
                                    print(f"Input field filled with value: '{int(input_value)}'.")
                                else:
                                    print('Input value is None, skipping input field.')
                            else:
                                input_value = self.fill_input_fields(label_text, job_info)
                                print(f'Input value to be filled: {str(input_value)}')
                                if input_value is not None:  # Check if input_value is not None
                                    input_field.send_keys(str(input_value))
                                    print(f"Input field filled with value: '{str(input_value)}'.")
                                else:
                                    print('Input value is None, skipping input field.')

                self.click_continue_button()
    # def get_label_text(self, label):
    #     try:
    #         label_span = label.find_element(By.TAG_NAME, 'span')
    #         return label_span.text()
    #     except:
    #         return label.text()
 # Define the method to get label text properly
    def get_label_text(self, label):
        span = label.find_elements(By.TAG_NAME, 'span')
        print(span)
        if span:
            return span[0].text.strip()
        return label.text.strip()

    def click_continue_button(self):
        try:
            # Check for the button with the specified class
            button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'ia-continueButton'))
            )
            button.click()
            print('Clicked button with class "ia-continueButton".')
        except:
            print('Button with class "ia-continueButton" not found.')

        try:
            # Check for a button inside a div with the specified class
            div = self.driver.find_element(By.CLASS_NAME, 'ia-Question-continue')
            button_in_div = div.find_element(By.TAG_NAME, 'button')
            button_in_div.click()
            print('Clicked button inside div with class "ia-Question-continue".')
        except:
            print('Button inside div with class "ia-Question-continue" not found.')


class GlassdoorJobAutomation:
    def __init__(self, driver):
        self.driver = driver
        self.openai_client = OpenAI(api_key=api_keyDetail)
    
    def get_job_details(self):
        show_more_btn = self.driver.find_element(By.XPATH, "//button[@class='JobDetails_showMore___Le6L']")
        show_more_btn.click()
        time.sleep(6)
        job_description_element = self.driver.find_element(By.XPATH, '//div[@class="JobDetails_jobDescriptionWrapper___tqxc JobDetails_jobDetailsSectionContainer__o_x6Z JobDetails_paddingTopReset__IIrci"]')
        job_description_with_tags = job_description_element.text
        time.sleep(6)
        return job_description_with_tags

    def get_job_info_gpt(self):
        job_description = self.get_job_details()
        time.sleep(10)
        completion = self.openai_client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role":"system",
                    "content": "\nExtract the following details from the job description:\n- Job Title:\n- Location:\n- Required Skills:\n- Qualifications:\n- Responsibilities:\n",
                },
                {
                    "role": "user",
                    "content": job_description
                }
            ],
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        # Extracted information from ChatGPT response
        job_details = completion.choices[0].message
        return job_details


class JobSearch:
    def __init__(self, driver):
        self.driver = driver
        self.job_automation = GlassdoorJobAutomation(driver)
        self.glassdoor_form_automation = None  # Initialize as None initially
        self.glassdoor_job_search_automation = None  # Initialize as None initially

    
    def get_glassdoor_job_search_automation(self):
        if self.glassdoor_job_search_automation is None:
            self.glassdoor_job_search_automation = GlassdoorJobSearchAutomation(self.driver)
        return self.glassdoor_job_search_automation
    
    def get_glassdoor_form_automation(self):
        if self.glassdoor_form_automation is None:
            self.glassdoor_form_automation = GlassdoorFormAutomation(self.driver)
        return self.glassdoor_form_automation
    

    def click_jobs(self):
        self.get_glassdoor_job_search_automation().close_popup()
        ul_element = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "//ul[@class='JobsList_jobsList__lqjTr']"))
        )
        li_elements = ul_element.find_elements(By.CSS_SELECTOR, 'li.JobsList_jobListItem__wjTHv.JobsList_dividerWithSelected__nlvH7')
        self.get_glassdoor_job_search_automation().close_popup()

        for index, li in enumerate(li_elements):
            self.get_glassdoor_job_search_automation().close_popup()
            try:
                self.driver.execute_script("arguments[0].scrollIntoView(true);", li)
                li.click()
                time.sleep(4)
                job_info = self.job_automation.get_job_info_gpt()
                if job_info == "":
                    pass
                else:
                    current_url = self.driver.current_url
                    self.get_glassdoor_job_search_automation().close_popup()
                    self.get_glassdoor_job_search_automation().click_apply_easy()  # Call the method here
                    time.sleep(4)
                    # # # Switch to the new tab
                    new_url = self.driver.current_url

                    if current_url == new_url:
                        time.sleep(5)
                        self.driver.switch_to.window(self.driver.window_handles[1])
                        GlassdoorFormAutomation(self.driver).automate_form(job_info)
                        self.driver.close()

                        # Switch back to the main tab
                        self.driver.switch_to.window(self.driver.window_handles[0])
                    else:
                        time.sleep(5)
                        GlassdoorFormAutomation(self.driver).automate_form(job_info)
                        time.sleep(4)
                        self.driver.back()
                        
                    # main_tab = self.driver.current_window_handle

                    # # Switch to the new tab
                    # self.driver.switch_to.window(self.driver.window_handles[1])

                    # # Wait until the page loads completely (you can change the condition based on your requirements)
                    # WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
                    # self.get_glassdoor_job_search_automation().close_popup()
                    # # Check if the page has changed from the main tab
                    # if self.driver.current_window_handle != main_tab:
                    #     # Perform actions specific to the new tab
                    #     time.sleep(4)
                    #     GlassdoorFormAutomation(self.driver).automate_form()

                    #     # Close the new tab
                    #     self.driver.close()

                    #     # Switch back to the main tab
                    #     self.driver.switch_to.window(main_tab)
                    # else:
                    #     # Perform actions specific to the main tab
                    #     time.sleep(4)
                    #     GlassdoorFormAutomation(self.driver).automate_form()
                    # WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
                    # driver.switch_to.window(driver.window_handles[1])
                    # time.sleep(4)
                    # self.get_glassdoor_form_automation().automate_form()
                    # time.sleep(4)
                    # # # Close the new tab and switch back to the original tab
                    # driver.close()
                    # driver.switch_to.window(driver.window_handles[0])
                time.sleep(12)
            except Exception as e:
                print(f"Error occurred while processing li index {index}: {e}")

# ia-PreviewSection-link
# css-mza3f0 e37uo190
# css-besaou e1jgz0i2



class GlassdoorFormAutomation:
    def __init__(self, driver):
        self.check = None
        self.driver = driver
        self.glassdoor_job_search_automation = None
        self.automate_form_filler = FormFiller(driver)

    def check_section(self):
        if self.check is None:
            self.check = JobApplicationAutomation(self.driver)
        return self.check

    def get_glassdoor_job_search_automation(self):
        if self.glassdoor_job_search_automation is None:
            self.glassdoor_job_search_automation = GlassdoorJobSearchAutomation(self.driver)
        return self.glassdoor_job_search_automation
    
    # def auto_filler(self):
    #     if self.automate_form_filler is None:
    #         self.automate_form_filler = FormFiller(self.driver)
    #     return self.automate_form_filler()

    def fill_input_fields(self, input_details):
        self.get_glassdoor_job_search_automation().close_popup()
        for input_id, value in input_details.items():
            try:
                field = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, f"input#{input_id}"))
                )
                field.clear()
                field.send_keys(value)
            except Exception as e:
                print(f"Field with ID {input_id} not found. Error: {str(e)}. Skipping.")

    def click_button(self, css_selector):
        self.get_glassdoor_job_search_automation().close_popup()
        try:
            button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))
            )
            button.click()
        except Exception as e:
            print(f"Button not found. Error: {str(e)}.")

    def upload_resume(self):
        self.get_glassdoor_job_search_automation().close_popup()
        try:
            file_input = self.driver.find_element(By.CSS_SELECTOR, "input[data-testid='FileResumeCard-file-input']")
            file_input.send_keys('/home/bmn/Downloads/Resume.pdf')
        except Exception as e:
            print(f"Error uploading the file. Error: {str(e)}.")

    def automate_form(self, job_info):
        self.get_glassdoor_job_search_automation().close_popup()
        input_details = {
            "input-firstName": "Brilliant",
            "input-lastName": "Makanju",
            "input-phoneNumber": "+2349015573136",
            "input-email": "brilliantmakanju5@gmail.com",
            # "input-location.city": "Lagos State",
            # "file-resume-input": '/home/bmn/Downloads/Resume.pdf'  # The file path for the resume upload
        }
        try:
            self.fill_input_fields(input_details)
            time.sleep(3)
            self.click_button('.ia-continueButton.ia-ContactInfo-continue.css-sbr3v1.e8ju0x50')
            time.sleep(3)
            self.upload_resume()
            time.sleep(3)
            self.click_button('.ia-continueButton.ia-Resume-continue.css-sbr3v1.e8ju0x50')
            time.sleep(3)
            print('started dev')
            check_section = self.check_section().check_current_section()
            if check_section == True:
                self.automate_form_filler.fill_form(job_info)
            else:
                self.check_section().fill_cv()
            print('dev ended successfully or failed')
        except Exception as e:
            print(f"An error occurred: {e}")

    #     self.glassdoor_job_search_automation = None  # Initialize as None initially

    
    # def get_glassdoor_job_search_automation(self):
    #     if self.glassdoor_job_search_automation is None:
    #         self.glassdoor_job_search_automation = GlassdoorJobSearchAutomation(self.driver)
    #     return self.glassdoor_job_search_automation

# success apply: icon-button_IconButton__nMTOc

class GlassdoorJobSearchAutomation:
    def __init__(self, driver):
        self.driver = driver
        self.job_search = JobSearch(driver)
        self.form_automation = GlassdoorFormAutomation(driver)

    def search_job(self):
        self.close_popup()
        inputTitle = self.driver.find_element(By.ID, "searchBar-jobTitle")
        inputTitle.send_keys("frontend")
        inputTitle.submit()
        time.sleep(3)
        self.get_easy_apply()

    def get_easy_apply(self):
        self.close_popup()
        filter_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "SearchFiltersBar_pill__cT_sS"))
        )
        filter_btn.click()

        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'SearchFiltersBar_labelButton__gF32h') and contains(text(), 'Most relevant')]"))
        )
        button.click()
        time.sleep(1)

        button_recent = WebDriverWait(self.driver, 1).until(
            EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'SearchFiltersBar_dropdownOptionLabel___af5z') and contains(text(), 'Most recent')]"))
        )
        button_recent.click()
        time.sleep(3)

        # showmore = self.showmore_job()
        # print(showmore)
        # if showmore:
        self.job_search.click_jobs()
        # else:
        #     pass

    def showmore_job(self):
        self.close_popup()
        load_complete = False
        while not load_complete:
            self.close_popup()
            try:
                self.close_popup()
                show_more_button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[@data-test='load-more']"))
                )
                show_more_button.click()
                time.sleep(4)
                self.close_popup()

                try:
                    self.close_popup()
                    show_more_button = WebDriverWait(self.driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, "//button[@data-test='load-more']"))
                    )
                    self.close_popup()
                    load_complete = not show_more_button.is_displayed()
                except TimeoutException:
                    self.close_popup()
                    load_complete = True

            except StaleElementReferenceException:
                self.close_popup()
                print("Stale element reference error. Retrying...")
                continue
            except Exception as e:
                self.close_popup()
                print(f"Error occurred: {e}. Stopping the loop.")
                load_complete = True
        self.close_popup()
        return load_complete

    def close_popup(self):
        try:
            close_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "CloseButton"))
            )
            close_btn.click()
        except (TimeoutException, StaleElementReferenceException):
            print("Close button not found or stale.")

    def click_apply_easy(self):
        self.close_popup()
        try:
            button = self.driver.find_element(By.XPATH, '//button[@data-test="easyApply"]')
            button.click()
            print("Button clicked successfully!")
            time.sleep(5)
        except Exception as e:
            print(f"Button not found. Error: {str(e)}.")

    # def click_jobs(self):
    #     ul_element = WebDriverWait(self.driver, 30).until(
    #         EC.presence_of_element_located((By.XPATH, "//ul[@class='JobsList_jobsList__lqjTr']"))
    #     )
    #     li_elements = ul_element.find_elements(By.CSS_SELECTOR, 'li.JobsList_jobListItem__wjTHv.JobsList_dividerWithSelected__nlvH7')

    #     for index, li in enumerate(li_elements):
    #         try:
    #             self.driver.execute_script("arguments[0].scrollIntoView(true);", li)
    #             li.click()
    #             self.close_popup()
    #             time.sleep(10)
    #             self.click_apply_easy()
    #             time.sleep(10)
    #         except Exception as e:
    #             print(f"Error occurred while processing li index {index}: {e}")


if __name__ == "__main__":
    user_agent = UserAgent()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f"user-agent={user_agent.random}")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.glassdoor.com/Job/index.htm")
    time.sleep(3)

    glassdoor_automation = GlassdoorJobSearchAutomation(driver)
    glassdoor_automation.search_job()
