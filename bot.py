import discord
import os

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Midzo está conectado como {client.user}")

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if client.user in message.mentions:
        await message.channel.send(
            f"¡Hola, {message.author.display_name}! "
            "Soy Midzo. ¿De qué hablamos?"
        )

    elif message.content.lower() == "hola midzo":
        await message.channel.send("¡Holaaa! ¿Cómo estás?")

@client.event
async def on_member_join(member):
    channel = member.guild.system_channel
    if channel:
        await channel.send(
            f"¡Bienvenido/a {member.mention}! Soy Midzo."
        )

if not TOKEN:
    raise RuntimeError("Falta configurar DISCORD_TOKEN")

client.run(TOKEN)
