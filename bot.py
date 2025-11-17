import os
import logging
import asyncio

import discord
from aiohttp import web

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.messages = True


class AutoReact(discord.Client):
    async def on_ready(self):
        logging.info(f"Logged in as {self.user} (id={self.user.id})")

    async def on_message(self, message: discord.Message):
        # Ignore bot messages, including ourselves
        if message.author.bot or message.author.id == self.user.id:
            return

        # Always try to react with ✅
        try:
            await message.add_reaction("✅")
        except discord.HTTPException as e:
            logging.warning(f"Reaction failed: {e}")

        # Simple keyword reply
        content = (message.content or "").lower()
        if "hello bot" in content:
            await message.channel.send("Hey!")


# -------- Web server (for Render free web service) -------- #

async def handle_health(request):
    return web.Response(text="OK")

async def start_web_server():
    app = web.Application()
    app.router.add_get("/", handle_health)
    app.router.add_get("/health", handle_health)

    port = int(os.environ.get("PORT", "10000"))  # Render provides PORT
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()

    logging.info(f"Web server started on 0.0.0.0:{port}")

    # Keep the web server task alive
    while True:
        await asyncio.sleep(3600)


async def main():
    # Read token from environment variable set on Render
    token = os.getenv("DISCORD_BOT_TOKEN")
    if not token:
        raise SystemExit("DMTQyNTI0MDc3NDUyMTY1MTMzMQ.G6dxLZ.OJS7J-LFHyZ71yGKVJYlH3B3plULGukgMWf5W4")

    client = AutoReact(intents=intents)

    # Run bot and web server in parallel
    await asyncio.gather(
        client.start(token),
        start_web_server(),
    )


if __name__ == "__main__":
    asyncio.run(main())

if __name__ == "__main__":
    TOKEN = os.getenv("MMTQyNTI0MDc3NDUyMTY1mtmZmQ.G6dxLZ.OJS7J-LFHyZ7tyGKVJYlH3B3plULGukMWf5W4")
    if not TOKEN:
        raise SystemExit("Error: DISCORD_BOT_TOKEN is missing")

    client = AutoReact(intents=intents)
    client.run(TOKEN)
