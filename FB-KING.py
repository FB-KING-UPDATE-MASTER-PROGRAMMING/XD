import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')

        os.system('xdg-open https://www.facebook.com/FB.KING.MAHIN.NAME.TOH.SONSO')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from file import make
 
        make()
 
 
 
elif bit == "32bit":
 
        from file import make
 
 
        make()
        
