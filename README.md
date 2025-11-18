Discord Bot Agent – CAIPO

A modular, extensible Discord automation bot built for Flo Labs R&D teams.
This bot manages team channels, processes automations, receives webhook data, and integrates with tools like Read.ai, Toggl, Zoom, and Notion.

It runs 24/7 on Render (Free Tier) using a built-in health-check web server.

🚀 Features
Core Bot Functions

Reacts to all user messages with a ✅

Responds to certain triggers (e.g., “hello bot”)

Modular architecture using cogs/

Supports role-based and channel-based automated actions

Designed to expand with additional team-specific behavior

Integrations

Read.ai Meeting Webhook → Automatically posts meeting summaries to the correct *-meetings channel

Notion API → Fetch time entries, pages, or changes for internal automations

Toggl API → For time tracking automations (client library included)

Zoom Webhooks → Ready to receive meeting events (client library included)

Dev-friendly architecture

Clean cogs/ folder for team modules

services/ folder for external API clients

Uses environment variables for all secrets

Runs Discord bot + Web server concurrently

📂 Project Structure
discord-bot-agent-CAIPO/
│
├── bot.py                      # Main bot runner + aiohttp web server
│
├── cogs/                       # Modular bot logic (team-specific)
│   ├── __init__.py
│   ├── ai_robotics.py
│   ├── alerts.py
│   ├── all_teams_general.py
│   ├── automation_team.py
│   ├── design_marketing.py
│   ├── dev_mobile.py
│   ├── go_to_market.py
│   ├── moodchanger.py
│   ├── pm_team.py
│   ├── podcasts.py
│   └── space_team.py
│
├── services/                   # API clients for external tools
│   ├── readai_client.py
│   ├── toggl_client.py
│   └── zoom_client.py
│
├── requirements.txt
├── runtime.txt
├── .gitignore
├── .gitattributes
└── README.md

🔧 Installation & Running Locally
1. Create virtual environment
python -m venv .venv
source .venv/bin/activate      # macOS/Linux
.\.venv\Scripts\activate       # Windows

2. Install dependencies
pip install -r requirements.txt

3. Configure environment variables

Create a .env file or set system env variables:

Discord
DISCORD_BOT_TOKEN=your_bot_token

Notion
NOTION_API_TOKEN=your_notion_token
NOTION_DATABASE_ID_TIME_ENTRIES=xxxxxxxxxxxxxxxx

Read.ai Webhook Secrets (if required)
REDAI_WEBHOOK_SECRET=optional

Toggl
TOGGL_API_TOKEN=xxxxxx

Zoom
ZOOM_WEBHOOK_SECRET=xxxxxx

4. Run the bot
python bot.py

☁️ Deploying on Render (Free Tier)

This bot is optimized for Render Free Plan:

Build Command
pip install -r requirements.txt

Start Command
python bot.py

Environment Variables

Add (minimum):

DISCORD_BOT_TOKEN=xxxxx
PORT=10000

Keep the bot awake

Render sleeps free instances unless they receive HTTP traffic.

Use UptimeRobot:

Setting	Value
Type	HTTP(s) Monitor
URL	https://<your-render-url>/health
Interval	Every 5 minutes

This pings the built-in aiohttp server to prevent sleeping.

🧠 How the Web Server Works

The bot spins up a small aiohttp server:

app.router.add_get("/health", handle_health)
app.router.add_post("/readai-webhook", readai_webhook)


This enables:

Render uptime protection

Accepting Read.ai meeting data

Future support for Zoom or Notion webhooks

🧩 Cogs (Modular Bot Logic)

Every cog file in cogs/ can contain:

Message listeners

Commands

Team-specific automation

Example cog entry point:

async def setup(bot):
    await bot.add_cog(MyTeamCog(bot))


You load new cogs by adding them to bot.py:

extensions = [
    "cogs.alerts",
    "cogs.all_teams_general",
    "cogs.ai_robotics",
    ...
]

🔗 External Services
Read.ai

Webhook URL handled by:

/readai-webhook


Bot posts recaps automatically to the right team’s *-meetings channel.

Notion

Used for:

Time entry processing

Task monitoring

Future automation pipelines

Toggl

Automations for:

Time entries

Debugging Toggl → Discord sync issues

Zoom

Webhook-ready to log or process meeting events.

🧪 Testing the Bot
Basic Functionality

Bot appears online

Reacts to every message with a checkmark

Replies to “hello bot”

/health returns “OK”

Webhook & Automation Tests

Trigger Read.ai test webhook → verify message arrives in the correct channel

Run Notion command:

!notion_updates 1


Trigger Toggl updates

📝 License

Open-source. You may reuse or modify as needed.