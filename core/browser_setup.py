import os
import json
import time
from seleniumbase import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from core.locators import LOGGED_IN_INDICATOR

def setup_browser(headless=False):
    """
    Set up and configure the browser.
    
    Args:
        headless (bool): Whether to run browser in headless mode
        
    Returns:
        driver: Configured Selenium webdriver
    """
    driver = Driver(uc=True, headless=headless)
    
    # If not headless, maximize window
    if not headless:
        driver.maximize_window()
        
    driver.implicitly_wait(10)
    return driver

def save_cookies(driver, path="data/cookies/chatgpt_cookies.json"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as file:
        json.dump(driver.get_cookies(), file)
    return True

def load_cookies(driver, path="data/cookies/chatgpt_cookies.json"):
    if not os.path.exists(path):
        return False
    
    try:
        driver.get("https://chat.openai.com/")
        time.sleep(2)
        
        with open(path, "r") as file:
            cookies = json.load(file)
            
        for cookie in cookies:
            # Skip cookies that might cause issues
            if 'expiry' in cookie:
                # Selenium expects 'expiry' as an integer
                cookie['expiry'] = int(cookie['expiry'])
            
            try:
                # Chrome doesn't like the sameSite parameter
                if 'sameSite' in cookie:
                    del cookie['sameSite']
                    
                driver.add_cookie(cookie)
            except Exception as e:
                print(f"Warning: Could not add cookie {cookie.get('name')}: {e}")
        
        driver.refresh()
        time.sleep(3)
        
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, LOGGED_IN_INDICATOR))
            )
            return True
        except:
            return False
    except Exception as e:
        print(f"Error loading cookies: {e}")
        return False

def is_logged_in(driver):
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, LOGGED_IN_INDICATOR))
        )
        return True
    except:
        return False