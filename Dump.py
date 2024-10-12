import os, platform, time, sys
print('\033[1;97m [❥] join Whatsapp Group')
os.system('xdg-open https://chat.whatsapp.com/FcQmyk9IVEhIwu3b7rGBfQ')
os.system('clear')
print('\033[1;97m [❥] Checking For Update...')
os.system('git pull --quiet 2>/dev/null')
os.system('clear')
bit = platform.architecture()[0]
if bit == '64bit':
   print('\033[1;97m [✓] Found 64 Bit Device')
   import Dump
elif bit == '32bit':
   print('\033[1;97m [✓] Found 32 Bit Device')
   import Dump32
