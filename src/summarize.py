import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def summarize_text(text, path):
  client = genai.Client(api_key=os.getenv("GEMINI_KEY"))
  response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=f"""
    Contexto: Vou fornecer a transcrição de um vídeo. Sua tarefa é elaborar um resumo que não apenas destaque os pontos principais e as conclusões do vídeo, mas que também explique e esclareça os conceitos, ideias e argumentos apresentados. O objetivo é tornar o conteúdo mais acessível e compreensível para alguém que não assistiu ao vídeo.

    Instruções de Formatação e Conteúdo:

    1. Estrutura:
        - Inclua uma breve introdução para contextualizar o assunto.
        - Resuma os principais tópicos e ideias centrais do vídeo em um corpo de texto bem organizado (use subtítulos ou bullet points, se necessário).
        - Em cada tópico, não apenas resuma o que foi dito, mas também explique os conceitos e argumentos apresentados, detalhando o "como" e o "porquê" para facilitar a compreensão.
        - Finalize com uma conclusão ou insight final que resuma os aprendizados e implicações do vídeo.

    2. Clareza e Objetividade:
        - Utilize linguagem simples e direta.
        - Evite repetições, ruídos de fala e detalhes irrelevantes.

    3. Destaques Importantes:
        - Saliente quaisquer inovações, exemplos práticos, benefícios e desafios mencionados.
        - Inclua, se necessário, implicações ou recomendações destacadas no vídeo.

    4. Tamanho do Resumo:
        - Mantenha o texto em um tamanho razoável, suficiente para transmitir o essencial sem se estender em demasia.

    5. Fidelidade:
        - Garanta que o resumo seja fiel ao que foi dito no vídeo, sem adicionar informações não contidas na transcrição.

    Transcrição do Vídeo:
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