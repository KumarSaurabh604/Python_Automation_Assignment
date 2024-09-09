import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from uibddpytest.pages.Base import SetDataInFile, GetDataFromFile


class CartPage:
    def __init__(self, driver):
        driver.execute_script("document.body.style.zoom='75%'")
        self.driver = driver
        self.cart_items = []

    def search_for_item(self):
        try:
            cart_icon = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//header/div[2]/div[3]/div[1]"))
            )
            cart_icon.click()
        except Exception as e:
            print(f"Error clicking cart icon: {e}")
            raise

    def is_item_present(self, item_name):
        try:
            item = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, f"//a[contains(text(),'{item_name}')]"))
            )
            return item.is_displayed()
        except Exception as e:
            print(f"Item not found: {e}")
            return False

    def verify_total_price(self):
        try:
            self.get_item_prices()
            expected_total = sum(self.cart_items)
            actual_total = self.get_total_price()
            return expected_total == actual_total
        except Exception as e:
            print(f"Error verifying total price: {e}")
            return False

    def get_item_prices(self):
        try:
            price_elements = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((By.XPATH, "//span[contains(@class, 'LAlF6k re6bBo')]"))
            )
            self.cart_items = [float(price.text.replace('₹', '').replace(',', '')) for price in price_elements]
            return self.cart_items
        except Exception as e:
            print(f"Error fetching item prices: {e}")
            return []

    def get_total_price(self):
        try:
            total_price_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH,
                                                '//body/div[@id="container"]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[2]/span[1]/div[1]/div[1]/div[2]/span'))
            )
            total_price = float(total_price_element.text.replace('₹', '').replace(',', ''))
            SetDataInFile('total_price_before_deletion', 'price', total_price)
            return total_price
        except Exception as e:
            print(f"Error fetching total price: {e}")
            return 0.0

    def remove_item(self, item_name):
        try:
            item_xpath = f"//div[contains(@class, 'x9LoV+') and contains(., '{item_name}')]"
            remove_button_xpath = f"{item_xpath}//parent::div/following-sibling::div[contains(@class,'d+mEZR JefwG6')]//div[contains(@class, 'sBxzFz') and text()='Remove']"
            remove_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, remove_button_xpath)))
            self.driver.execute_script("window.scrollBy(0, 200);")
            # Click the remove button to remove the item
            remove_button.click()

            confirm_remove_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div/div[1]//div[contains(@class, "sBxzFz") and text()="Remove"]')))
            confirm_remove_button.click()
            time.sleep(2)
        except Exception as e:
            print(f"Error removing item: {e}")
            raise

    def price_after_removed_item(self):
        try:
            total_price_before_deletion = GetDataFromFile("total_price_before_deletion", "price")
            print("Total price before deletion: " + total_price_before_deletion)

            updated_total_price_element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//body/div[@id="container"]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[4]/div[1]/div[2]/span[1]/div[1]/div[1]/div[2]/span')))
            total_price_after_deletion = float(updated_total_price_element.text.replace('₹', '').replace(',', ''))
            print("Total price after deletion: " + str(total_price_after_deletion))
            return str(total_price_after_deletion) < total_price_before_deletion
        except Exception as e:
            print(f"Error calculating price after item removal: {e}")
            return False
