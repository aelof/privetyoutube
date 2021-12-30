from telethon import events, Button
# from telethon.client import buttons
from telethon.tl.custom import Message
from gen import bot
import requests
from helpers import clean_video_link
from time import sleep


markup = [Button.text('скачать видео', single_use=True, resize=True)]


@bot.on(events.NewMessage(pattern='/start'))
async def reload_command(event: Message):
    await event.respond('Я проснулся и готов помочь тебе скачать видео, ориентируйся по кнопкам ниже )', buttons=markup)


@bot.on(events.NewMessage(func=lambda event: event.text.lower() == 'скачать видео'))
async def download_video(event: Message):
    chat = await event.get_chat()
    async with bot.conversation(event.chat_id) as conv:
        await conv.send_message('Отправьте ссылку с youtube: \n\nпример: "https://www.youtube.com/watch?v=ndizAUAR_Cs"', link_preview=False)
        response = await conv.get_response()
        link = response.text
    try:
        r = await requests.get(clean_video_link(link))
        if 'youtube.com' in link:
            if r.status_code == 200:
                message = await conv.send_message('Немного подождите, ваше видео готовится')
                await conv.send_file(file='/Users/uko/Documents/stock/py/tg/privetyoutube/smile.png')
                await message.edit('hello my dear with english')
                await message.delete()
    except Exception:
        print('wrong link')
        await conv.send_message('Ссылка указана неверно, попробуйет ещё', buttons=markup)