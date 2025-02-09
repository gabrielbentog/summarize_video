import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

def summarize_text(text, path):
    client = genai.Client(api_key=os.getenv("GEMINI_KEY"))
    response = client.models.generate_content(
      model="gemini-2.0-flash",
      contents=f"""Please generate a concise and brief, point-by-point summary of the video content provided below, in Brazilian Portuguese. The summary should clearly capture what the video is talking about and detail, point by point, the most important aspects mentioned in the video. Organize the summary into the topics listed below and format it in Markdown (.md):
        1. **Context:** A brief description of the scenario or situation presented in the video.
        2. **Objectives/Purpose:** What the video intends to address or achieve.
        3. **Main Points:** Main arguments, ideas, or facts presented in the video, detailed point by point.
        4. **Relevant Details:** Information, examples, and data that support the main points.
        5. **Conclusion:** The final message, implications, or results derived from the video.
        6. **Recommendations/Implications (when applicable):** Suggestions or recommended actions presented in the video.

        Do not include additional information or comments beyond the items requested.

        Text:
        {text}
      """
    )
    print(response.text)

    # Garante que a pasta "summary" exista
    os.makedirs("summary", exist_ok=True)

    # Extrai apenas o nome do arquivo original e gera um nome para o resumo
    original_filename = os.path.basename(path)           # Ex: "video.m4a"
    summary_filename = f"summary_{original_filename.replace('.m4a', '.md')}"  # Ex: "summary_video.md"
    summary_path = os.path.join("summary", summary_filename)

    # Salva o resumo no arquivo .md
    with open(summary_path, "w", encoding="utf-8") as f:
        f.write(response.text)