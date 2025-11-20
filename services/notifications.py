import os
import discord

PERSONAL_LOG_CHANNEL_ID = int(os.getenv("DISCORD_PERSONAL_LOG_CHANNEL_ID", "0") or "0")

async def notify_personal(bot: discord.Client, content: str):
    if not PERSONAL_LOG_CHANNEL_ID:
        return

    channel = bot.get_channel(PERSONAL_LOG_CHANNEL_ID)
    if channel is None:
        channel = await bot.fetch_channel(PERSONAL_LOG_CHANNEL_ID)

    await channel.send(content)
