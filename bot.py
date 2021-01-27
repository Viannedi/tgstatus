import telethon
from telethon import TelegramClient, events
import asyncio
from  time import sleep
from telethon.tl.functions.account import UpdateProfileRequest
from datetime import datetime
from random import randint
api_id = 0
api_hash = ''
client = TelegramClient('name', api_id, api_hash)

async def progress_day():
	date = datetime.now()
	total_minute = (date.hour * 60) + date.minute
	progress = ( total_minute / 1440 ) * 100
	return progress

async def main():
	while True:
		days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

		date = datetime.now()

		day = days[date.weekday()]
		time_now = date.strftime("%H:%M")
		random_number = randint(1, 10)
		get_progress = round(await progress_day(), 2)
		await client(UpdateProfileRequest(about=f'Python Developer / {date.day} {day} {time_now} / 🎲{random_number}.       📅Progress Day {get_progress}'))
		sleep(60)

with client:
	client.loop.run_until_complete(main())

client.start()
client.run_until_disconnected()