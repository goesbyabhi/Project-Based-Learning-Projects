import discord, requests, re, json
from discord.ext import commands
from colorama import Fore
from datetime import datetime
from urllib.request import Request, urlopen

with open("config.json") as token_file:
    tokens = json.load(token_file)

user_token = {}
for token in tokens:
    user_token.update(tokens)

alt_token = user_token["alt_token"]
main_token = user_token["main_token"]
webhook = user_token["WEBHOOK_URL"]
ping = True

logo =( f"""{Fore.RED}\
 █████╗     ██╗   ██╗    ██████╗      ██████╗     ██████╗      █████╗ 
██╔══██╗    ██║   ██║    ██╔══██╗    ██╔═══██╗    ██╔══██╗    ██╔══██╗
███████║    ██║   ██║    ██████╔╝    ██║   ██║    ██████╔╝    ███████║
██╔══██║    ██║   ██║    ██╔══██╗    ██║   ██║    ██╔══██╗    ██╔══██║
██║  ██║    ╚██████╔╝    ██║  ██║    ╚██████╔╝    ██║  ██║    ██║  ██║
╚═╝  ╚═╝     ╚═════╝     ╚═╝  ╚═╝     ╚═════╝     ╚═╝  ╚═╝    ╚═╝  ╚═╝                                                                       
""" + Fore.RESET)

print(logo)

time = datetime.now().strftime("%H:%M %p")

Snipr = discord.Client()
Snipr = commands.Bot(command_prefix="!", self_bot=False)


@Snipr.event
async def on_ready():
    print(f"Log in time - {time}\nSnipping as: {Fore.GREEN}[{Snipr.user.name}#{Snipr.user.discriminator}]\nYou're ready to snipe!😈" + Fore.RESET)

@Snipr.event
async def on_message(message):
    async for  message in message.channel.history(limit=1):
        content = message.content

    def Nitro(code):
        output=(
            f"{Fore.RED}Nitro Sniped!"
            f"\n{Fore.GREEN}Code: {Fore.CYAN}[{code}]"
            f"\n{Fore.GREEN}Server: {Fore.CYAN}[{message.guild}]"
            f"\n{Fore.GREEN}Channel: {Fore.CYAN}[{message.channel}]"
            + Fore.RESET
        )
        print(output)
        message = '@everyone' if ping else ''
        message += f'```{output}```'

    try:
        if 'discord.gift/' in content:
            code = re.search("discord.gift/(.*)", content).group(1)
            headers = {'Authorization': main_token}
            r = requests.post(
                f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}/redeem',
                headers=headers,
            ).text

            if 'This gift has been redeemed already.' in r:
                print(""
                        f"\n{Fore.RED}[{time} - USED NITRO CODE]" + Fore.RESET)
                Nitro(code)
            elif 'Unknown Gift Code' in r:
                print(""
                        f"\n{Fore.YELLOW}[{time} - INVALID NITRO CODE]" + Fore.RESET)
                Nitro(code)
            elif 'subscription_plan' in r:
                print(f"\n{Fore.GREEN}[{time} - REDEEMED!🎉" + Fore.RESET)
                Nitro(code)
            else:
                return
    except AttributeError:
        pass
    
Snipr.run(alt_token, bot=False, reconnect=True)