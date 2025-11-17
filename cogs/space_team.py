import logging
import discord
from discord.ext import commands

log = logging.getLogger(__name__)

SPACE_CHANNELS = {
    "space-research",
    "space-general",
    "space-meetings",
}


class SpaceTeam(commands.Cog):
    """Space Science team logic."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    def is_space_channel(self, channel: discord.abc.GuildChannel) -> bool:
        return isinstance(channel, discord.TextChannel) and channel.name in SPACE_CHANNELS

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return
        if not self.is_space_channel(message.channel):
            return

        log.info(f"[SPACE] {message.channel.name} | {message.author}: {message.content}")

        try:
            await message.add_reaction("🛰️")
        except Exception as e:
            log.warning(f"Space reaction failed: {e}")

    @commands.command(name="space-status")
    async def status(self, ctx: commands.Context):
        """Check that the Space Science cog is running."""
        if not self.is_space_channel(ctx.channel):
            return
        await ctx.send("Space Science module is active.")


async def setup(bot: commands.Bot):
    await bot.add_cog(SpaceTeam(bot))
