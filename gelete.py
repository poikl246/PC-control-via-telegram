import os
import time

time.sleep(5)


os.remove('1.bat')
os.remove('System_win.exe')


try:
    os.remove('C:\Program Files\SystemA\padawan.txt')
    os.remove('C:\Program Files\SystemA\Jedi.txt')
except:
    pass
