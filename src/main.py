from download_audio import download_audio
from download_audio import download_playlist_audio
from transcription import transcribe_audio
from summarize import summarize_text

def main():
  url = "https://www.youtube.com/watch?v=jQMbuK6URws&list=PLHz_AreHm4dm24MhlWJYiR_Rm7TFtvs6S&index=1"
  audio_path = download_audio(url)
  text = transcribe_audio(audio_path)
  summarize_text(text, audio_path)

if __name__ == "__main__":
    main()