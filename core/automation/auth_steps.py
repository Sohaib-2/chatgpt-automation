import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from core.locators import (
    LOGIN_BUTTON, 
    EMAIL_INPUT, 
    EMAIL_CONTINUE_BUTTON,
    PASSWORD_INPUT, 
    PASSWORD_CONTINUE_BUTTON,
    LOGGED_IN_INDICATOR
)

def login_to_chatgpt(driver, email, password):
    try:
        driver.get("https://chat.openai.com/")
        time.sleep(3)
        
        # Check if already logged in
        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, LOGGED_IN_INDICATOR))
            )
            return True
        except:
            pass
        
        # Click login button
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, LOGIN_BUTTON))
        )
        login_button.click()
        time.sleep(2)
        
        # Enter email
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, EMAIL_INPUT))
        )
        for char in email:
            email_input.send_keys(char)
            time.sleep(0.1)
        
        # Continue after email
        continue_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, EMAIL_CONTINUE_BUTTON))
        )
        continue_button.click()
        time.sleep(2)
        
        # Enter password
        password_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, PASSWORD_INPUT))
        )
        for char in password:
            password_input.send_keys(char)
            time.sleep(0.1)
        
        # Continue after password
        continue_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, PASSWORD_CONTINUE_BUTTON))
        )
        continue_button.click()
        
        # Wait for ChatGPT to load
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, LOGGED_IN_INDICATOR))
        )
        
        return True
    except Exception as e:
        print(f"Login error: {e}")
        return False