import os
import logging
import asyncio

import discord
from aiohttp import web
from datetime import datetime, timedelta


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

        content = (message.content or "").strip()

        # ---------- CLEANUP COMMAND ----------
        # Usage.  !cleanup @user 7
        # meaning. delete messages from @user in this channel from the last 7 days
        if content.startswith("!cleanup"):
            # Only allow people with Manage Messages permission
            perms = message.channel.permissions_for(message.author)
            if not perms.manage_messages:
                await message.channel.send(
                    "You need the 'Manage Messages' permission to use this command."
                )
                return

            parts = content.split()
            if len(parts) < 3 or not message.mentions:
                await message.channel.send(
                    "Usage. `!cleanup @user <days>` for example. `!cleanup @TogglBot 7`"
                )
                return

            target_user = message.mentions[0]
            try:
                days = int(parts[-1])
            except ValueError:
                await message.channel.send("Days must be a number, for example `7`.")
                return

            after = datetime.utcnow() - timedelta(days=days)
            deleted = 0

            async for msg in message.channel.history(limit=None, after=after):
                if msg.author.id == target_user.id:
                    try:
                        await msg.delete()
                        deleted += 1
                    except discord.HTTPException as e:
                        logging.warning(f"Failed to delete message. {e}")

            await message.channel.send(
                f"Deleted {deleted} messages from {target_user.mention} "
                f"in the last {days} days."
            )
            return  # do not also add reaction to the command itself

        # ---------- NORMAL BEHAVIOUR ----------
        # Always try to react with ✅
        try:
            await message.add_reaction("✅")
        except discord.HTTPException as e:
            logging.warning(f"Reaction failed. {e}")

        # Simple keyword reply
        if "hello bot" in content.lower():
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
        raise SystemExit("Error: DISCORD_BOT_TOKEN is missing")

    client = AutoReact(intents=intents)

    # Run bot and web server in parallel
    await asyncio.gather(
        client.start(token),
        start_web_server(),
    )


if __name__ == "__main__":
    asyncio.run(main())
