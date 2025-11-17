import logging
import discord
from discord.ext import commands

from zoom_client import ZoomClient
from readai_client import ReadAIClient

log = logging.getLogger(__name__)

PM_CHANNELS = {
    "pm-general",
    "pm-meetings",
}


class PMTeam(commands.Cog):
    """Project Management team logic."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.zoom = ZoomClient()
        self.readai = ReadAIClient()

    def is_pm_channel(self, channel: discord.abc.GuildChannel) -> bool:
        return isinstance(channel, discord.TextChannel) and channel.name in PM_CHANNELS

    @commands.command(name="next-meeting")
    async def next_meeting(self, ctx: commands.Context, email: str = None):
        """
        Show next Zoom meeting for a given email address.
        Usage: !next-meeting your@email.com
        """
        if not self.is_pm_channel(ctx.channel):
            return

        if email is None:
            await ctx.send("Please provide your Zoom email. Example: `!next-meeting you@example.com`")
            return

        msg = await self.zoom.get_next_meeting_for_user(email)
        await ctx.send(msg)

    @commands.command(name="meeting-summary")
    async def meeting_summary(self, ctx: commands.Context, meeting_id: str):
        """
        Get a summary for a meeting recorded in ReadAI.
        Usage: !meeting-summary MEETING_ID
        """
        if not self.is_pm_channel(ctx.channel):
            return

        summary = await self.readai.summarize_meeting(meeting_id)
        await ctx.send(summary)

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
