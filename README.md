# Football Chatbot

A simple Streamlit-based football chatbot that uses the Groq Chat API to respond to user questions about football.

## Project Files

- `app.py` - Main Streamlit application.
- `requirements.txt` - Python dependencies.
- `.env` - Environment file for storing API keys.
- `.gitignore` - Files and folders excluded from Git.

## Prerequisites

- Python 3.9+
- `pip` package manager

## Setup

1. Clone the repository or copy the project files.
2. Create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment:

- Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

- Windows Command Prompt:

```cmd
venv\Scripts\activate.bat
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Create a `.env` file in the project root with:

```env
GROQ_API_KEY=your_api_key_here
```

## Run

Start the Streamlit app:

```bash
streamlit run app.py
```

Then open the local URL displayed in the terminal.

## Notes

- Keep your `GROQ_API_KEY` secret.
- The app sends chat history to the Groq API and displays the response in a chat-style layout.
