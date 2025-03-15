# Technical Details

## Architecture Overview

The ChatGPT Automation script follows a modular, layered architecture designed for reliability, maintainability, and extensibility:

```
chatgpt-automation/
├── core/                      # Core functionality
│   ├── __init__.py            # Package initialization
│   ├── automation/            # Web automation components
│   │   ├── auth_steps.py      # Authentication functions
│   │   ├── chat_steps.py      # Chat interaction functions
│   │   └── ui_flow.py         # User interaction flow
│   ├── browser_setup.py       # Browser initialization and session 
│   ├── locators.py            # UI element selectors
│   └── utils.py               # Utility functions
├── data/                      # Data storage (created at runtime)
│   ├── cookies/               # Browser cookies storage
│   └── outputs/               # Response output files
├── .env.example               # Environment variable template
├── .gitignore                 # Git ignore configuration
├── dev_script.ipynb           # Development notebook
├── main.py                    # Main application entry point
├── README.md                  # Project documentation
└── requirements.txt           # Dependencies
```

## Core Components

### 1. Browser Initialization and Session Management
- **File**: `core/browser_setup.py`
- **Key Functions**:
  - `setup_browser()`: Configures and initializes the web driver
  - `save_cookies()`: Persists authentication cookies
  - `load_cookies()`: Restores previous sessions
  - `is_logged_in()`: Verifies login status

### 2. Authentication Flow
- **File**: `core/automation/auth_steps.py`
- **Key Functions**:
  - `login_to_chatgpt()`: Handles the complete login sequence
  - Element location and interaction for each authentication step

### 3. Chat Interaction
- **File**: `core/automation/chat_steps.py`
- **Key Functions**:
  - `send_prompt_get_response()`: Submits a prompt and extracts the response
  - `send_followup_get_response()`: Handles follow-up interactions
  - `wait_for_response()`: Detects when ChatGPT has finished generating
  - `extract_last_response()`: Extracts the text of the generated response

### 4. User Interface Flow
- **File**: `core/automation/ui_flow.py`
- **Key Functions**:
  - `handle_browser_session()`: Manages browser setup and authentication
  - `get_initial_prompt()`: Obtains the initial prompt from user or config
  - `get_followup_prompt()`: Obtains the follow-up prompt
  - `get_output_path()`: Determines where to save results
  - `preview_response()`: Shows a snippet of the response to the user

### 5. Utilities
- **File**: `core/utils.py`
- **Key Functions**:
  - `save_to_csv()`: Stores response data in CSV format
  - `save_to_env_file()`: Updates environment variables
  - `create_directories()`: Ensures required directories exist

### 6. Element Locators
- **File**: `core/locators.py`
- Contains CSS selectors and XPaths for all UI elements

## Technical Approaches

### Anti-Detection Measures
- Human-like typing with random delays
- SeleniumBase's undetected ChromeDriver mode (used this to bypass cloudflare)
- Cookie-based session persistence

### Resilient Web Interaction
- Explicit waits with appropriate timeouts
- Multiple selector fallbacks when possible
- Comprehensive error handling

### Configuration Management
- Environment variable support via dotenv
- Interactive configuration with save options
- Configuration persistence between runs

### Data Storage
- Structured CSV output with timestamps
- Session cookies persistence
- Directory structure organization

## Dependencies

- **seleniumbase**: Enhanced web driver with undetected mode
- **dotenv**: Environment variable management
- **Standard libraries**: os, time, json, csv, datetime

## Performance Considerations

- **Timeouts**: Carefully calibrated for reliability
- **Session Persistence**: Reduces unnecessary logins
- **Error Recovery**: Graceful handling of unexpected conditions

