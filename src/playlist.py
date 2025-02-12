from pytubefix import Playlist
from download_audio import download_audio  # Função que você já criou para baixar um vídeo
from transcription import transcribe_audio  # Função que você já criou para transcrever um áudio
from summarize import summarize_text  # Função que você já criou para resumir um texto
from utils import parametrize_title
import os

url = input("Digite a URL da playlist: ")
pl = Playlist(url)
playlist_title = parametrize_title(pl.title)
playlist_folder = f"temp/{playlist_title}"
os.makedirs(playlist_folder, exist_ok=True)

for index, video in enumerate(pl.videos, start=1):
  video_url = video.watch_url

  audio_path = download_audio(video_url, playlist_folder, index=index)
  text = transcribe_audio(audio_path)
  summarize_text(text, audio_path)

