#
# Copyright (C) 2021-2022 by alone_support@Github, < https://github.com/Jankarikiduniya >.
# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group

# Kanged By © @alone_support
# Rocks © @alone_support
# Owner harsh op 
# Harsh op 
# All rights reserved. © Alisha © Alexa © Yukki


import asyncio

from pyrogram import Client as c

API_ID = input("\nEnter Your API_ID:\n > ")
API_HASH = input("\nEnter Your API_HASH:\n > ")

print("\n\n Enter Phone number when asked.\n\n")

i = c(":memory:", api_id=API_ID, api_hash=API_HASH)


async def main():
    await i.start()
    ss = await i.export_session_string()
    print(
        "\nHERE IS YOUR PYROGRAM STRING SESSION, COPY IT, DON'T SHARE IT WITH YOUR GF !\n"
    )
    print(f"\n{ss}\n")


asyncio.run(main())
