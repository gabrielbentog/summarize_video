import os
import torch
from faster_whisper import WhisperModel

def transcribe_audio(audio_path):
  transcription_path = audio_path.replace(".m4a", ".txt")
  
  print(transcription_path)

  if os.path.exists(transcription_path):
    print(f"✅ Transcrição já realizada em: {transcription_path}")
    with open(transcription_path, "r") as f:
      return f.read()

  # Define o dispositivo: "cuda" se houver GPU, senão "cpu"
  device = "cuda" if torch.cuda.is_available() else "cpu"
  # Escolhe o tipo de computação: FP16 na GPU para otimizar e INT8 na CPU
  compute_type = "float16" if device == "cuda" else "int8"

  model = WhisperModel("large-v3", device=device, compute_type=compute_type)
  segments, info = model.transcribe(audio_path, beam_size=5, language="pt")
  transcription_text = " ".join(segment.text.strip() for segment in segments)
  
  # Salva a transcrição em um arquivo .txt
  with open(transcription_path, "w", encoding="utf-8") as f:
    f.write(transcription_text)

  return transcription_text

