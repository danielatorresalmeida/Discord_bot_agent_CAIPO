import os
import logging
import discord

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.messages = True

class AutoReact(discord.Client):
    async def on_ready(self):
        logging.info(f"Logged in as {self.user} (id={self.user.id})")

    async def on_message(self, message: discord.Message):
        if message.author.bot or message.author.id == self.user.id:
            return
        try:
            await message.add_reaction("✅")
        except discord.HTTPException as e:
            logging.warning(f"Reaction failed: {e}")

        if "hello bot" in (message.content or "").lower():
            await message.channel.send("Hey!")

if __name__ == "__main__":
    # Read token from environment variable set on Render
    TOKEN = os.getenv("DISCORD_BOT_TOKEN")
    if not TOKEN:
        raise SystemExit("DMTQyNTI0MDc3NDUyMTY1MTMzMQ.Gt_LrF.fvxnVHzBcBJ28xsZjZEQtGcPjkYS7QIlZhbfgo")
    AutoReact(intents=intents).run(TOKEN)