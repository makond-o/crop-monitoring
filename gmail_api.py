from __future__ import print_function

import os.path
import pickle
import base64
import email
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def getEmails():
    # Variable creds will store the user access token.
    # If no valid token found, we will create one.
    creds = None

    # The file token.pickle contains the user access token.
    # Check if it exists
    if os.path.exists('token.pickle'):

        # Read the token from the file and store it in the variable creds
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    # If credentials are not available or are invalid, ask the user to log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the access token in token.pickle file for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    # Connect to the Gmail API
    service = build('gmail', 'v1', credentials=creds)

    # request a list of all the messages
    result = service.users().messages().list(userId='me', q="is:unread").execute()

    # We can also pass maxResults to get any number of emails. Like this:
    # result = service.users().messages().list(maxResults=200, userId='me').execute()
    messages = result.get('messages')

    # messages is a list of dictionaries where each dictionary contains a message id.
    email_content = ''
    # iterate through all the messages
    if email_content == '':
        for msg in messages:
            # Get the message from its id
            txt = service.users().messages().get(userId='me', id=msg['id']).execute()

            # Use try-except to avoid any Errors
            try:
                # Get value of 'payload' from dictionary 'txt'
                payload = txt['payload']
                headers = payload['headers']
                for d in headers:
                    # можно проверить дату и возможно есть способ отметить как прочитанное
                    if d['name'] == 'From':
                        if 'Crop Monitoring' in d['value']:
                            parts = payload.get('parts')[0]
                            data = parts['body']['data']
                            data = data.replace("-", "+").replace("_", "/")
                            email_content = base64.b64decode(data).decode()
                        break
            except:
                print('error')

    email_list = list(email_content)
    n = ''
    for char in email_list:
        if len(n) == 5:
            break
        if '0' <= char <= '9':
            n += char
        elif char == '-':
            if n != '':
                n += char
            else:
                n = ''
        else:
            n = ''

    print(n)





if __name__ == '__main__':
    getEmails()