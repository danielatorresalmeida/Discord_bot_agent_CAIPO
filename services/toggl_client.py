# toggl_client.py
import os
import logging
from datetime import datetime

log = logging.getLogger(__name__)


class TogglClient:
    """
    Placeholder Toggl client.

    Later you will:
    - Store TOGGL_API_TOKEN in env vars
    - Call Toggl Track API for time entries / summaries.
    """

    def __init__(self):
        self.api_token = os.getenv("TOGGL_API_TOKEN")
        if not self.api_token:
            log.warning("TOGGL_API_TOKEN not set. Using dummy time data.")

    async def get_today_summary(self, user_label: str = "team") -> str:
        """
        TODO: Call Toggl API and summarize hours for today.
        For now, returns a dummy summary.
        """
        log.info("Requested Toggl summary for today")

        today = datetime.utcnow().date().isoformat()
        if not self.api_token:
            return f"(Toggl mock) {user_label} has logged ~6.5h today ({today})."

        # Later: implement real API call
        return f"(Toggl stub) {user_label} time summary for {today} (real API not implemented yet)."
