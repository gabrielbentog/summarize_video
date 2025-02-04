from pytubefix import YouTube
from pytubefix.cli import on_progress
import whisper
import subprocess

url = "https://www.youtube.com/watch?v=G3e-8EWdv8c"

yt = YouTube(url, on_progress_callback=on_progress)
print(yt.title)

ys = yt.streams.get_audio_only()
ys.download()

# -----------------------------
model = whisper.load_model("turbo")

import subprocess

filename = "O NARUTO PODE SER UM POUCO DURO AS VEZES....m4a"
model_name = "large-v3"

subprocess.run(
  [
    "whisper",
    filename,                    # Arquivo de áudio
    "--language", "pt",           # Forçar idioma para melhorar precisão
    "--model", model_name,        # Definir o modelo
    "--output_dir", f"output-{model_name}",   # Salvar saída no diretório correto
    "--fp16", "True",             # Usar precisão reduzida (melhor performance em GPU)
    "--temperature", "0.2",         # Reduz variação nas transcrições
    "--beam_size", "1",           # Aumenta a precisão
    "--best_of", "1",             # Mantém a melhor transcrição
    "--output_format", "txt"      # Especificar formato de saída como txt
  ]
)

# result = model.transcribe("Jogando cs com os amiguinhos..m4a", language="pt")

# temp_transcription = open("transcription.txt", "w")
# temp_transcription.write(result["text"])
