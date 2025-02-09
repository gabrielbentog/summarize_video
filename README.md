# 🎵 YouTube Audio Downloader, Transcriber & Summarizer

Este projeto permite baixar o áudio de vídeos do YouTube (ou playlists inteiras), transcrever o conteúdo utilizando o modelo **Whisper** e gerar um resumo estruturado em **Markdown** com a API do **Google GenAI**. O resumo destaca os principais pontos do vídeo em português.

---

## ✨ Funcionalidades

- 🎧 **Download de Áudio:** Baixa o áudio de vídeos individuais ou de playlists inteiras.
- 📝 **Transcrição Automática:** Converte o áudio em texto usando o **Whisper**.
- 📑 **Geração de Resumos:** Cria um resumo detalhado em Markdown com os seguintes tópicos:
  - **📌 Contexto:** Descrição breve do cenário apresentado no vídeo.
  - **🎯 Objetivos/Propósito:** O que o vídeo pretende abordar ou alcançar.
  - **🔑 Principais Pontos:** Ideias, argumentos e fatos principais do vídeo.
  - **📊 Detalhes Relevantes:** Exemplos, dados e informações que sustentam os pontos principais.
  - **🛑 Conclusão:** Mensagem final ou implicações do conteúdo.
  - **💡 Recomendações/Implicações:** Sugestões ou ações recomendadas (quando aplicável).
- 🖋 **Saída em Markdown:** Os resumos são salvos como arquivos `.md`, facilitando leitura e compartilhamento.

---

## ⚙️ Pré-requisitos

### 📌 Requisitos do Sistema
- **Python 3.7+**
- **FFmpeg:** Necessário para processar e converter áudio/vídeo.
  - No Windows: Baixe e instale o FFmpeg através do site oficial: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)  
  - No Linux/macOS: Instale via gerenciador de pacotes:  

    - **Ubuntu/Debian:** `sudo apt install ffmpeg`
    - **MacOS (Homebrew):** `brew install ffmpeg`
    - **Windows (Chocolatey):** `choco install ffmpeg`
- **Bibliotecas Python:**  
  Instale as dependências com o comando:

  pip install -r requirements.txt

  Caso o arquivo `requirements.txt` não esteja disponível, instale manualmente:

  pip install pytubefix whisper torch python-dotenv google
- **
### 🔑 Configuração da API do Google GenAI
Crie um arquivo `.env` na raiz do projeto e adicione sua chave de API:

GEMINI_KEY=your_gemini_api_key_here

---

## 🚀 Como Usar

### 🎥 Processando um Vídeo Único
1. **Configure a URL do vídeo**  
   No arquivo `main.py`, altere a variável `url` para o vídeo desejado:

   url = "https://www.youtube.com/watch?v=SEU_VIDEO_ID"

2. **Execute o script**  

   python main.py

3. **Resultados:**  
   - O áudio será salvo na pasta `temp/`
   - A transcrição será salva no mesmo diretório (`.txt`)
   - O resumo gerado será salvo na pasta `summary/` (`.md`)

### 📺 Processando uma Playlist
1. **Configure a URL da Playlist**  
   No arquivo `playlist_script.py`, edite a variável `url`:

   url = "https://www.youtube.com/watch?v=SEU_VIDEO_ID&list=SUA_PLAYLIST_ID"

2. **Execute o script**  

   python playlist_script.py

3. **Resultados:**  
   - Uma pasta será criada dentro de `temp/` para armazenar os arquivos.
   - Cada vídeo terá seu áudio, transcrição e resumo gerados individualmente.

---

## 📂 Saída dos Arquivos

- **🎧 Áudio:** Salvo na pasta `temp/`, nomeado conforme o título do vídeo.
- **📜 Transcrição:** Salvo no mesmo diretório do áudio, com extensão `.txt`.
- **📑 Resumo:** Salvo na pasta `summary/`, nomeado como `summary_<nome_do_arquivo>.md`.

---

## 🔧 Personalizações

### ✏️ Ajustando o Prompt de Resumo
Para modificar a estrutura do resumo, edite o prompt em `summarize.py`.

### 🎙️ Configurações do Whisper
Caso queira alterar parâmetros como o modelo ou idioma, modifique `transcription.py`.

---

## ❗ Possíveis Problemas & Soluções

### ❌ Chave de API Inválida ou Ausente
- Verifique se o arquivo `.env` está presente e se a variável `GEMINI_KEY` está configurada corretamente.

### 🔄 Erros de Dependências
- Certifique-se de que todas as bibliotecas necessárias estão instaladas e atualizadas.

### ⚠️ Falha no Download do Áudio
- Confira sua conexão com a internet e a validade do URL do vídeo/playlist.

---

## 🤝 Contribuições

Contribuições são bem-vindas!  
Se encontrar algum problema ou quiser melhorar o projeto, sinta-se à vontade para **abrir uma issue** ou **enviar um pull request**. 🚀

---
