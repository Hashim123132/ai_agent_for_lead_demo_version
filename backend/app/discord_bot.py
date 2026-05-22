import os
import discord
from dotenv import load_dotenv

from app.agent import chat_with_agent

load_dotenv()

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"Discord bot is running as {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    user_message = message.content.strip()

    if not user_message:
        return

    await message.channel.typing()

    session_id = f"discord-{message.author.id}"

    try:
        reply = chat_with_agent(session_id, user_message)
        await message.reply(reply)
    except Exception as e:
        print("Discord bot error:", e)
        await message.reply("Sorry, something went wrong.")


if not DISCORD_BOT_TOKEN:
    raise ValueError("DISCORD_BOT_TOKEN is missing in .env")

client.run(DISCORD_BOT_TOKEN)