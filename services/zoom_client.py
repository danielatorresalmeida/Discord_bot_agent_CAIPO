# zoom_client.py
import os
import logging
from datetime import datetime, timedelta

log = logging.getLogger(__name__)


class ZoomClient:
    """
    Placeholder Zoom client.

    Later you will:
    - Put ZOOM_API_KEY / ZOOM_API_SECRET or OAuth token in env vars
    - Call Zoom REST API to list meetings, etc.
    """

    def __init__(self):
        self.token = os.getenv("ZOOM_TOKEN")  # or OAuth token later
        if not self.token:
            log.warning("ZOOM_TOKEN not set. Using dummy meetings.")

    async def get_next_meeting_for_user(self, user_email: str) -> str:
        """
        TODO: Call Zoom API to get upcoming meetings for this user.
        For now, returns a dummy string.
        """
        log.info(f"Requested Zoom next meeting for {user_email}")

        if not self.token:
            start = datetime.utcnow() + timedelta(hours=2)
            return (
                f"(Zoom mock) Next meeting for {user_email} at "
                f"{start:%Y-%m-%d %H:%M} UTC on 'Flo Labs Sync'."
            )

        # Later: implement real API call
        return f"(Zoom stub) Next meeting for {user_email} (real Zoom API not implemented yet)."
