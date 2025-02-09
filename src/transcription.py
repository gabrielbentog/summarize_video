import os
import torch
import whisper

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
