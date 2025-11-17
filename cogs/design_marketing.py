import logging
import discord
from discord.ext import commands

log = logging.getLogger(__name__)

DESIGN_MARKETING_CHANNELS = {
    "design-marketing-research",
    "design-marketing-general",
    "design-marketing-meetings",
    "robocollective-meetings",
}


class DesignMarketing(commands.Cog):
    """Design and Marketing team logic."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    def is_design_channel(self, channel: discord.abc.GuildChannel) -> bool:
        return isinstance(channel, discord.TextChannel) and channel.name in DESIGN_MARKETING_CHANNELS

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return
        if not self.is_design_channel(message.channel):
            return

        log.info(f"[DESIGN] {message.channel.name} | {message.author}: {message.content}")

        try:
            await message.add_reaction("🎨")
        except Exception as e:
            log.warning(f"Design reaction failed: {e}")

    @commands.command(name="design-status")
    async def status(self, ctx: commands.Context):
        """Check that the Design & Marketing cog is running."""
        if not self.is_design_channel(ctx.channel):
            return
        await ctx.send("Design & Marketing module is active.")


async def setup(bot: commands.Bot):
    await bot.add_cog(DesignMarketing(bot))
