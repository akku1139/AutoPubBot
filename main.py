import discord

client = discord.Client(
  intents = discord.Intents(messages=True)
)

@client.event
async def on_message(m: discord.Message):
  await m.publish()

if __name__ == "__main__":
  import os
  TOKEN = os.environ.get("DISCORD_TOKEN")

  if TOKEN is None:
    print("Set the token in the environment variable DISCORD_TOKEN.")
    exit(1)

  client.run(TOKEN)
