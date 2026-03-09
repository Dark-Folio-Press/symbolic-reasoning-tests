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

def log_test_run(run_id, myth, model, temp, prompt_id, response_id, score, failure, notes):

    sheet.append_row([
        run_id,
        datetime.now().isoformat(),
        myth,
        model,
        temp,
        prompt_id,
        response_id,
        score,
        failure,
        notes
    ])
