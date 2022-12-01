import os,time
A='\033[1;31m'
B='\033[1;32m'
C='\033[1;37m'
os.system('clear')
print(f" \n    {B}[{A}+{B}]Instaling  Module figlet{A}....{B}\n ")
os.system("pkg install figlet -y")
os.system('clear')
os.system('figlet FB-KING |lolcat')
print(47*'-')
print(f' {C}[{B}01{C}] {B}FILE  CLONING {A}[{B}M1{A}]')
print(f' {C}[{B}02{C}] {B}FILE  CLONING {A}[{B}M2{A}]{C}')
print(47*'-')
A=input(f' {A}>>> {B}Choose Menu :')
if A in ["1","01"]:
    import FILEBD
elif A in ["2","02"]:
    import FILEOK
else:
    print('  \033[1;32mDhur Halar Put 1&2 Input Kor😾')
    time.sleep(7)
    exit()
