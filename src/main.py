from bot import bot
from telebot.types import Message, File
from transcriber import transcribe

def save_voice(message: Message) -> None:
	file_info: File = bot.get_file(message.voice.file_id)
	voice: bytes = bot.download_file(file_info.file_path)
	with open(file='_temp\.ogg', mode='wb') as temp_file:
		temp_file.write(voice)

@bot.message_handler(commands=['start'])
def on_start(message: Message) -> None:
	bot.send_message(chat_id=message.from_user.id,
	                  text='Hello!')

@bot.message_handler(content_types=['voice'])
def on_voice(message: Message) -> None:
	save_voice(message=message)
	transcription: str = transcribe()
	bot.send_message(chat_id=message.from_user.id,
	                 text=transcription)

if __name__ == '__main__':
	bot.infinity_polling()