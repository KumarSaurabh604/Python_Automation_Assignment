import time
from selenium.webdriver.common.by import By
from uibddpytest.pages.Base import SetDataInFile


class SearchResultsPage():
    def __init__(self, driver):
        driver.execute_script("document.body.style.zoom='75%'")
        self.driver = driver

    def select_second_item(self, item):
        try:
            if item == '"Samsung S23 128 GB"':
                item_name = self.driver.find_element(By.XPATH, '//body/div[@id="container"]/div[1]/div[3]/div[1]/div[2]/div[3]/div[1]/div[1]/div[1]/a[1]/div[2]/div[1]/div[1]')
                SetDataInFile('productPage', 'first_item', item_name.text)
            else:
                item_name = self.driver.find_element(By.XPATH, '//div[@id="container"]/div[1]/div[3]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/a[2]')
                SetDataInFile('productPage', 'second_item', item_name.text)
            item_name.click()
            # Wait a bit for the new tab to open
            time.sleep(2)
        except Exception as e:
            print(f"Error occurred: {e}")
            raise

