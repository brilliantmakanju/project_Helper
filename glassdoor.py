import os
import time
import random
import string
from bs4 import BeautifulSoup
from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

def navigate_page(webdriver):
    pass

# continue button className .ia-continueButton.ia-Resume-continue.css-sbr3v1.e8ju0x50

# Define the input field details
# Define the input field details
input_details = {
    "input-firstName": "Brilliant",
    "input-lastName": "Makanju",
    "input-phoneNumber": "+2349015573136",
    "input-email": "brilliantmakanju5@gmail.com",
    # "input-location.city": "Lagos State",
    # "file-resume-input": '/home/bmn/Downloads/Resume.pdf'  # The file path for the resume upload
}

# Function to fill input fields
def fill_input_fields(driver, input_details):
    for input_id, value in input_details.items():
        try:
            field = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, f"input#{input_id}"))
            )
            field.clear()
            field.send_keys(value)
        except Exception as e:
            print(f"Field with ID {input_id} not found. Error: {str(e)}. Skipping.")

# Function to click a button by its CSS selector
def click_button(driver, css_selector):
    try:
        button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))
        )
        button.click()
    except Exception as e:
        print(f"Button not found. Error: {str(e)}.")

# Function to upload a resume
def upload_resume(driver):
    try:
        # radio_button = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "input#ihl-useId-indeed-theme-provider-hbgkkv-1-file-resume-input"))
        # )
        # radio_button.click()
        # label = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.CSS_SELECTOR, "label.css-mza3f0.e37uo190"))
        # )
        # label.click()
        file_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='FileResumeCard-file-input']")

        # file_input = driver.find_element_by_css_selector("input[data-testid='FileResumeCard-file-input']")

        # # Send the file path to the file input
        file_input.send_keys('/home/bmn/Downloads/Resume.pdf')
    except Exception as e:
        print(f"Error uploading the file. Error: {str(e)}.")

# Function to fill dynamic experience fields
def fill_experience_fields(driver):
    try:
        # Example static experience fields
        experience_fields = {
            "How many years of Front-end development experience do you have?": "3",
            "How many years of CSS experience do you have?": "3",
            "How many years of React experience do you have?": "2"
        }
        
        # Fill out each experience field
        for question, answer in experience_fields.items():
            try:
                question_element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"//*[text()='{question}']/following-sibling::input"))
                )
                question_element.clear()
                question_element.send_keys(answer)
            except Exception as e:
                print(f"Experience question '{question}' not found. Error: {str(e)}. Skipping.")
    except Exception as e:
        print(f"Error filling experience fields. Error: {str(e)}.")

# Function to fill job experience form
def fill_job_experience_form(driver):
    try:
        job_details = {
            "input-jobTitle": "Front-end Developer",
            "input-company": "Tech Company"
        }
        
        for input_id, value in job_details.items():
            try:
                field = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, f"input#{input_id}"))
                )
                field.clear()
                field.send_keys(value)
            except Exception as e:
                print(f"Field with ID {input_id} not found. Error: {str(e)}. Skipping.")
    except Exception as e:
        print(f"Error filling job experience form. Error: {str(e)}.")

# Main function to automate the form process
def automate_form(driver, input_details):
    try:
        # Open the target URL # Replace with your actual URL
        
        # Fill initial form
        fill_input_fields(driver, input_details)
        time.sleep(3)
        # Click the Continue button
        click_button(driver, '.ia-continueButton.ia-ContactInfo-continue.css-sbr3v1.e8ju0x50')
        time.sleep(3)
        # Upload the resume
        upload_resume(driver)
        time.sleep(3)
        # Click the Continue button
        click_button(driver, '.ia-continueButton.ia-Resume-continue.css-sbr3v1.e8ju0x50')
        time.sleep(3)
        
        # Fill dynamic experience fields
        # # fill_experience_fields(driver)
        
        # # Click the Continue button
        # click_button(driver, '.ia-continueButton.ia-ContactInfo-continue.css-sbr3v1.e8ju0x50')
        
        # # Fill job experience form
        # fill_job_experience_form(driver)
        
        # # Click the final Continue button
        # click_button(driver, '.ia-continueButton.ia-ContactInfo-continue.css-sbr3v1.e8ju0x50')
        
    except Exception as e:
        print(f"An error occurred: {e}")

def get_easy_apply(webdriver):
        # Wait for the filter button to be clickable
    filter_btn = WebDriverWait(webdriver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "SearchFiltersBar_pill__cT_sS"))
    )
    filter_btn.click()

    # Wait for the "Most recent" button to be clickable
    button = WebDriverWait(webdriver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'SearchFiltersBar_labelButton__gF32h') and contains(text(), 'Most relevant')]"))
    )
    button.click()
    time.sleep(1)
    # SearchFiltersBar_dropdownOption__qEIBz

    button_recent = WebDriverWait(webdriver, 1).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'SearchFiltersBar_dropdownOptionLabel___af5z') and contains(text(), 'Most recent')]"))
    )
    button_recent.click()
    time.sleep(1)

    # Button_greenTheme__EXYIV
    button_apply = WebDriverWait(webdriver, 1).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'JobDetails_applyButtonContainer__L36Bs')]"))
    )
    button_apply.click()
    time.sleep(30)
    original_window = webdriver.current_window_handle
    new_window = [window for window in webdriver.window_handles if window != original_window][0]

    # Switch to the new window
    webdriver.switch_to.window(new_window)

    time.sleep(10)
    automate_form(webdriver, input_details)




def search_job(webdriver):
    inputTitle = webdriver.find_element(By.ID, "searchBar-jobTitle")
    inputTitle.send_keys("frontend")
    inputTitle.submit()
    get_easy_apply(webdriver)
    print("testing2")


# Define the selectors and value to fill
span_selector = "span.css-1owegx3.e6fjgti1"
input_selector = "input#input-firstName"
value = "John"

if __name__ == "__main__":
    # authorized = input('Are you authorized to work outside your country (true or false): ')
    # jobs_skill = input("Enter your search keyword(frontend, backend): ")
    # phone = input('Enter your phone number (without country code): ')
    # experience = input('Enter no of experience with skills: ')
    # country_code = input('Enter your Country code (+1): ')
    # desired_salary = input("Enter your desired Salary: ")
    # resume_path = "/home/bmn/Downloads/Resume.pdf"
    # firstname = input('Enter your firstname: ')
    # lastname = input('Enter your lastname: ')
    # email = input('Enter your email: ')

    print("testing")
    # Proxy = "139.99.148.90:3128" 
    user_agent = UserAgent()

    # Set up Chrome options
    chrome_options = webdriver.ChromeOptions()

    # Add a random user-agent to Chrome options
    chrome_options.add_argument(f"user-agent={user_agent.random}")

    # Initialize the WebDriver with Chrome options
    driver = webdriver.Chrome(options=chrome_options)
    # Initialize the WebDriver (this example uses Chrome; make sure you have the appropriate WebDriver installed)
    # driver = webdriver.Chrome(desired_capabilities=capabilities)
    driver.get("https://www.glassdoor.com/Job/index.htm")
    time.sleep(10)
    search_job(driver)
