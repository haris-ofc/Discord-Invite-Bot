"""Central settings. Values come from .env where it makes sense."""
import os

import discord
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

# Embed colors
COLOR = 0x5865F2
COLOR_JOIN = 0x57F287
COLOR_LEAVE = 0xED4245

# Accounts younger than this many days count as "fake" joins
FAKE_ACCOUNT_AGE_DAYS = int(os.getenv("FAKE_ACCOUNT_AGE_DAYS", "7"))
FAKE_ACCOUNT_AGE = FAKE_ACCOUNT_AGE_DAYS * 24 * 60 * 60

# Gateway intents ("Server Members Intent" must be enabled in the dev portal)
INTENTS = discord.Intents.default()
INTENTS.members = True
INTENTS.invites = True

_STATUSES = {
    "online": discord.Status.online,
    "idle": discord.Status.idle,
    "dnd": discord.Status.dnd,
    "invisible": discord.Status.invisible,
}
_ACTIVITY_TYPES = {
    "playing": discord.ActivityType.playing,
    "watching": discord.ActivityType.watching,
    "listening": discord.ActivityType.listening,
    "competing": discord.ActivityType.competing,
}


def build_presence():
    """Return (status, activity) from BOT_STATUS / BOT_ACTIVITY_* in .env."""
    status = _STATUSES.get(os.getenv("BOT_STATUS", "online").strip().lower(), discord.Status.online)
    text = os.getenv("BOT_ACTIVITY_TEXT", "").strip()
    kind = os.getenv("BOT_ACTIVITY_TYPE", "playing").strip().lower()
    if not text:
        return status, None
    if kind == "streaming":
        url = os.getenv("BOT_STREAM_URL", "https://twitch.tv/discord").strip()
        return status, discord.Streaming(name=text, url=url)
    return status, discord.Activity(
        type=_ACTIVITY_TYPES.get(kind, discord.ActivityType.playing), name=text
    )
