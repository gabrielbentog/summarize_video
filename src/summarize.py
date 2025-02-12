import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

def summarize_text(text, path):
  client = genai.Client(api_key=os.getenv("GEMINI_KEY"))
  response = client.models.generate_content(
      model="gemini-2.0-flash",
      contents=f"""
  Gere um resumo detalhado e preciso do conteúdo do vídeo fornecido abaixo, em português do Brasil. O resumo deve ser organizado em Markdown (.md) e incluir títulos e, quando necessário, subtítulos, todos em português. Certifique-se de que o resumo explique claramente o que é dito no vídeo, abordando os pontos principais de forma minuciosa. Estruture o resumo nos tópicos a seguir:

  1. **Contexto:** Descreva brevemente o cenário ou situação apresentada no vídeo.
  2. **Objetivos/Propósito:** Explique o objetivo principal ou a finalidade do vídeo.
  3. **Principais Pontos:** Liste, de forma organizada e em tópicos, os argumentos, ideias e fatos centrais mencionados no vídeo. Caso algum ponto necessite de mais explicação, utilize subtópicos para detalhá-lo.
  4. **Detalhes Relevantes:** Destaque informações, exemplos e dados que reforcem os pontos principais.
  5. **Conclusão:** Resuma a mensagem final, os resultados ou as implicações extraídas do vídeo.
  6. **Recomendações/Implicações (quando aplicável):** Indique sugestões ou ações recomendadas, conforme mencionado no vídeo.

  Incorpore somente as informações solicitadas acima, sem incluir comentários ou informações adicionais.

  Texto:
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