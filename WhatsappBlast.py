# Cara Install PIP di python 3.11
# python -m pip install pywhatkit
# python -m pip install flask
# python -m pip install pyautogui
# Contoh Cara menjalankan di cmd = py flower.py

import pywhatkit
import pyautogui
import time
# Blast message Whatsapp
# Format whatsapp nomor whatsapp + isi pesan + jam +menits
pywhatkit.sendwhatmsg("+6283127048901","halo Saya Mas Mutaqin",10,7)
time.sleep(1)
pyautogui.click()
time.sleep(1)
pyautogui.press('enter')