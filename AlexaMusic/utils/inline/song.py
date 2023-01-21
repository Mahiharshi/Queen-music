#
# Copyright (C) 2021-2022 by alone_support@Github, < https://github.com/Jankarikiduniya >.
# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group

# Kanged By © @alone_support
# Rocks © @alone_support
# Owner harsh op 
# harsh op
# All rights reserved. © Alisha © Alexa © Yukki


from pyrogram.types import InlineKeyboardButton


def song_markup(_, vidid):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["SG_B_2"],
                callback_data=f"song_helper audio|{vidid}",
            ),
            InlineKeyboardButton(
                text=_["SG_B_3"],
                callback_data=f"song_helper video|{vidid}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="• sᴜᴩᴩᴏʀᴛ •",
                url="https://t.me/alone_support",
            ),
            InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close"),
        ],
    ]
    return buttons
