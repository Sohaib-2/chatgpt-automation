import os
import dotenv
from core.automation.chat_steps import send_prompt_get_response, send_followup_get_response
from core.utils import save_to_csv, create_directories
from core.automation.ui_flow import (
    handle_browser_session,
    get_initial_prompt,
    get_followup_prompt,
    get_output_path,
    preview_response
)

def main():
    # Create necessary directories
    create_directories()
    
    # Load .env file if it exists
    if os.path.exists(".env"):
        dotenv.load_dotenv()
    
    print("\n=== ChatGPT Automation ===\n")
    
    # Setup browser and handle login
    driver, login_success = handle_browser_session()
    if not login_success or not driver:
        return
    
    # Get initial prompt
    initial_prompt = get_initial_prompt()
    
    # Send initial prompt and get response
    print(f"\nSending initial prompt: {initial_prompt[:50]}...")
    initial_response = send_prompt_get_response(driver, initial_prompt)
    print("Response received.")
    
    # Print preview of initial response
    preview_response(initial_response, "Initial Response")
    
    # Now get followup prompt after seeing the response
    followup_prompt = get_followup_prompt()
    
    # Send followup prompt and get response
    print(f"\nSending followup prompt: {followup_prompt[:50]}...")
    followup_response = send_followup_get_response(driver, followup_prompt)
    print("Response received.")
    
    # Print preview of followup response
    preview_response(followup_response, "Followup Response")
    
    # Get output path
    output_path = get_output_path()
    
    # Save responses to CSV
    data = [
        {"prompt": initial_prompt, "response": initial_response, "type": "initial"},
        {"prompt": followup_prompt, "response": followup_response, "type": "followup"}
    ]
    
    save_to_csv(data, output_path)
    print(f"\nResponses saved to {output_path}")
    
    # Close the browser
    print("\nClosing browser...")
    driver.quit()
    print("Done.")

if __name__ == "__main__":
    main()