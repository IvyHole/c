def LEAP_YEAR(y):
    if y%4==0:
        return 'L'
    else :
        return 'N'

y=int(input())
print(LEAP_YEAR(y))
