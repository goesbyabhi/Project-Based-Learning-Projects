import discord, json, asyncio
from discord.ext import commands
from colorama import Fore, init
from datetime import datetime

init()
time = datetime.now().strftime("%H:%M %p")

with open("config.json") as token_file:
    tokens = json.load(token_file)

user_token = {}
for token in tokens:
    user_token.update(tokens)

token = user_token["main_token"]

prefix = input(f"{Fore.YELLOW}BOT PREFIX: "+ Fore.RESET)

cloner = discord.Client()
cloner = commands.Bot(command_prefix=prefix, case_insensitive=True, self_bot=True)
cloner.remove_command('help')
header = {"Authorization: " f"Bot {token}"}

intents = discord.Intents.all()
intents.members = True

@cloner.event
async def on_ready():
    print(f"""
    \nBot online!
    Logged in as {cloner.user.name}
    Command = {prefix}clone
    Time = {time}
    """)
@cloner.command()
async def clone(ctx):
    await ctx.message.delete()
    mk_srvr = await cloner.create_guild(f'Copy of {ctx.guild.name}')
    await asyncio.sleep(4)
    for gld in cloner.guilds:
        if f'Copy of {ctx.guild.name}' in gld.name:
            for chan in gld.channels:
                await chan.delete()
            for category in ctx.guild.categories:
                mk_ctgry = await gld.create_category(f"{category.name}")
                print(f"\nNew category {category.name} created\n")
                for channel in category.channels:
                    if isinstance(channel, discord.TextChannel):
                        await mk_ctgry.create_text_channel(f"{channel.name}")
                        print(f"\nNew text channel {channel.name} created\n")
                    if isinstance(channel, discord.VoiceChannel):
                        await mk_ctgry.create_voice_channel(f"{channel.name}")
                        print(f"\nNew voice channel {channel.name} created\n")
    print("\nChannels created. Creating roles...\n")

    for role in ctx.guild.roles[::-1]:
        if role.name != "@everyone":
            try:
                await mk_srvr.create_role(name=role.name, permissions=role.permissions, colour=role.colour, hoist=role.hoist, mentionable=role.mentionable)
                print(f"\nNew role {role.name} added\n")
            except:
                print("Error in creating roles")
                break
        print("Server and roles cloned successfully.")

cloner.run(token, bot=False)