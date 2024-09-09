from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def search_for_item(self, search_query):
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.clear()
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)

    def navigateToHome(self):
        # Get all window handles
        window_handles = self.driver.window_handles
        # Switch back to the original tab (the first one in the list)
        self.driver.switch_to.window(window_handles[0])
        home_button = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,
                                               "//div[@id='container']/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]")))
        home_button.click()

    def closeButton(self):
        try:
            # Wait until the close button is visible
            close_button = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div/span")))
            # Check if the close button is displayed
            if close_button.is_displayed():
                close_button.click()
        except Exception as e:
            # Handle exceptions if the element is not found or other issues arise
            print(f"An error occurred: {e}")
