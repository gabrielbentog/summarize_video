from download_audio import download_audio
from transcription import transcribe_audio
from summarize import summarize_text

def main():
  url = input("Digite a URL do vídeo: ")
  audio_path = download_audio(url)
  text = transcribe_audio(audio_path)
  summarize_text(text, audio_path)

if __name__ == "__main__":
    main()
