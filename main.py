from dhooks import Webhook, Embed
from colorama import Fore, Back, Style
import time
import os
import sys


Version = 'Release 1.0.1'
sys.stdout.write(f"ThunderHook {Version}")

os.system("")
print(Fore.LIGHTMAGENTA_EX, Style.BRIGHT)
print(r"     ________                    __          __  __            __  ")
time.sleep(0.05)
print(r"    /_  __/ /_  __  ______  ____/ /__  _____/ / / /___  ____  / /__")
time.sleep(0.05)
print(r"     / / / __ \/ / / / __ \/ __  / _ \/ ___/ /_/ / __ \/ __ \/ //_/")
time.sleep(0.05)
print(r"    / / / / / / /_/ / / / / /_/ /  __/ /  / __  / /_/ / /_/ / ,<   ")
time.sleep(0.05)
print(r"   /_/ /_/ /_/\__,_/_/ /_/\__,_/\___/_/  /_/ /_/\____/\____/_/|_|  ")
time.sleep(0.75)
print(Fore.WHITE)
print(f"Welcome to ThunderHook {Version}!")
print("")
time.sleep(1)

print(Fore.RED + r"/!\ The creators of ThunderHook are NOT responsible for the malicious usage of ThunderHook that could break discord TOS.")
print(Fore.WHITE)
time.sleep(1)

InputHook = input("Waiting for Webhook URL > ")
hook = Webhook(InputHook)
time.sleep(1)

Mode = input("What would you like to do? (1 = Send Messages via Webhook | 2 = Modify Webhook | 3 = Webhook Info) > ")

if Mode == "1":
    MsgMode = input("What would you like to do? (1 = Nuke Webhook (Spam) | 2 = Send Standalone Messages) > ")

    if MsgMode == "1":
        SpamMessage = input("Input the message you wish to spam here > ")
        MsgA = 0
        while True:
            hook.send(SpamMessage)
            MsgA = MsgA + 1
            print(Fore.LIGHTGREEN_EX + "[+] Message Sent! (" + str(MsgA) + ")")

    if MsgMode == "2":
        print("Input the messages you wish to send:")
        while True:
            Msg = input("> ")
            hook.send(Msg)

if Mode == "2":
    Modification = input("What would you like to do? (1 = Modify Name | 2 = Delete Webhook) > ")

    if Modification == "1":
        HookName = input("What would you like to set the Webhook name to? > ")
        hook.modify(name=HookName)
        print(Fore.LIGHTGREEN_EX + f"Webhook's name was changed to '{HookName}' successfully!")
        time.sleep(1)
        print("This window will close soon..")
        time.sleep(3)
        print(Style.RESET_ALL)

    if Modification == "2":
        print(Fore.RED + r"/!\ WARNING: YOU WILL NOT BE ABLE TO RECOVER THE WEBHOOK AFTER DELETION.")
        DelWarn = input("Type '1' to confirm webhook deletion. > ")
        print(Style.RESET_ALL)

        if DelWarn == "1":
            hook.delete()
            print(Fore.LIGHTGREEN_EX + "Webhook permanently deleted. This window will close soon..")
            time.sleep(3)

        elif DelWarn != "1":
            print("Deletion cancelled. This window will close soon..")
            time.sleep(3)

if Mode == "3":
    hook.get_info()
    print("Guild ID: " + str(hook.guild_id))
    time.sleep(0.2)
    print("Channel ID: " + str(hook.channel_id))
    time.sleep(2)
    print(Fore.LIGHTGREEN_EX + "This window will close in a few seconds.")
    time.sleep(30)
