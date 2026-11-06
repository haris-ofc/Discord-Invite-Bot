"""Shared helpers used by the command and event files."""
import discord

import config
import db
from emojis import e

NO_PINGS = discord.AllowedMentions.none()


def fmt_age(seconds: float) -> str:
    seconds = max(0, int(seconds))
    days = seconds // 86400
    if days >= 365:
        return f"{days // 365}y {(days % 365) // 30}mo"
    if days >= 30:
        return f"{days // 30}mo {days % 30}d"
    if days >= 1:
        return f"{days}d"
    if seconds >= 3600:
        return f"{seconds // 3600}h"
    return f"{seconds // 60}m"


def created_ts(uid) -> float:
    """Account creation time, derived from the user's snowflake ID."""
    return discord.utils.snowflake_time(int(uid)).timestamp()


def invitees(gid: int, inviter_id: int) -> list[tuple[str, dict]]:
    members = db.guild(gid)["members"]
    return [(uid, rec) for uid, rec in members.items() if rec["inviter"] == inviter_id]


def status_of(guild: discord.Guild, uid: str, rec: dict) -> str:
    if guild.get_member(int(uid)) is None:
        return f"{e('status_left')} left"
    if rec["fake"]:
        return f"{e('status_new')} new account"
    return f"{e('status_in')} in server"


def invitee_line(guild: discord.Guild, uid: str, rec: dict, show_inviter: bool = False) -> str:
    age = fmt_age(rec["at"] - created_ts(uid))
    line = f"<@{uid}>"
    if show_inviter:
        inviter = f"<@{rec['inviter']}>" if rec["inviter"] else "Unknown"
        line += f" ← {inviter}"
    return f"{line} • joined <t:{int(rec['at'])}:R> • acct age **{age}** • {status_of(guild, uid, rec)}"


def summary_embed(user: discord.abc.User, s: dict) -> discord.Embed:
    embed = discord.Embed(
        title="Invite statistics",
        description=f"{e('total')} **{db.total(s)}** total invites",
        color=config.COLOR,
    )
    embed.set_author(name=user.name, icon_url=user.display_avatar.url)
    embed.add_field(name=f"{e('joined')} Joined", value=str(s["regular"]))
    embed.add_field(name=f"{e('left')} Left", value=str(s["left"]))
    embed.add_field(name=f"{e('fake')} Fake", value=str(s["fake"]))
    embed.add_field(name=f"{e('bonus')} Bonus", value=str(s["bonus"]))
    return embed


async def send_log(guild: discord.Guild, embed: discord.Embed) -> None:
    channel_id = db.guild(guild.id)["log_channel"]
    if not channel_id:
        return
    channel = guild.get_channel(channel_id)
    if channel:
        try:
            await channel.send(embed=embed, allowed_mentions=NO_PINGS)
        except discord.HTTPException:
            pass
