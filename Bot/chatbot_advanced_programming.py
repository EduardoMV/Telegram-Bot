import telebot
import autobot
import pyautogui
from playsound import playsound
from gtts import gTTS 
import subprocess

bot_token = "1576277547:AAFjX5ZAae1J1oGH3umvTMDt_iusUxL7o4s"
bot = telebot.TeleBot(token=bot_token)

sonido_generado = open("gruñido.mp3", "rb")

orderFile = open("orders.txt", "r")
to_do_list = orderFile.read().split("\n")
orderFile.close()  

#commands = {
    #"hola": ["hola", "hello", "hi",]
#}

#memory = open("to_do_list.txt", "r")
#to_do_list = memory.read().split("\n")
#memory.close()

@bot.message_handler()
def initial_step(message):
    content = message.text.lower()

    #global idioma
    #idioma = "es"

    if content.find("lista de lenguas") != -1:
        answer = "Los idiomas son:\naf: Afrikaans\nar: Arabic\nbn: Bengali\nbs: Bosnian\nca: Catalan\ncs: Czech\ncy: Welsh\nda: Danish\nde: German\nel: Greek\nen: English\neo: Esperanto\nes: Spanish\net: Estonian\nfi: Finnish\nfr: French\ngu: Gujarati\nhi: Hindi\nhr: Croatian\nhu: Hungarian\nhy: Armenian\nid: Indonesian\nis: Icelandic\nit: Italian\nja: Japanese\njw: Javanese\nkm: Khmer\nkn: Kannada\nko: Korean\nla: Latin\nlv: Latvian\nmk: Macedonian\nml: Malayalam\nmr: Marathi\nmy: Myanmar (Burmese)\nne: Nepali\nnl: Dutch\nno: Norwegian\npl: Polish\npt: Portuguese\nro: Romanian\nru: Russian\nsi: Sinhala\nsk: Slovak\nsq: Albanian\nsr: Serbian\nsu: Sundanese\nsv: Swedish\nsw: Swahili\nta: Tamil\nte: Telugu\nth: Thai\ntl: Filipino\ntr: Turkish\nuk: Ukrainian\nur: Urdu\nvi: Vietnamese\nzh-CN: Chinese\nzh-TW: Chinese (Mandarin/Taiwan)\nzh: Chinese (Mandarin)"
        bot.reply_to(message, answer)

    if content.find("add element") != -1:
        #add element: Do homework
        parts = content.split(":")
        name = parts[1]
        to_do_list.append(name)

        answer = "Element has been created"
        bot.reply_to(message, answer)

    elif content.find("clear") != -1:
        del to_do_list[:]
        answer = "List has been deleted"
        bot.reply_to(message, answer)

    elif content.find("view list") != -1:
        nombres = ""
        index = 0
        for element in to_do_list:
            nombres = nombres + "\n" + str(index) + ".-" + element 
            index = index + 1
        
        answer = "Your current list is:\n" + nombres
        bot.reply_to(message, answer)

    elif content.find("delete") != -1:
        #delete 15
        try:
            parts = content.split(" ")
            index_to_delete = int(parts[1])
            to_do_list.pop(index_to_delete)

            answer = "Your element has been deleted"
            bot.reply_to(message, answer)
        except:
            answer = "An error has ocurred"
            bot.reply_to(message, answer)

    elif content.find("edit") != -1:
        #edit 7 : new value
        words = content.split(" ")
        index_to_update = int(words[1])

        parts = content.split(":")
        new_value = parts[1]
        to_do_list[index_to_update] = new_value
        answer = "Your element has been updated"
        bot.reply_to(message, answer)

    if content.find("hello") != -1 and content.find("hablar") == -1:
        answer = "Hello world, hello sunshine"
        bot.reply_to(message, answer)

    elif content.find("hi") != -1:
        answer = "Hi! :D"
        bot.reply_to(message, answer)

    elif content.find("hola") != -1 and content.find("hablar") == -1:
        answer = "Hola! :D"
        bot.reply_to(message, answer)

    if content.find("thanks") != -1:
        answer = "You're welcome my friend!"
        bot.reply_to(message, answer)

    elif content.find("thank you") != -1:
        answer = "You're welcome my friend!"
        bot.reply_to(message, answer)

    elif content.find("gracias") != -1:
        answer = "No hay de que"
        bot.reply_to(message, answer)
    
    elif content.find("run") != -1:
        autobot.runOrders()
    
        answer = "Command running"
        bot.reply_to(message, answer)

    elif content.find("save") != -1: 
        orderFile = open("orders.txt", "w")
        orderFile.write("\n".join(to_do_list))

        answer = "Your list has been saved"
        bot.reply_to(message, answer)

    elif content.find("screenshot") != -1 or content.find("scrn") != -1:
        new_image = pyautogui.screenshot("auto_screenshot.png")
        new_image.save("auto_screenshot.png")

        new_image = open("auto_screenshot.png", "rb")
        bot.send_document(message.chat.id, new_image)

    #elif content.find("idioma") != -1:
        #idioma = content.split(": ")[1]
        #print(idioma)

        #answer = "Idioma actualizado"
        #bot.reply_to(message, answer)

    elif content.find("hablar") != -1:
        #hablar: idioma: mensaje

        try:
            txt_to_transform = content.split(": ")[2]
            idioma = content.split(": ")[1]

            tts = gTTS(txt_to_transform, lang= idioma)
            sound_file = open("eduardo.mp3", "wb")
            tts.write_to_fp(sound_file)
            sound_file.close()
        
            sound_file = open("eduardo.mp3", "rb")
            bot.send_document(message.chat.id, sound_file)
            
        except:
            answer = "Idioma no reconocido"
            bot.reply_to(message, answer)

    #elif content.find("Nombre") != -1:

        #tts = gTTS("Nombre", lang= "es")
        #sound_file = open("eduardo.mp3", "wb")
        #tts.write_to_fp(sound_file)
        #sound_file.close()
     
        #sound_file = open("eduardo.mp3", "rb")
        #bot.send_document(message.chat.id, sound_file)

    #if content.find("Nombre") != -1: 

        #answer = "BLABLABLA"
        #bot.reply_to(message, answer)
        
    

    #memory = open("to_do_list", "w")
    #memory.write("\n".join(to_do_list))
        
bot.polling()