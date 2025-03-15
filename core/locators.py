# ChatGPT Web UI Locators

# Login Page
LOGIN_BUTTON = "button[data-testid='login-button']"
EMAIL_INPUT = "input#email-input"
EMAIL_CONTINUE_BUTTON = "input.continue-btn"
PASSWORD_INPUT = "input#password"
PASSWORD_CONTINUE_BUTTON = "button[type='submit']"

# Chat Interface
CHAT_INPUT = "div[contenteditable='true'][data-virtualkeyboard='true']" 
SEND_BUTTON = "button[data-testid='send-button']"
STOP_GENERATING_BUTTON = "button[aria-label='Stop generating']"
RESPONSE_TEXT = "div.markdown.prose"

# Login Status
LOGGED_IN_INDICATOR = "//button[@aria-label='Close sidebar']"
