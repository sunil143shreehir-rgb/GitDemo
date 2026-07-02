import subprocess
import pyautogui
import time

# Open Microsoft Teams
#subprocess.Popen(r"C:\Users\SSD\AppData\Local\Microsoft\Teams\Update.exe --processStart Teams.exe")
subprocess.run("start ms-teams:", shell=True)
time.sleep(10)  # wait for Teams to load

# Open search bar
pyautogui.hotkey('ctrl', 'e')

time.sleep(1)

# Type person's name
pyautogui.write("Sunil")

time.sleep(2)

# Open chat
pyautogui.press("enter")

time.sleep(2)

# Type message
pyautogui.write("Hello Sunil, this is an automated message.")

# Send message
pyautogui.press("enter")
