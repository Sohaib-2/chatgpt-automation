import os
from getpass import getpass
from core.browser_setup import setup_browser, save_cookies, load_cookies, is_logged_in
from core.automation.auth_steps import login_to_chatgpt
from core.utils import save_to_env_file

def get_credentials_from_env():
    """Get credentials from environment variables if available."""
    email = os.getenv("CHATGPT_EMAIL")
    password = os.getenv("CHATGPT_PASSWORD")
    return email, password

def prompt_for_credentials(save_to_env=False):
    """Prompt user for credentials and optionally save to .env file."""
    email = input("Enter ChatGPT email: ")
    password = getpass("Enter ChatGPT password: ")
    
    if save_to_env:
        save_to_env_file({"CHATGPT_EMAIL": email, "CHATGPT_PASSWORD": password})
    
    return email, password

def get_initial_prompt():
    """Get the initial prompt either from .env or from user input."""
    use_env_prompt = os.path.exists(".env") and input("Use prompt from .env file? (y/n): ").lower() == 'y'
    
    if use_env_prompt:
        initial_prompt = os.getenv("CHATGPT_PROMPT")
        if not initial_prompt:
            print("Error: Prompt not found in .env file")
            initial_prompt = input("Enter initial prompt: ")
            save_env = input("Save prompt to .env file? (y/n): ").lower() == 'y'
            if save_env:
                save_to_env_file({"CHATGPT_PROMPT": initial_prompt})
    else:
        initial_prompt = input("Enter initial prompt: ")
        save_prompt = input("Save prompt to .env file for next time? (y/n): ").lower() == 'y'
        if save_prompt:
            save_to_env_file({"CHATGPT_PROMPT": initial_prompt})
    
    return initial_prompt

def get_followup_prompt():
    """Get the followup prompt either from .env or from user input."""
    use_env_followup = os.path.exists(".env") and input("Use followup from .env file? (y/n): ").lower() == 'y'
    
    if use_env_followup:
        followup_prompt = os.getenv("CHATGPT_FOLLOWUP")
        if not followup_prompt:
            print("Error: Followup prompt not found in .env file")
            followup_prompt = input("Enter followup prompt: ")
            save_env = input("Save followup to .env file? (y/n): ").lower() == 'y'
            if save_env:
                save_to_env_file({"CHATGPT_FOLLOWUP": followup_prompt})
    else:
        followup_prompt = input("Enter followup prompt: ")
        save_followup = input("Save followup to .env file for next time? (y/n): ").lower() == 'y'
        if save_followup:
            save_to_env_file({"CHATGPT_FOLLOWUP": followup_prompt})
    
    return followup_prompt

def get_output_path():
    """Get the output path for saving responses."""
    default_output_path = "data/outputs/responses.csv"
    output_path = os.getenv("OUTPUT_PATH") or default_output_path
    
    custom_output = input(f"Use custom output path? (default: {output_path}) (y/n): ").lower() == 'y'
    if custom_output:
        output_path = input("Enter output path: ")
        save_to_env_file({"OUTPUT_PATH": output_path})
    
    # Ensure output_path is never None
    if not output_path:
        output_path = default_output_path
        print(f"Using default output path: {output_path}")
    
    return output_path

def handle_browser_session():
    """Handle browser setup and login process."""
    print("\n=== Starting Browser ===\n")
    
    # Ask user if they want to run in headless mode
    headless = input("Run in headless mode (no browser window)? (y/n): ").lower() == 'y'
    
    driver = setup_browser(headless=headless)
    
    # Check for cookies file
    cookies_path = "data/cookies/chatgpt_cookies.json"
    if os.path.exists(cookies_path):
        use_cookies = input("Previous session found. Use it? (y/n): ").lower() == 'y'
        if use_cookies:
            print("Attempting to load saved session...")
            cookies_loaded = load_cookies(driver)
            
            # Even if there are warnings, check if we're actually logged in
            if cookies_loaded or is_logged_in(driver):
                print("Session loaded successfully.")
                return driver, True
            
            print("Failed to load session. Proceeding with fresh login...")
    else:
        print("No saved session found. Login required.")
    
    # Get credentials and login
    env_file_exists = os.path.exists(".env")
    email, password = None, None
    
    # Only ask about using env credentials if cookies failed or don't exist
    if env_file_exists:
        use_env = input("Use credentials from .env file? (y/n): ").lower() == 'y'
        if use_env:
            email, password = get_credentials_from_env()
            if not email or not password:
                print("Error: Credentials not found in .env file")
                email, password = prompt_for_credentials(save_to_env=True)
        else:
            email, password = prompt_for_credentials()
            save_env = input("Save credentials to .env file for next time? (y/n): ").lower() == 'y'
            if save_env:
                save_to_env_file({"CHATGPT_EMAIL": email, "CHATGPT_PASSWORD": password})
    else:
        email, password = prompt_for_credentials()
        save_env = input("Save credentials to .env file for next time? (y/n): ").lower() == 'y'
        if save_env:
            save_to_env_file({"CHATGPT_EMAIL": email, "CHATGPT_PASSWORD": password})
    
    # Perform login
    login_success = login_to_chatgpt(driver, email, password)
    if login_success:
        print("Login successful. Saving new session...")
        save_cookies(driver)
        return driver, True
    else:
        print("Login failed. Exiting.")
        driver.quit()
        return None, False

def preview_response(response, prefix="Response"):
    """Display a preview of the response."""
    words = response.split()
    preview = " ".join(words[:100]) + ("..." if len(words) > 100 else "")
    print(f"\n=== {prefix} Preview ===")
    print(preview)
    print("=" * (len(prefix) + 11) + "\n")