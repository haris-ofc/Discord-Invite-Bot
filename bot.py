import hashlib
import pathlib

import discord
from discord.ext import commands

import config
import db

ROOT = pathlib.Path(__file__).resolve().parent


class InviteBot(commands.Bot):
    def __init__(self):
        status, activity = config.build_presence()
        super().__init__(
            command_prefix=commands.when_mentioned,
            intents=config.INTENTS,
            status=status,
            activity=activity,
        )

    async def setup_hook(self):
        # Load every file in events/ and cmds/ automatically
        for folder in ("events", "cmds"):
            for file in sorted((ROOT / folder).glob("*.py")):
                if file.name.startswith("_"):
                    continue
                await self.load_extension(f"{folder}.{file.stem}")
                print(f"Loaded {folder}/{file.name}")

        # Sync slash commands only when the files in cmds/ changed (avoids 429 rate limits)
        digest = hashlib.sha256()
        for file in sorted((ROOT / "cmds").glob("*.py")):
            digest.update(file.read_bytes())
        current = digest.hexdigest()
        if db.data.get("command_hash") != current:
            await self.tree.sync()
            db.data["command_hash"] = current
            db.save()
            print("Slash commands synced.")
        else:
            print("Slash commands unchanged, skipping sync.")

    async def on_ready(self):
        print(f"Logged in as {self.user} ({self.user.id}) in {len(self.guilds)} server(s)")


if __name__ == "__main__":
    if not config.TOKEN:
        raise SystemExit("DISCORD_TOKEN is missing. Copy .env.example to .env and set it.")
    InviteBot().run(config.TOKEN)
