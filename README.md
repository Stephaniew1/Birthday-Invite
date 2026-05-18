# Birthday Invite

An interactive web-based invitation app built for a surprise birthday party. 
Guests open the link, get a "Save the Date" notification, tap through a 
chatbot-style RSVP flow, and automatically receive an email with a calendar 
invite attached.

Built before Apple launched Apple Invites on iOS.

## How it works

- Guests visit the deployed link and see a lock-screen-style "Save the Date" 
  overlay
- Tapping through opens an animated chat-style invitation flow
- RSVP responses are captured and stored in SQLite
- On RSVP, the app uses the Gmail API to send a confirmation email with an 
  .ics calendar attachment
- Works for both iPhone (Apple Calendar) and Android (Google Calendar) users
- All without the birthday person ever knowing

## Tech stack

Python, Flask, SQLite, Gmail API, Google OAuth 2.0, Bootstrap, HTML, CSS, JS. 
Deployed on Heroku via Procfile.

## Why I built this

I needed to invite all my mum's friends to her surprise birthday party from 
11,000 km away, without her finding out. Group chats were too risky. A 
shared doc was too risky. So I built a single link the family could send out 
that handled invites, RSVPs, calendar adds, and reminders, end to end.

The party went well.

## Run locally

`pip install -r requirements.txt`, set up Gmail API credentials, then 
`python app.py`.
