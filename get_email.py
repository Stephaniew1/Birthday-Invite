import os
import google_auth_oauthlib.flow
import google.auth.transport.requests
from google.oauth2.credentials import Credentials

# Scope: "gmail.send" means we only need to send
# .
SCOPES = ["https://www.googleapis.com/auth/gmail.send"]


def main():
    creds = None

    # If we already have token.json, try to load it
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    # If no valid creds or token is invalid/expired:
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            # Refresh
            creds.refresh(google.auth.transport.requests.Request())
        else:
            # Do an interactive OAuth flow in your browser
            flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)

        # Save the tokens for future runs
        with open("token.json", "w") as token_file:
            token_file.write(creds.to_json())

    print("OAuth flow complete. token.json has been created/updated.")


if __name__ == "__main__":
    main()
