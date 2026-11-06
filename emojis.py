r"""
All emojis used by the bot live here - edit this file to customise them.

Default values are normal unicode emojis, so the bot works out of the box.

To use a custom emoji:
  1. Type  \:emoji_name:  in Discord (with the backslash) and send it.
  2. Copy the result, e.g.  <a:stats:1567917023990648842>  (animated)
     or  <:stats:1567917023990648842>  (static).
  3. Paste it as the value below.

The bot must be in the server that owns the emoji (and have the
"Use External Emojis" permission) for custom emojis to display.
"""

EMOJIS = {
    # general
    "success": "<:Tick:1568132116896555099>",
    "error": "<:CROSS_ZS:1568132224220405770>",
    "stats": "<a:stats:1567917023990648842>",
    "invites": "<:5575members:1568132816557052047>>",
    "leaderboard": "<:config_leader:1568132684234883112>",
    "total": "<a:CxT_Disco:1568132927810834502>",
    # leaderboard medals
    "medal_1": "<:RankPlatinum:1567918014605824060>",
    "medal_2": "<:RankGold:1567917896649277591>",
    "medal_3": "<:RankSilver:1567917947073331364>",
    # invite counters
    "joined": "<a:ruin_Tick:1568133234355601541>",
    "left": "<:wowfake:1568133679740362752>",
    "fake": "<a:cautiondude:1568133404099088488>",
    "bonus": "<a:Gift:1568133508046520381>",
    # member details
    "inviter": "<:5575members:1532384137728622632>",
    "code": "<:linkperms:1568133903259144212>",
    "joined_at": "<a:calendar:1568133994451828819>",
    "account": "<a:TIMER_COUNT:1568134293278957609>",
    "age": "<a:time:1568134203449544734>",
    "crown": "<a:crown_crown:1568134395095679040>",
    # status badges in lists
    "status_in": "<:Tick:1568132116896555099>",
    "status_left": "<:CROSS_ZS:1568132224220405770>",
    "status_new": "<:CROSS_ZS:1568132224220405770>",
    # log channel
    "log_join": "<:5575members:1568132816557052047>",
    "log_leave": "<a:leftwing:1568134799992946748>",
}


def e(name: str) -> str:
    """Return the emoji for a key (empty string if the key doesn't exist)."""
    return EMOJIS.get(name, "")
