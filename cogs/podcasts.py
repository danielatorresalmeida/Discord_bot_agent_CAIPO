import logging
import discord
from discord.ext import commands

log = logging.getLogger(__name__)

PODCAST_CHANNELS = {
    "podcasts-meetings",
    "podcasts-general",
}


class Podcasts(commands.Cog):
    """Podcast Production team logic."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    def is_podcast_channel(self, channel: discord.abc.GuildChannel) -> bool:
        return isinstance(channel, discord.TextChannel) and channel.name in PODCAST_CHANNELS

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return
        if not self.is_podcast_channel(message.channel):
            return

        log.info(f"[PODCASTS] {message.channel.name} | {message.author}: {message.content}")

        try:
            await message.add_reaction("🎙️")
        except Exception as e:
            log.warning(f"Podcast reaction failed: {e}")

    @commands.command(name="podcast-status")
    async def status(self, ctx: commands.Context):
        """Check that the Podcasts cog is running."""
        if not self.is_podcast_channel(ctx.channel):
            return
        await ctx.send("Podcast Production module is active.")


async def setup(bot: commands.Bot):
    await bot.add_cog(Podcasts(bot))
