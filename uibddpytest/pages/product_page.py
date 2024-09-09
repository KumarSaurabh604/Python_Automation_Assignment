import os
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException


class ProductPage:

    def __init__(self, driver):
        try:
            self.driver = driver
            self.driver.execute_script("document.body.style.zoom='85%'")
        except WebDriverException as e:
            print(f"Error setting zoom level: {e}")
            raise

    def enter_pin_code_and_check_availability(self, param, product):
        try:
            # Get all window handles
            window_handles = self.driver.window_handles
            # Switch to the new tab (the second window handle)
            if product == '"mobile"':
                self.driver.switch_to.window(window_handles[1])
                # self.driver.execute_script("document.body.style.zoom='85%'")
                # Scroll down by 800 pixels
                self.driver.execute_script("window.scrollBy(0, 800);")
                # Wait for the tooltip to become visible and locate it
                wait = WebDriverWait(self.driver, 10)

                pincode_input = wait.until(EC.visibility_of_element_located((By.ID, "pincodeInputId")))
                pincode_input.clear()
                pincode_input.send_keys(param)

                check_button = wait.until(EC.visibility_of_element_located((By.XPATH,
                                                                            "//span[contains(text(), 'Check') or contains(text(),'Change')]")))
                check_button.click()
            else:
                self.driver.switch_to.window(window_handles[2])

                self.driver.execute_script("document.body.style.zoom='75%'")
                # Scroll down by 800 pixels
                self.driver.execute_script("window.scrollBy(0, 800);")
        except TimeoutException:
            print("Timeout while waiting for elements to load.")
            raise
        except NoSuchElementException as e:
            print(f"Element not found: {e}")
            raise
        except AssertionError as e:
            print(f"Assertion Error: {e}")
            raise
        except WebDriverException as e:
            print(f"WebDriver Error: {e}")
            raise

    def add_to_cart(self):
        try:
            # Initialize WebDriverWait
            wait = WebDriverWait(self.driver, 10)

            # Wait for the add button to be visible and clickable
            add_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="container"]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[1]')))

            # Click the add button
            add_button.click()
        except Exception as e:
            print(f"Error occurred while adding item to cart: {e}")
            raise
