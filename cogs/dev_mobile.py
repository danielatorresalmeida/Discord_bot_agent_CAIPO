import logging
import discord
from discord.ext import commands

log = logging.getLogger(__name__)

DEV_MOBILE_CHANNELS = {
    "ai-travel-dev-research",
    "ai-travel-dev-help",
    "ai-travel-dev-meetings",
    "ai-travel-dev-general",
    "caipo-dev-meetings",
    "caipo-dev-general",
    "mobile-app-general",
    "mobile-app-meetings",
}


class DevMobile(commands.Cog):
    """Dev and Mobile team channels."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    def is_dev_mobile_channel(self, channel: discord.abc.GuildChannel) -> bool:
        return isinstance(channel, discord.TextChannel) and channel.name in DEV_MOBILE_CHANNELS

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return
        if not self.is_dev_mobile_channel(message.channel):
            return

        log.info(f"[DEV MOBILE] {message.channel.name} | {message.author}: {message.content}")

        try:
            await message.add_reaction("📱")
        except Exception as e:
            log.warning(f"DevMobile reaction failed: {e}")

    @commands.command(name="dev-status")
    async def status(self, ctx: commands.Context):
        """Check that the Dev & Mobile cog is running."""
        if not self.is_dev_mobile_channel(ctx.channel):
            return
        await ctx.send("Dev & Mobile module is active.")


async def setup(bot: commands.Bot):
    await bot.add_cog(DevMobile(bot))
