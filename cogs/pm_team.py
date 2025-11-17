import logging
import discord
from discord.ext import commands

log = logging.getLogger(__name__)

PM_CHANNELS = {
    "pm-general",
    "pm-meetings",
}


class PMTeam(commands.Cog):
    """Project Management team logic."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    def is_pm_channel(self, channel: discord.abc.GuildChannel) -> bool:
        return isinstance(channel, discord.TextChannel) and channel.name in PM_CHANNELS

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return
        if not self.is_pm_channel(message.channel):
            return

        log.info(f"[PM] {message.channel.name} | {message.author}: {message.content}")

        try:
            await message.add_reaction("📋")
        except Exception as e:
            log.warning(f"PM reaction failed: {e}")

    @commands.command(name="pm-status")
    async def status(self, ctx: commands.Context):
        """Check that the PM cog is running."""
        if not self.is_pm_channel(ctx.channel):
            return
        await ctx.send("PM Team module is active.")


async def setup(bot: commands.Bot):
    await bot.add_cog(PMTeam(bot))
