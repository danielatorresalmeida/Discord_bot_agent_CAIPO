import logging
import discord
from discord.ext import commands

log = logging.getLogger(__name__)


class Alerts(commands.Cog):
    """Global simple reactions and keyword replies."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return

        # Global ✅ reaction
        try:
            await message.add_reaction("✅")
        except Exception as e:
            log.warning(f"Reaction failed: {e}")

        content = (message.content or "").lower()
        if "hello bot" in content:
            await message.channel.send("Hey, how can I help?")


async def setup(bot: commands.Bot):
    await bot.add_cog(Alerts(bot))
