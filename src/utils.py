import unicodedata
import re

def parametrize_title(title: str) -> str:
  title_parametrize = unicodedata.normalize('NFKD', title)
  title_without_accent = title_parametrize.encode('ASCII', 'ignore').decode('ASCII')
  clean_title = re.sub(r'[^A-Za-z0-9\s]', '', title_without_accent)
  return clean_title.replace(" ", "_").lower()
