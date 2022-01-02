import os

from telethon import events, Button
from telethon.tl.custom import Message
from gen import bot

from helpers import clean_video_link, is_video_valid, get_download_link


markup = [Button.text('скачать видео', single_use=True, resize=True)]


@bot.on(events.NewMessage(pattern='/start'))
async def reload_command(event: Message):
    await event.respond('Я проснулся и готов помочь скачать видео, ориентируйся по кнопкам ниже )', buttons=markup)


@bot.on(events.NewMessage(func=lambda event: event.text.lower() == 'скачать видео'))
async def download_video(event: Message):
    chat = await event.get_chat()
    async with bot.conversation(event.chat_id) as conv:
        await conv.send_message('Отправьте youtube ссылку:\n\nпример: "https://www.youtube.com/watch?v=ndizAUAR_Cs"', link_preview=False)
        response = await conv.get_response()
        link = clean_video_link(response.text)
        print(link)
        if is_video_valid(link):
            message = await conv.send_message('Немного подождите, ваше видео готовится')
            await conv.send_message(get_download_link(link))

        else:
            await conv.send_message('Похоже, что ссылка нерабочая')
