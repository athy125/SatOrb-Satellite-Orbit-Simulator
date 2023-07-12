import os
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow

CLIENT_SECRETS_FILE = "client_secrets.json"
SCOPES = ["openid", "email", "profile"]

def authenticate_with_google():
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_local_server()

    save_credentials(credentials)
    return credentials

def save_credentials(credentials):
    credentials_file = "credentials.json"
    credentials.refresh(Request())
    with open(credentials_file, "w") as f:
        f.write(credentials.to_json())

def load_credentials():
    credentials_file = "credentials.json"
    if os.path.exists(credentials_file):
        with open(credentials_file, "r") as f:
            return Credentials.from_authorized_user_info(f.read())

    return None

def validate_credentials(credentials):
    if credentials and credentials.expired and credentials.refresh_token:
        credentials.refresh(Request())

    return credentials
