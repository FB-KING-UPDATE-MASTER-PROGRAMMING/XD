import os,time
os.system('clear')
os.system('figlet FB-KING |lolcat')
print(47*'-')
print('')
print(f' [01] FILE   CLONING [m1]')
print(f' [02] FILE   CLONING [m2]')
print(47*'-')
A=input(f' >>> Choose Menu :')
if A in ["1","01"]:
    import FILE1
elif A in ["2","02"]:
    import FILE2
else:
    print('Dhur Halar Put 1&2 Input Kor😾')
    time.slep(7)
    exit()
