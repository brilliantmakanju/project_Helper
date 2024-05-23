   # current_url = driver.current_url
    # print(current_url)

    # try:
    #     # Wait for the iframe to be present
    #     # wait = WebDriverWait(driver, 20)
    #     # iframe = wait.until(EC.presence_of_element_located((By.ID, 'SA_PRELOAD_ASSETS_IFRAME_ID')))
    #     # print("iFrame found")

    #     # # Switch to the iframe
    #     # driver.switch_to.frame(iframe)
    #     # print("Switched to iFrame")

    #     # # Wait for the specific element inside the iframe to be visible
    #     # container = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.ia-BasePage-component.ia-BasePage-component--withContinue')))
    #     # print("Element inside iFrame found")

    #     # Get the page source of the iframe content
    #     iframe_html_content = driver.page_source

    #     # Parse the HTML content using BeautifulSoup
    #     soup = BeautifulSoup(iframe_html_content, 'html.parser')

    #     # Print the parsed HTML
    #     # print(soup.prettify())

    #     form_html = soup.prettify()

    #     with open('page_source.html', 'w', encoding='utf-8') as file:
    #         file.write(form_html)
    #         print("HTML saved successfully")


    # except Exception as e:
    #     print(f"An error occurred: {e}")

    # finally:
    #     # Clean up and close the browser
    #     driver.quit()


    # # Wait for the iframe to be present
    #     wait = WebDriverWait(driver, 20)
    #     iframe = wait.until(EC.presence_of_element_located((By.ID, 'SA_PRELOAD_ASSETS_IFRAME_ID')))
    #     print("iFrame found")

    #     # Switch to the iframe
    #     driver.switch_to.frame(iframe)
    #     print("Switched to iFrame")

    #     # Wait for the specific element inside the iframe to be visible
    #     container = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.ia-BasePage-component.ia-BasePage-component--withContinue')))
    #     print("Element inside iFrame found")

    #     # Get the page source of the iframe content
    #     iframe_html_content = driver.page_source

    #     # Parse the HTML content using BeautifulSoup
    #     soup = BeautifulSoup(iframe_html_content, 'html.parser')

    #     # Print the parsed HTML
    #     print(soup.prettify())






    # wait = WebDriverWait(driver, 20)
    # iframe = wait.until(EC.presence_of_element_located((By.ID, 'SA_PRELOAD_ASSETS_IFRAME_ID')))

    # # Switch to the iframe
    # driver.switch_to.frame(iframe)

    # # Optionally wait for the content inside the iframe to load
    # # For example, wait for the specific div to be visible
    # container = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.ia-BasePage-component.ia-BasePage-component--withContinue')))

    # # Get the page source of the iframe content
    # iframe_html_content = driver.page_source

    # # Parse the HTML content using BeautifulSoup
    # soup = BeautifulSoup(iframe_html_content, 'html.parser')

    # # Print the parsed HTML
    # print(soup.prettify())






    # wait = WebDriverWait(driver, 20)
    # # Get the page source after the page is fully loaded
    # html_content = driver.page_source
    
    # # Parse the HTML content using BeautifulSoup
    # soup = BeautifulSoup(html_content, 'html.parser')
    
    # # Print the parsed HTML
    # print(soup.prettify())
    # driver.implicitly_wait(10)

    # Wait for the iframe to be present and switch to it
    # wait = WebDriverWait(driver, 20)
    # iframe = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'iframe')))
    # driver.switch_to.frame(iframe)

    # # Now wait for the specific div containing the form to be visible
    # container = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.ia-BasePage-component.ia-BasePage-component--withContinue')))

    # Get the page source after the div is loaded and visible
    # html_content = driver.page_source

    # # Parse the HTML content using BeautifulSoup
    # soup = BeautifulSoup(html_content, 'html.parser')

    # # Print the parsed HTML
    # print(soup.prettify())


    # # Locate the container element using XPath
    # container = driver.find_element(By.XPATH, '//div[contains(@class, "ia-BasePage-component") and contains(@class, "ia-BasePage-component--withContinue")]')

    # # Get all input elements within the container using XPath
    # input_elements = container.find_elements(By.XPATH, './/input')

    # # Print the input elements
    # for input_element in input_elements:
    #     print(f"Input ID: {input_element.get_attribute('id')}, Name: {input_element.get_attribute('name')}, Type: {input_element.get_attribute('type')}")




    # except Exception as e:
    #     print(f'Could not locate or interact with the input field. Error: {e}')
    #     driver.find_element(By.ID, 'input-firstName')
    # try:
    #     # Wait until the input field is present and visible
    #     input_field = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.XPATH, field_xpath))
    #     )
    #     WebDriverWait(driver, 10).until(
    #         EC.visibility_of(input_field)
    #     )
    #     input_field.send_keys(value)
    #     print(f'Filled input field: {field_xpath}')
    # except Exception as e:
    #     print(f'Could not locate or interact with the input field: {field_xpath}. Error: {e}')



    
    # fill_input_field_with_js(webdriver, 'input[id="input-firstName"]', 'Brilliant')
    # input_fields(webdriver)
    # filterBtnRecent = webdriver.find_element(By.CLASS_NAME, 'SearchFiltersBar_dropdown__3iNIB SearchFiltersBar_dropdownOption__qEIBz')
    # filterBtnRecent.click()

        # Perform actions in the new tab
    # print(f"New Tab URL: {webdriver.current_url}")
    # fill_input_field(span_selector, input_selector, value, webdriver)





# def fill_input_field(span_selector, input_selector, value, driver):
#     try:
#         # Wait for the span containing the input field to be present
#         span = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, span_selector))
#         )
#         print(span)
#         #
#         #  Once the span is located, find the input field within the span
#         input_field = WebDriverWait(span, 10).until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, input_selector))
#         )
#         print(input_field)
#         # Ensure the input field is visible and interactable
#         input_field = WebDriverWait(driver, 10).until(
#             EC.element_to_be_clickable((By.CSS_SELECTOR, input_selector))
#         )
#         print(input_field)
#         # Clear the input field and enter the desired value
#         input_field.clear()
#         input_field.send_keys(value)
#     except Exception as e:
#         print(f"Could not locate or interact with the input field. Error: {str(e)}")

# def fill_input_field(span_selector, input_selector, value, driver):
#     try:
#         # Wait for the span containing the input field to be present
#         span = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, span_selector))
#         )
#         # Use JavaScript to find and fill the input field
#         script = f"""
#             var span = document.querySelector('{span_selector}');
#             var input = span.querySelector('{input_selector}');
#             if (input) {{
#                 input.value = '{value}';
#                 input.dispatchEvent(new Event('input', {{ bubbles: true }}));
#             }}
#         """
#         driver.execute_script(script)
#     except Exception as e:
#         print(f"Could not locate or interact with the input field. Error: {str(e)}")

# # Define the selectors and value to fill
# span_selector = "span.css-1owegx3.e6fjgti1"
# input_selector = "input#input-firstName"
# value = "John"


# def fill_input_field_with_actionchains(driver, field_selector, value):
#     try:
#         # Wait until the input field is present
#         input_field = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, field_selector))
#         )
#         # Move to the element and click it using ActionChains
#         actions = ActionChains(driver)
#         actions.move_to_element(input_field).click().perform()
#         # Send the value to the input field
#         input_field.clear()
#         input_field.send_keys(value)
#         print(f'Filled input field: {field_selector}')
#     except Exception as e:
#         print(f'Could not locate or interact with the input field: {field_selector}. Error: {e}')


# def fill_input_field_with_js(driver, field_selector, value):
#     try:
#         # Wait until the input field is present
#         WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, field_selector))
#         )
#         # Use JavaScript to set the value of the input field
#         driver.execute_script(f'document.querySelector("{field_selector}").value = "{value}";')
#         print(f'Filled input field: {field_selector}')
#     except Exception as e:
#         print(f'Could not locate or interact with the input field: {field_selector}. Error: {e}')
















    # css-lwkpjt
    # time.sleep(20)
    # input_id = 'input-firstName'
    # value = 'Brilliant'
    # time.sleep(50)
    # try:
    #     # Use a more specific CSS selector to target the input field
    #     field = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.CSS_SELECTOR, f"input#{input_id}"))
    #     )
    #     # Wait until the field is clickable
    #     field = WebDriverWait(driver, 10).until(
    #         EC.element_to_be_clickable((By.CSS_SELECTOR, f"input#{input_id}"))
    #     )
    #     # Clear the field and fill it with the provided value
    #     field.clear()
    #     field.send_keys('Brilliant')
    # except Exception as e:
    #     print(f"Field with ID {input_id} not found. Error: {str(e)}")
    #     # Try to locate using JavaScript as a fallback
    #     try:
    #         field = driver.find_element(By.CSS_SELECTOR, f"input#{input_id}")
    #         driver.execute_script("arguments[0].value = arguments[1];", field, value)
    #     except Exception as js_error:
    #         print(f"JavaScript execution failed for field {input_id}. Error: {str(js_error)}")

    # field = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.CSS_SELECTOR, "#input-firstName.css-lwkpjt"))
    # )

    # for input_id, value in input_details.items():
    #     try:
    #         # Use a more specific CSS selector to target the input field
    #         field = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located((By.CSS_SELECTOR, f"input#{input_id}"))
    #         )
    #         # Wait until the field is clickable
    #         field = WebDriverWait(driver, 10).until(
    #             EC.element_to_be_clickable((By.CSS_SELECTOR, f"input#{input_id}"))
    #         )
    #         # Clear the field and fill it with the provided value
    #         field.clear()
    #         field.send_keys(value)
    #     except Exception as e:
    #         print(f"Field with ID {input_id} not found. Error: {str(e)}. Skipping.")
    #         try:
    #             field = driver.find_element(By.CSS_SELECTOR, f"input#{input_id}")
    #             driver.execute_script("arguments[0].value = arguments[1];", field, value)
    #         except Exception as js_error:
    #             print(f"JavaScript execution failed for field {input_id}. Error: {str(js_error)}")

    # field = driver.find_element(By.CSS_SELECTOR, "input#input-firstName.css-lwkpjt.e1jgz0i3")
    # field.send_keys('Brilliant')
    # time.sleep(300)
    # for input_id, value in input_details.items():
    #     try:
    #         # Use a more specific CSS selector to target the input field
    #         field = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located((By.CSS_SELECTOR, f"input#{input_id}"))
    #         )
    #         # Wait until the field is clickable
    #         field = WebDriverWait(driver, 10).until(
    #             EC.element_to_be_clickable((By.CSS_SELECTOR, f"input#{input_id}"))
    #         )
    #         # Clear the field and fill it with the provided value
    #         field.clear()
    #         field.send_keys(value)
    #     except Exception as e:
    #         # If direct interaction fails, use JavaScript to set the value
    #         print(f"Direct interaction with field {input_id} failed. Using JavaScript. Error: {str(e)}")
    #         try:
    #             field = driver.find_element(By.CSS_SELECTOR, f"input#{input_id}")
    #             driver.execute_script("arguments[0].value = arguments[1];", field, value)
    #         except Exception as js_error:
    #             print(f"JavaScript execution failed for field {input_id}. Error: {str(js_error)}")


    # for xpath, value in input_details.items():
    #     try:
    #         field = WebDriverWait(driver, 10).until(
    #             EC.presence_of_element_located((By.XPATH, xpath))
    #         )
    #         field = WebDriverWait(driver, 10).until(
    #             EC.element_to_be_clickable((By.XPATH, xpath))
    #         )
    #         field.clear()
    #         field.send_keys(value)
    #     except Exception as e:
    #         print(f"Field with XPath {xpath} not found. Error: {str(e)}. Skipping.")
    #         try:
    #             field = driver.find_element(By.XPATH, xpath)
    #             driver.execute_script("arguments[0].value = arguments[1];", field, value)
    #         except Exception as js_error:
    #             print(f"JavaScript execution failed for field {xpath}. Error: {str(js_error)}")

    # time.sleep(2)





















#     def input_fields(driver):
#     for input_id, value in input_details.items():
#         try:
#             # Wait until the field is present and visible
#             field = WebDriverWait(driver, 10).until(
#                 EC.presence_of_element_located((By.CSS_SELECTOR, f"input#{input_id}"))
#             )
#             # # Wait until the field is clickable
#             field = WebDriverWait(driver, 10).until(
#                 EC.element_to_be_clickable((By.CSS_SELECTOR, f"input#{input_id}"))
#             )
#             # Clear the field and fill it with the provided value
#             field.clear()
#             field.send_keys(value)
#         except Exception as e:
#             # If the field is not found, continue to the next one
#             print(f"Field with ID {input_id} not found. Error: {str(e)}. Skipping.")

#     wait = WebDriverWait(driver, 10)
#     continue_button = wait.until(
#         EC.element_to_be_clickable((By.CSS_SELECTOR, '.ia-continueButton.ia-ContactInfo-continue.css-sbr3v1.e8ju0x50'))
#     )

#     # Click the button
#     continue_button.click()

#     time.sleep(20)
# # JobsList_jobsList__lqjTr
