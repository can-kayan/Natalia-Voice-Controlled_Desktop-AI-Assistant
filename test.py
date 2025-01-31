import os
import wave
import json
import sys  
# Vosk modelini yükleyin (Türkçe model)
from tts import save

text = "Hello, World!"
language = "en"  # Specify the language (IETF language tag)
output_file = "konusma.mp3"  # Specify the output file (only accepts .mp3)

save(text, language, file=output_file)