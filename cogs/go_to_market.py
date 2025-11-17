import logging
import discord
from discord.ext import commands

log = logging.getLogger(__name__)

GTM_CHANNELS = {
    "go-to-market-research",
    "go-to-market-meetings",
    "go-to-market-general",
}


class GoToMarket(commands.Cog):
    """Go To Market team logic."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    def is_gtm_channel(self, channel: discord.abc.GuildChannel) -> bool:
        return isinstance(channel, discord.TextChannel) and channel.name in GTM_CHANNELS

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return
        if not self.is_gtm_channel(message.channel):
            return

        log.info(f"[GTM] {message.channel.name} | {message.author}: {message.content}")

        try:
            await message.add_reaction("📈")
        except Exception as e:
            log.warning(f"GTM reaction failed: {e}")

    @commands.command(name="gtm-status")
    async def status(self, ctx: commands.Context):
        """Check that the Go To Market cog is running."""
        if not self.is_gtm_channel(ctx.channel):
            return
        await ctx.send("Go To Market module is active.")


async def setup(bot: commands.Bot):
    await bot.add_cog(GoToMarket(bot))
