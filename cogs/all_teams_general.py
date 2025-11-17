import logging
import discord
from discord.ext import commands

log = logging.getLogger(__name__)

ALL_TEAMS_CHANNELS = {
    "welcome-channel",
    "announcements",
    "weekly-meeting-schedule",
    "all-teams-meetings",
    "general-chat",
}


class AllTeamsGeneral(commands.Cog):
    """Logic for global cross team channels."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    def is_all_teams_channel(self, channel: discord.abc.GuildChannel) -> bool:
        return isinstance(channel, discord.TextChannel) and channel.name in ALL_TEAMS_CHANNELS

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return
        if not self.is_all_teams_channel(message.channel):
            return

        log.info(f"[ALL TEAMS] {message.channel.name} | {message.author}: {message.content}")

    @commands.command(name="allteams-status")
    async def status(self, ctx: commands.Context):
        """Check that the All Teams cog is running."""
        if not self.is_all_teams_channel(ctx.channel):
            return
        await ctx.send("All Teams module is active and watching global channels.")


async def setup(bot: commands.Bot):
    await bot.add_cog(AllTeamsGeneral(bot))
