import os,time
os.system('clear')
os.system('figlet FB-KING |lolcat')
print(47*'-')
print('')
print(f' [01] FILE  CLONING [M1]')
print(f' [02] FILE  CLONING [M2]')
print(47*'-')
A=input(f' >>> Choose Menu :')
if A in ["1","01"]:
    import FILE-BD
elif A in ["2","02"]:
    import FILE-OK
else:
    print('Dhur Halar Put 1&2 Input Kor😾')
    time.sleep(7)
    exit()
