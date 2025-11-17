Discord_bot_agent_CAIPO

A lightweight Discord bot that automatically reacts to messages and responds to simple triggers.
Built using discord.py, designed to run 24/7 on Render Free Web Services (with a health-check endpoint to prevent sleeping).

🚀 Features

Adds a ✅ reaction to every user message

Responds to the phrase “hello bot”

Includes a built-in aiohttp web server for Render uptime pings

Runs both the bot and the web endpoint in parallel

Fully environment-variable based token handling

Clean, minimal codebase

📂 Project Structure
discord-bot-agent-CAIPO/
│
├── bot.py               # Main bot + web server
├── requirements.txt     # Python dependencies
├── runtime.txt          # Python version for Render
├── .gitignore
├── .gitattributes
└── README.md

🔧 Installation & Running Locally
1. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate        # macOS/Linux
.\.venv\Scripts\activate         # Windows

2. Install dependencies
pip install -r requirements.txt

3. Set your bot token

Create an environment variable:

Windows (PowerShell):

setx DISCORD_BOT_TOKEN "YOUR_TOKEN_HERE"


macOS/Linux:

export DISCORD_BOT_TOKEN="YOUR_TOKEN_HERE"

4. Run the bot
python bot.py

☁️ Deploying on Render (Free Tier)

This bot is designed to run on a Render Web Service, even on the free plan.

1. Create a new Web Service

Build command:

pip install -r requirements.txt


Start command:

python bot.py


Root directory: .

Environment variable:

DISCORD_BOT_TOKEN = your_bot_token_here

2. Keep Render Awake (Required on Free Tier)

Render free services sleep without incoming HTTP traffic.

This bot includes a /health endpoint, so you can keep it awake using:

UptimeRobot

Create a “HTTP(s) Monitor”

URL:

https://dashboard.uptimerobot.com/monitors/801805781


Interval: Every 5 minutes

This keeps your bot running 24/7.

🧠 How the Keep-Alive Web Server Works

Inside bot.py, an aiohttp server runs alongside the Discord bot:

async def handle_health(request):
    return web.Response(text="OK")


Render detects incoming traffic to /health, so your free instance is never marked as idle.

🔐 Environment Variables
Variable	Description
DISCORD_BOT_TOKEN	Your Discord bot secret token

⚠️ Never commit your token or put it in your code.

🧪 Testing

After deployment:

Check your bot appears online in Discord

Send any message → bot should react with ✅

Send "hello bot" → bot replies "Hey!"

Visit your /health URL → should show:

OK

🛠️ Built With

Python 3.x

discord.py

aiohttp

Render Web Services

📝 License

This project is open-source. You may reuse, modify, and adapt it freely.