import logging
import discord
from discord.ext import commands

log = logging.getLogger(__name__)

MOODCHANGER_CHANNELS = {
    "neuroscience-research",
    "neuroscience-general",
    "moodchanger-research",
    "moodchanger-meetings",
    "moodchanger-general",
}


class MoodChanger(commands.Cog):
    """MoodChanger and Neuroscience team logic."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    def is_mood_channel(self, channel: discord.abc.GuildChannel) -> bool:
        return isinstance(channel, discord.TextChannel) and channel.name in MOODCHANGER_CHANNELS

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return
        if not self.is_mood_channel(message.channel):
            return

        log.info(f"[MOODCHANGER] {message.channel.name} | {message.author}: {message.content}")

        try:
            await message.add_reaction("🧠")
        except Exception as e:
            log.warning(f"MoodChanger reaction failed: {e}")

    @commands.command(name="mood-status")
    async def status(self, ctx: commands.Context):
        """Check that the MoodChanger cog is running."""
        if not self.is_mood_channel(ctx.channel):
            return
        await ctx.send("MoodChanger module is active.")


async def setup(bot: commands.Bot):
    await bot.add_cog(MoodChanger(bot))
