import logging
import discord
from discord.ext import commands

log = logging.getLogger(__name__)

AUTOMATION_CHANNELS = {
    "automation-research",
    "automation-meetings",
    "automation-general",
}


class AutomationTeam(commands.Cog):
    """Automation team channels."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    def is_automation_channel(self, channel: discord.abc.GuildChannel) -> bool:
        return isinstance(channel, discord.TextChannel) and channel.name in AUTOMATION_CHANNELS

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return
        if not self.is_automation_channel(message.channel):
            return

        log.info(f"[AUTOMATION] {message.channel.name} | {message.author}: {message.content}")

        try:
            await message.add_reaction("⚙️")
        except Exception as e:
            log.warning(f"Automation reaction failed: {e}")

    @commands.command(name="automation-status")
    async def status(self, ctx: commands.Context):
        """Check that the Automation cog is running."""
        if not self.is_automation_channel(ctx.channel):
            return
        await ctx.send("Automation Team module is active.")


async def setup(bot: commands.Bot):
    await bot.add_cog(AutomationTeam(bot))
