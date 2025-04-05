import os
import time
import torch
from faster_whisper import WhisperModel
from tqdm import tqdm

def transcribe_audio(audio_path):
    transcription_path = audio_path.replace(".m4a", ".txt")
    
    if os.path.exists(transcription_path):
        print(f"✅ Transcrição já realizada em: {transcription_path}")
        with open(transcription_path, "r", encoding="utf-8") as f:
            return f.read()

    # Define o dispositivo: "cuda" se houver GPU, senão "cpu"
    device = "cpu"
    # Escolhe o tipo de computação: FP16 na GPU para otimizar e INT8 na CPU
    compute_type = "int8"

    model = WhisperModel("large-v3", device=device, compute_type=compute_type)
    
    # Inicia o timer
    start_time = time.time()

    # Transcreve o áudio e captura as informações
    segments, info = model.transcribe(audio_path, beam_size=5, language="pt")
    total_duration = info.duration if info.duration else 0

    # Se a duração total estiver disponível, inicializa a barra de progresso
    progress_bar = tqdm(total=total_duration, unit='s', desc="Transcrevendo") if total_duration > 0 else None
    
    transcription_text = ""
    for segment in segments:
        transcription_text += segment.text.strip() + " "
        
        if progress_bar:
            # Atualiza a barra de progresso com a duração do segmento
            progress_bar.update(segment.end - segment.start)
            
            # Cálculo do progresso baseado no tempo já processado / tempo total
            progress_ratio = segment.end / total_duration if total_duration else 0
            elapsed_time = time.time() - start_time
            # Estima o tempo total (supondo ritmo constante) e tempo restante
            estimated_total_time = elapsed_time / progress_ratio if progress_ratio > 0 else 0
            remaining_time = estimated_total_time - elapsed_time
            
            # Exibe progresso e tempo restante estimado
            tqdm.write(f"Progresso: {progress_ratio*100:.2f}% - Tempo restante estimado: {remaining_time:.2f} s")

    if progress_bar:
        progress_bar.close()

    # Salva a transcrição em um arquivo .txt
    with open(transcription_path, "w", encoding="utf-8") as f:
        f.write(transcription_text.strip())

    return transcription_text.strip()
