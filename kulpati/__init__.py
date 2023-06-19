from telethon import TelegramClient
import logging
import time



api_id="1125689"
api_hash="4772d1792ed194020a8fb06a91ffb8fa"
bot_token="6258039017:AAFicuXPsY11eh8fKKA2EC1nxCL7WLi7zL8"

bot = TelegramClient("kulpati", api_id, api_hash).start(bot_token = bot_token)