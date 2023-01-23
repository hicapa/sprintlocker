# <>-------------------------------------------------------------------------------------------------------------------<>
#  ______     ______   ______     __     __   __     ______   __         ______     ______     __  __     ______     ______    
# /\  ___\   /\  == \ /\  == \   /\ \   /\ "-.\ \   /\__  _\ /\ \       /\  __ \   /\  ___\   /\ \/ /    /\  ___\   /\  == \   
# \ \___  \  \ \  _-/ \ \  __<   \ \ \  \ \ \-.  \  \/_/\ \/ \ \ \____  \ \ \/\ \  \ \ \____  \ \  _"-.  \ \  __\   \ \  __<   
#  \/\_____\  \ \_\    \ \_\ \_\  \ \_\  \ \_\\"\_\    \ \_\  \ \_____\  \ \_____\  \ \_____\  \ \_\ \_\  \ \_____\  \ \_\ \_\ 
#   \/_____/   \/_/     \/_/ /_/   \/_/   \/_/ \/_/     \/_/   \/_____/   \/_____/   \/_____/   \/_/\/_/   \/_____/   \/_/ /_/ 
#
#                                                        Version 1.0.2
#
#                                      Discord Discriminator Tool - created by hicapabex
#
#                              you can find this project at: https://github.com/hicapa/sprintlocker
#
# <>-------------------------------------------------------------------------------------------------------------------<>  
#
# "sprintlocker is licensed under a "Creative Commons BY-NC-SA 4.0" license. You can find the terms at the following link:
# https://creativecommons.org/licenses/by-nc-sa/4.0/ . If you build upon this project, please credit me by either putting
# the original link to this project in your repository, or inviting me as a collaborator. With that, thank you for checking
# out this little Python project that I made!                         
# - rebecca "hicapabex"
#
# <>-------------------------------------------------------------------------------------------------------------------<>     
# 
# Credits:
# hicapabex - programming, concept
# dolfies - discord.py-self (https://github.com/dolfies/discord.py-self)     
# 
# <>-------------------------------------------------------------------------------------------------------------------<>                                                  
#  _              _      _ 
# | |__  ___ __ _(_)_ _ | |
# | '_ \/ -_) _` | | ' \|_|
# |_.__/\___\__, |_|_||_(_)
#           |___/           (the code)

# ~~~~~~ import modules ~~~~~~
from colorama import Fore, init
from os import name, system, get_terminal_size
from requests import get, post, patch
import discord
import json

# ~~~~~~ project information ~~~~~~
version = "1.0.2"

# ~~~~~~ parse json configuration file // imports token, command prefix ~~~~~~
raw_config = open("config.json")
load_config = json.load(raw_config)
token = load_config.get("token")
prefix = load_config.get("prefix")
raw_config.close()

# ~~~~~~ colorama variables and event statuses // logging flags in terminal ~~~~~~
loginmsg = Fore.BLUE+"[LOGIN] "+Fore.RESET
cmdmsg = Fore.YELLOW+"[COMMS] "+Fore.RESET
errormsg = Fore.RED+"[ERROR] "+Fore.RESET
helprmsg = Fore.LIGHTGREEN_EX+"[HELPR] "+Fore.RESET
init()

# ~~~~~~ clear function // clears the terminal ~~~~~~
def clear():
    if name == "nt":
        system("cls")
    else:
        system("clear")

# ~~~~~~ command width operation ~~~~~~
terminal_width = get_terminal_size().columns

# ~~~~~~ function for grabbing all user guilds ~~~~~~
def scrapeguilds():
    temporarydict = {}
    for guild in client.guilds:
        guildid = guild.id
        member_count = 0
        for member in guild.members:
            if member.bot == False:
                member_count = member_count + 1
            else:
                pass
        temporarydict[guildid] = member_count
    return temporarydict

# ~~~~~~ function for grabbing all users in a guild ~~~~~~
def scrapeusers():
    return

# ~~~~~~ initialize main client ~~~~~~
class SprintLocker(discord.Client):
    async def on_ready(self):
        print(loginmsg+Fore.LIGHTMAGENTA_EX+f'Logged into Discord as {self.user}'+Fore.RESET) # delayed, looking for fix (priority low)

    async def on_message(self, message): # listens for messages
        if message.content == prefix+"roll":
            await message.delete()
            await message.channel.send("sprintlocker "+version+" > running command.")
            print(cmdmsg+Fore.LIGHTMAGENTA_EX+"Running command 'roll'")
            print(helprmsg+Fore.LIGHTMAGENTA_EX+f"Scraping {len(client.guilds)} servers for users")
            nonglobal_clients = ", ".join(guild.name+" ("+str(guild.id)+")" for guild in client.guilds)
            print(helprmsg+Fore.LIGHTMAGENTA_EX+f"Found {len(client.guilds)} servers: "+str(nonglobal_clients))
            print(helprmsg+Fore.LIGHTMAGENTA_EX+"Running scrape operation -> "+str(scrapeguilds()))
        else:
            if prefix in message.content:
                print(errormsg+Fore.LIGHTMAGENTA_EX+"Command not found")
            else:
                return

# ~~~~~~ run code (end of script) ~~~~~~
clear()
print((Fore.LIGHTGREEN_EX+"~ sprintlocker "+version+" by hicapabex ~"+Fore.RESET).center(terminal_width))
client = SprintLocker()
print(loginmsg+Fore.LIGHTMAGENTA_EX+"Attempting Login... (commands will still work, please wait a few minutes for full login)"+Fore.RESET)
client.run(token)
