# ChatGPT Automation

An automation task for automating interactions with ChatGPT, including authentication, prompt submission, response extraction, and data storage.

For detailed documentation on the implementation approach and technical architecture, please refer to:
- [Implementation_Approach.md](Implementation_Approach.md) - Details on development process and code origin
- [Technical_Details.md](Technical_Details.md) - In-depth technical documentation
## Features

- **Automated Login**: log in to ChatGPT with credentials
- **Prompt Management**: Submit initial prompts and follow-up messages
- **Response Extraction**: Reliably extract and format ChatGPT's responses
- **Session Persistence**: Save and reuse sessions to minimize login frequency
- **Data Storage**: Save all interactions(chats) to CSV file as requested
- **Configuration Management**: configuration via environment variables or interactive prompts

## Setup and Installation

### Prerequisites

- Python 3.9+ 

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/sohaib-2/chatgpt-automation.git
   cd chatgpt-automation
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # On Windows
   .venv\Scripts\activate
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. (Optional) Create a `.env` file based on the template:
   ```bash
   cp .env.example .env
   # Edit .env with your preferred settings
   ```

## Usage

### Running the Script

Execute the main script to start the automation:

```bash
python main.py
```

### Configuration Options

You can configure the tool in two ways:

1. **Interactive Mode**: The script will prompt you for necessary information:
   - ChatGPT login credentials
   - Initial prompt
   - Follow-up prompt
   - Output file path

2. **Environment Variables**: Set up a `.env` file with the following variables:
   ```
   CHATGPT_EMAIL=your_email@example.com
   CHATGPT_PASSWORD=your_password
   CHATGPT_PROMPT=Your initial prompt text
   CHATGPT_FOLLOWUP=Your follow-up prompt text
   OUTPUT_PATH=data/outputs/your_filename.csv
   ```

### Output Format

The script generates a CSV file with the following columns:
- `timestamp`: Date and time of the interaction
- `type`: Either "initial" or "followup"
- `prompt`: The text sent to ChatGPT
- `response`: ChatGPT's complete response

## Project Structure

- `main.py`: Main entry point script
- `core/`: Core functionality modules
  - `automation/`: Web automation components
  - `browser_setup.py`: Browser initialization
  - `locators.py`: UI element selectors
  - `utils.py`: Utility functions
- `data/`: Generated data storage
- `dev_script.ipynb`: Development notebook with step-by-step exploration


## Development Notes

The task was done using a systematic approach:
1. Initial exploration and prototyping in a Jupyter notebook
2. Extraction of core functionality into modular components
3. Building a clean architecture with separation of concerns
4. Implementation of error handling and configuration management
