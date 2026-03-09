import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

creds = Credentials.from_service_account_file(
    "google_credentials.json",
    scopes=SCOPES
)

client = gspread.authorize(creds)

sheet = client.open("LLM_Symbolic_Evaluation").worksheet("Test Runs")

sheet.append_row([
    "TEST_CONNECTION",
    datetime.now().isoformat(),
    "Odin",
    "gpt-test",
    0.5,
    "prompt_test",
    "response_test",
    10,
    "none",
    "connection successful"
])

print("Row successfully written to Google Sheets.")
