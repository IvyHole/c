import time,os
count = 0
a = input("time(min):")
b= a*60
while ( count < b):
    i = os.system("cls")
    ncount = b -count
    print ncount
    time.sleep(1)
    count +=1
print '\done'
