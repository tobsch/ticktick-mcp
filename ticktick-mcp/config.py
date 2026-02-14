import os

TICKTICK_API_BASE = "https://api.ticktick.com/open/v1"
TICKTICK_API_KEY = os.environ["TICKTICK_API_KEY"]
HEADERS = {
    "Authorization": f"Bearer {TICKTICK_API_KEY}",
    "Content-Type": "application/json",
}
