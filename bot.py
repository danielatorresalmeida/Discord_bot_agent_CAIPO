import os
import logging
import asyncio

import discord
from discord.ext import commands
from aiohttp import web

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")

# INTENTS
intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.message_content = True

# Bot instance
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    logging.info(f"Logged in as {bot.user} (id={bot.user.id})")
    logging.info("Loaded cogs: %s", list(bot.cogs.keys()))

async def main():
    token = os.getenv("DISCORD_BOT_TOKEN")
    if not token:
        raise SystemExit("Error: DISCORD_BOT_TOKEN is missing")

    # Load all cogs
    await load_cogs()

    # Run both services
    await asyncio.gather(
        bot.start(token),
        start_web_server(),
    )

# -------------------- LOAD COGS -------------------- #

async def load_cogs():
    """Load modular cogs."""
    extensions = [
        "cogs.alerts",
        "cogs.all_teams_general",
        "cogs.ai_robotics",
        "cogs.automation_team",
        "cogs.design_marketing",
        "cogs.dev_mobile",
        "cogs.go_to_market",
        "cogs.moodchanger",
        "cogs.podcasts",
        "cogs.pm_team",
        "cogs.space_team",
    ]

    for ext in extensions:
        try:
            await bot.load_extension(ext)
            logging.info(f"Loaded {ext}")
        except Exception as e:
            logging.error(f"Failed to load {ext}: {e}")

# -------------------- RENDER WEB SERVER -------------------- #

async def handle_health(request):
    return web.Response(text="OK")

async def start_web_server():
    app = web.Application()
    app.router.add_get("/", handle_health)
    app.router.add_get("/health", handle_health)

    port = int(os.getenv("PORT", "10000"))
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()

    logging.info(f"Web server running on port {port}")

    while True:
        await asyncio.sleep(3600)


# -------------------- MAIN ENTRY -------------------- #

async def main():
    token = os.getenv("MTQyNTI0MDc3NDUyMTY1mtmZmQ.G6dxLZ.OJS7J-LFHyZ7tyGKVJYlH3B3plULGukMWf5W4")
    if not TOKEN: raise SystemExit("Error: DISCORD_BOT_TOKEN is missing")

    await load_cogs()

    await asyncio.gather(
        bot.start(token),
        start_web_server(),
    )


if __name__ == "__main__":
    asyncio.run(main())
