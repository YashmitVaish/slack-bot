# Django Slack Bot (local dev)

A minimal Django + Bolt (Slack) bot scaffold for local development.

## Quick setup

1. Create a Slack app in your workspace. Add these at minimum under **OAuth & Permissions**:
   - `chat:write`
   - `app_mentions:read`
   - `commands`

   Also copy:
   - **Bot Token** (`xoxb-...`)
   - **Signing Secret**

   Optionally enable **Socket Mode** and create an **App-Level Token** (`xapp-...`) with `connections:write` if you prefer Socket Mode.

2. Copy `.env.example` to `.env` and set values.

3. Install dependencies and run locally:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
