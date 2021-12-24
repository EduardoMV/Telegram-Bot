from playsound import playsound
from gtts import gTTS 
import subprocess

#Para generar un archivo hazlo con el formato "Introduce_algo.mp3"
saludo = "sonido_generado.mp3"

tts = gTTS("Grrrr, gruñido de ogro", lang="es")
tts_afrikaans = gTTS("Hallo, ek wil sê dat ek van Paloma hou", lang="af")
tts_arabic = gTTS("مرحباً ، أريد أن أقول إنني أحب بالوما", lang="ar")
tts_bengali = gTTS("হ্যালো, আমি বলতে চাই যে আমি পালোমাকে ভালবাসি", lang="bn")
tts_bosnian = gTTS("Pozdrav, želim reći da volim Palomu", lang="bs")
tts_catalan = gTTS("Hola, vull dir que estimo Paloma", lang="ca")
tts_czech = gTTS("Dobrý den, chci říct, že miluji Palomu", lang="cs")
tts_welsh = gTTS("Helo, rwyf am ddweud fy mod yn caru Paloma", lang="cy")
tts_ingles = gTTS("Hello, I want to say that I love Paloma", lang="en")
tts_frances = gTTS("Bonjour, je veux dire que j'aime Paloma", lang="fr")
tts_chino = gTTS("嗨，爸爸，让我们看看您的汉堡是否很好", lang="zh-cn")

with open(saludo, "wb") as archivo:
    tts.write_to_fp(archivo)
    #tts_afrikaans.write_to_fp(archivo)
    #tts_arabic.write_to_fp(archivo)
    #tts_bengali.write_to_fp(archivo)
    #tts_bosnian.write_to_fp(archivo)
    #tts_catalan.write_to_fp(archivo)
    #tts_czech.write_to_fp(archivo)
    #tts_welsh.write_to_fp(archivo)
    #tts_ingles.write_to_fp(archivo)
    #tts_frances.write_to_fp(archivo)
    tts_chino.write_to_fp(archivo)

playsound(saludo)