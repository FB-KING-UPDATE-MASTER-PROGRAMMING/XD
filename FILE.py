import os,time
A='\033[1;31m'
B='\033[1;32m'
C='\033[1;37m'
os.system('clear')
print(f" \n    [+]Instaling  Module figlet....\n ")
os.system("pkg install figlet -y")
os.system('clear')
os.system('figlet FB-KING |lolcat')
print(47*'-')
print(f' [01] FILE  CLONING [M1]')
print(f' [02] FILE  CLONING [M2]')
print(47*'-')
A=input(f' \033[1;31m>>> \033[1;32mChoose Menu :')
if A in ["1","01"]:
    import FILEBD
elif A in ["2","02"]:
    import FILEOK
else:
    print('  \033[1;32mDhur Halar Put 1&2 Input Kor😾')
    time.sleep(7)
    exit()
