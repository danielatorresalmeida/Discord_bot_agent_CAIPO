# readai_client.py
import os
import logging

log = logging.getLogger(__name__)


class ReadAIClient:
    """
    Placeholder ReadAI client.

    Later you will:
    - Store READAI_API_KEY in env vars
    - Call ReadAI's HTTP API for summaries / transcripts
    """

    def __init__(self):
        self.api_key = os.getenv("READAI_API_KEY")
        if not self.api_key:
            log.warning("READAI_API_KEY not set. Using dummy summaries.")

    async def summarize_meeting(self, meeting_id: str) -> str:
        """
        TODO: Call ReadAI API with the meeting_id.
        For now, returns a dummy summary so the bot still works.
        """
        log.info(f"Requested ReadAI summary for meeting_id={meeting_id}")

        if not self.api_key:
            return f"(ReadAI mock) Summary for meeting {meeting_id}."

        # Later: implement real HTTP request here
        return f"(ReadAI stub) Summary for meeting {meeting_id} (real API not implemented yet)."
from services.notifications import notify_personal

...
await target_channel.send(embed=embed)  # existing line

await notify_personal(
    self.bot,
    f"✅ Sent {len(entries)} time entries to {target_channel.mention}"
)
