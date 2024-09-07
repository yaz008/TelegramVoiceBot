from os import getenv
from whisper import load_model, Whisper

def transcribe() -> str:
	model: Whisper = load_model(name='base',
	                            download_root=getenv(key='WHISPER_MODELS'))
	transcription: dict[str, str | list] = model.transcribe(audio='_temp\.ogg',
	                                                        verbose=False)
	return transcription['text']