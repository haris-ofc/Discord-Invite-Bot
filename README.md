# Invite Tracker Bot

A Discord invite tracking bot built with discord.py. Free to run, no database needed.
Every command lives in its own file, and every emoji can be changed from one place.

## Features
- Detects which invite a member used and who created it (including single-use invites and vanity URL)
- Tracks joined / left / fake (new account) / bonus invites
- Join and leave log channel
- Custom bot status and activity from `.env`
- Custom emoji support for every embed

## Setup
1. Create an application at https://discord.com/developers/applications and copy the bot token.
2. Bot tab -> enable **Server Members Intent**.
3. Invite the bot with scopes `bot` + `applications.commands` and permissions:
   View Channels, Send Messages, Embed Links, Use External Emojis, **Manage Server**.
4. Copy `.env.example` to `.env` and fill it in.
5. Install and run (Python 3.10+):
   ```
   pip install -r requirements.txt
   python bot.py
   ```

## Commands
| Command | Description | Permission |
|---|---|---|
| `/invites [user]` | Show invite stats | Everyone |
| `/leaderboard` | Top 10 inviters | Everyone |
| `/inviter user` | Who invited a member | Everyone |
| `/invited [user]` | Everyone a member invited, with account age & status | Everyone |
| `/joininfo user` | Inviter, code, join date, account age | Everyone |
| `/recentjoins` | Last 10 joins with inviter | Everyone |
| `/invitecodes [user]` | Active invite links, uses, creator | Everyone |
| `/inviteage [user]` | Average/oldest/newest account age of invitees | Everyone |
| `/serverstats` | Overall tracking stats | Everyone |
| `/help` | List all commands | Everyone |
| `/setlogchannel` | Set join/leave log channel | Manage Server |
| `/addbonus user amount` | Add/remove bonus invites | Manage Server |
| `/resetinvites` | Wipe all data | Administrator |

## Project structure
```
bot.py            entry point, auto-loads everything in cmds/ and events/
config.py         colors, intents, fake-account age, status/activity
emojis.py         ALL emojis - edit this file to use your custom emojis
helpers.py        shared helper functions
db.py             JSON storage (data.json)
events/tracker.py invite detection (join / leave / invite events)
cmds/             one file per slash command
```

## Custom emojis
Open `emojis.py` and replace any value with your emoji code:
```python
"stats": "<a:stats:1567917023990648842>",   # animated
"leaderboard": "<:trophy:123456789012345678>",  # static
```
To get the code, type `\:emoji_name:` in Discord (with the backslash) and send it.
The bot must be in the server that owns the emoji and have **Use External Emojis**.
Emojis are placed in descriptions and field names. Slash command names can never contain emojis (Discord rule).

## Custom status & activity (`.env`)
- `BOT_STATUS` - `online`, `idle`, `dnd` or `invisible`
- `BOT_ACTIVITY_TYPE` - `playing`, `watching`, `listening`, `competing` or `streaming`
- `BOT_ACTIVITY_TEXT` - the text shown
- `BOT_STREAM_URL` - Twitch/YouTube link, only for `streaming`
- `FAKE_ACCOUNT_AGE_DAYS` - accounts younger than this count as fake joins (default 7)

## Adding a new command
Copy any file in `cmds/`, rename the class and command, and restart. It loads automatically.
Slash commands are re-synced only when a file in `cmds/` changes, so restarts don't hit rate limits.

## Publishing
Never upload `.env` or `data.json` (the included `.gitignore` already excludes them).
If your token ever leaks, reset it in the Developer Portal.

## Credits
Made by **Hydra Developer - Haris**
