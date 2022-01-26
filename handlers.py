import os

from telethon import events, Button
from telethon.tl.custom import Message
from gen import bot

from helpers import clean_video_link, is_video_valid, get_download_link


@bot.on(events.NewMessage(pattern='/start'))
async def reload_command(event: Message):
    await event.respond('Я проснулся и готов помочь скачать видео, отправьте ссылку на него ')


@bot.on(events.NewMessage(func=lambda event: 'youtube' in event.text))
async def download_video(event: Message):
    link = clean_video_link(event.text)
    if is_video_valid(link):
        try:
            await event.respond('Немного подождите, ваша ссылка проверяется')
            await event.respond(f'Вот ваша ссылка: <a href="{get_download_link(link)}">ссылка на источник видео</a>')
        except Exception as e:
            await event.respond('Не удаётся сопоставить ссылку с видео, попробуйте другую')
