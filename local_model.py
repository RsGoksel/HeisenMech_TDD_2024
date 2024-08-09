SORU = "CP violation nedir?"
SYSTEM_PROMPT = """Sen türkçe konuşan bir asistansın. Kullanıcının sorduğu soruları cevapla. Asla ingilizce cevap verme. Sadece TÜrkçe yaz."""

from gpt4all import GPT4All
from pathlib import Path

def get_model(model_name):
    return GPT4All(model_name=model_name, model_path= './' ,allow_download=False, device='cuda')
    #model = GPT4All(model_name="TRLlama3_Q8_0.gguf", model_path=Path.home() / "Jupyter/ProjectPDF/" ,allow_download=False, device='cuda')
