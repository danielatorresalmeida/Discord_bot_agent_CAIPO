import logging
import discord
from discord.ext import commands

log = logging.getLogger(__name__)

ROBOTICS_CHANNELS = {
    "robotics-research",
    "robotics-meetings",
    "robotics-help",
    "robotics-general",
    "humanoid-general",
}


class AIRobotics(commands.Cog):
    """AI Robotics team logic."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    def is_robotics_channel(self, channel: discord.abc.GuildChannel) -> bool:
        return isinstance(channel, discord.TextChannel) and channel.name in ROBOTICS_CHANNELS

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return
        if not self.is_robotics_channel(message.channel):
            return

        log.info(f"[AI ROBOTICS] {message.channel.name} | {message.author}: {message.content}")

        # Fun reaction
        try:
            await message.add_reaction("🤖")
        except Exception as e:
            log.warning(f"Robotics reaction failed: {e}")

        text = (message.content or "").lower()
        if "help" in text or "issue" in text or "problem" in text:
            await message.channel.send(
                f"Hi {message.author.mention}, the AI Robotics team will review this. "
                f"Please include logs, screenshots, or repro steps if possible."
            )

    @commands.command(name="robotics-status")
    async def status(self, ctx: commands.Context):
        """Check that the AI Robotics cog is running."""
        if not self.is_robotics_channel(ctx.channel):
            return
        await ctx.send("AI Robotics module is active and monitoring robotics channels.")


async def setup(bot: commands.Bot):
    await bot.add_cog(AIRobotics(bot))
