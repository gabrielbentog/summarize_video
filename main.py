from pytubefix import YouTube
from pytubefix.cli import on_progress
import whisper
import subprocess
import re
import torch
import os
from dotenv import load_dotenv
from google import genai
import unicodedata

load_dotenv()

print("🚀 Iniciando...")

def parametrize_title(title: str) -> str:
  # Normaliza a string para separar os acentos dos caracteres
  title_parametrize = unicodedata.normalize('NFKD', title)
  # Codifica para ASCII, ignorando caracteres que não puderem ser convertidos (como acentos)
  title_sem_acento = title_parametrize.encode('ASCII', 'ignore').decode('ASCII')
  # Remove caracteres especiais, mantendo apenas letras, números e espaços
  title_limpo = re.sub(r'[^A-Za-z0-9\s]', '', title_sem_acento)
  return title_limpo.replace(" ", "_").lower()

# download audio from youtube
def download_audio(url, output_folder="temp"):
  yt = YouTube(url, on_progress_callback=on_progress)
  file_name = parametrize_title(yt.title)

  os.makedirs(output_folder, exist_ok=True)

  ys = yt.streams.get_audio_only()
  audio_path = f"{output_folder}/{file_name}.m4a"

  if os.path.exists(audio_path):
    print(f"✅ Áudio já baixado em: {audio_path}")
    return audio_path
  
  # Realiza o download do áudio para o caminho especificado
  print("Baixando o áudio...")
  ys.download(output_path=output_folder, filename=f"{file_name}.m4a")
  
  if os.path.exists(audio_path):
      print(f"✅ Áudio salvo em: {audio_path}")
  else:
      print("❌ Falha ao baixar o áudio!")

  return audio_path

# transcribe audio
def transcribe_audio(audio_path):
  transcription_path = audio_path.replace(".m4a", ".txt")
  
  print(transcription_path)

  if os.path.exists(transcription_path):
    print(f"✅ Transcrição já realizada em: {transcription_path}")
    with open(transcription_path, "r") as f:
      return f.read()

  device = "cuda" if torch.cuda.is_available() else "cpu"
  model = whisper.load_model("turbo", device=device)
  result = model.transcribe(audio_path, language="pt")

  # save transcription in .txt file
  with open(transcription_path, "w") as f:
    f.write(result["text"])

  return result["text"]

url = "https://www.youtube.com/watch?v=jQMbuK6URws&list=PLHz_AreHm4dm24MhlWJYiR_Rm7TFtvs6S&index=1"

audio_path = download_audio(url)

text = transcribe_audio(audio_path)

client = genai.Client(api_key=os.getenv("GEMINI_KEY"))
response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=f"""Please generate a concise and accurate summary of the text below, in Brazilian Portuguese. The summary must be organized into topics, according to the items listed below, and formatted in Markdown (.md):
      1. **Context:** A brief description of the scenario or situation covered in the text.
      2. **Objectives/Purpose:** What the text intends to address or achieve.
      3. **Main Points:** Main arguments, ideas or facts presented.
      4. **Relevant Details:** Information, examples and data that support the main points.
      5. **Conclusion:** The final message, implications or results derived from the text.
      6. **Recommendations/Implications (when applicable):** Suggestions or recommended actions presented in the text.

      Do not include additional information or comments beyond the items requested.

      Text:
      {text}
    """
)

print(response.text)

# save summary in .md file
with open("summary.md", "w") as f:
  f.write(response.text)