import os
import re
from pytubefix import YouTube
from pytubefix import Playlist
from pytubefix.cli import on_progress
from utils import parametrize_title

def download_audio(url, output_folder="temp", index=None):
    yt = YouTube(url, on_progress_callback=on_progress)
    title = parametrize_title(yt.title)
    
    # Se o índice for fornecido, prefixa o título com ele (formatação com 2 dígitos)
    if index is not None:
        file_name = f"{index:02d}_{title}"
    else:
        file_name = title
  
    # Cria uma pasta específica para o vídeo dentro da pasta de saída
    video_folder = os.path.join(output_folder, file_name)
    os.makedirs(video_folder, exist_ok=True)
  
    ys = yt.streams.get_audio_only()
    audio_path = os.path.join(video_folder, f"{file_name}.m4a")
  
    if os.path.exists(audio_path):
        print(f"✅ Áudio já baixado em: {audio_path}")
        return audio_path
  
    # Realiza o download do áudio para a pasta do vídeo
    print("Baixando o áudio...")
    ys.download(output_path=video_folder, filename=f"{file_name}.m4a")
  
    if os.path.exists(audio_path):
        print(f"✅ Áudio salvo em: {audio_path}")
    else:
        print("❌ Falha ao baixar o áudio!")
  
    return audio_path
