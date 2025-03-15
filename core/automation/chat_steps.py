import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from core.locators import (
    CHAT_INPUT,
    SEND_BUTTON,
    STOP_GENERATING_BUTTON,
    RESPONSE_TEXT
)

def send_prompt_get_response(driver, prompt):
    try:
        # Find and click on the input area
        input_area = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, CHAT_INPUT))
        )
        input_area.click()
        
        # Type the prompt
        for char in prompt:
            ActionChains(driver).send_keys(char).perform()
            time.sleep(0.05)
        
        # Send the prompt
        send_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, SEND_BUTTON))
        )
        send_button.click()
        
        # Wait for response
        wait_for_response(driver)
        
        # Extract the response
        return extract_last_response(driver)
    except Exception as e:
        print(f"Error sending prompt: {e}")
        return None

def send_followup_get_response(driver, prompt):
    return send_prompt_get_response(driver, prompt)

def wait_for_response(driver):
    try:
        # Wait for stop generating button to appear
        try:
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, STOP_GENERATING_BUTTON))
            )
        except:
            pass
        
        # Wait for it to disappear
        try:
            WebDriverWait(driver, 60).until_not(
                EC.presence_of_element_located((By.CSS_SELECTOR, STOP_GENERATING_BUTTON))
            )
        except:
            pass
        
        # Additional wait to ensure response is loaded
        time.sleep(2)
    except Exception as e:
        print(f"Error waiting for response: {e}")

def extract_last_response(driver):
    try:
        # Find all response elements
        response_elements = driver.find_elements(By.CSS_SELECTOR, RESPONSE_TEXT)
        
        if not response_elements:
            return None
        
        # Get the last response element
        last_response = response_elements[-1]
        return last_response.text
    except Exception as e:
        print(f"Error extracting response: {e}")
        return None