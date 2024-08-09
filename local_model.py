SORU = "Bitcoin Nedir?"
SYSTEM_PROMPT = """Sen türkçe konuşan bir asistansın. Kullanıcının sorduğu soruları cevapla. Asla ingilizce cevap verme. Sadece Türkçe cevapla."""

from gpt4all import GPT4All
from pathlib import Path

def get_model(model_name):
    return GPT4All(model_name=model_name, model_path= './' ,allow_download=False, device='cuda')
