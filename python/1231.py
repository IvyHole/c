a,b=input().split()
From,to=input().split()
a=int(a)
b=int(b)
From=int(From)
to=int(to)
rouna=a
rounb=b
p=1
i=1
c=0
x=1
rounc=c
if From==to:
    print('1')
elif From<to:
    if (From+a+b) !=to:
         while 1==1:
            while (From+a+b) !=to:
                if c==0:
                    c=c+1
                b=rounb*p
                p=p+1
                c=c+1

                if b>100 or b<0:
                    c=rounc
                    b=rounb
                    p=1
                    break
            if(From+a+b) == to:
                break
            a=rouna*i
            i=i+1
            c=c+1
            rounc=c

            print('')
            if a>100 or a<0:
                c=0
                a=rouna
                b=rounb
                i=0
                break
         if c == 0:
             rounc=c
             if (From+a-b) != to:
                 while 1==1:
                     if c==0:
                         c=c+1
                     while (From+a-b) !=to:
                         b=rounb*p
                         p=p+1
                         c=c+1
                        
                         if b>100 or b<0:
                             c=rounc
                             b=rounb
                             p=1
                             break
                     if(From+a-b) == to:
                          break
                     a=rouna*i
                     i=i+1
                     c=c+1
                     rounc=c
                     if a>100 or a<0:
                          c=0
                          
                          break
                 if c==0:
                     print('Error')
                 else:
                     print(c-1)
             else:
                 print(c+2)
         else:
             print(c+1)
    else:
        print(c+2)
elif From >to:
    if (From-a-b) !=to:
         while 1==1:
            if c==0:
                c=c+1
            while (From-a-b) !=to:
                b=rounb*p
                p=p+1
                c=c+1
                if b>100 or b<0:
                    c=rounc
                    b=rounb
                    p=1
                    break
            if(From-a-b) == to:
                break
            a=rouna*i
            i=i+1
            c=c+1
            rounc=c
            if a>100 or a<0:
                c=0
                a=rouna
                b=rounb
                i=0
                break
         if c==0:
             rounc=c
             if (From-a+b) != to:
                 while 1==1:
                     if c==0:
                         c=c+1
                     while (From-a+b) !=to:
                         b=rounb*p
                         p=p+1
                         c=c+1
                         if b>100 or b<0:
                             c=rounc
                             b=rounb
                             p=1
                             break
                     if(From-a+b) == to:
                          break
                     a=rouna*i
                     i=i+1
                     c=c+1
                     rounc=c
                     if a>100 or a<0:
                          c=0
                          break
                 if c==0:
                     print('Error')
                 else:
                     print(c-1)
             else:
                 print(c+2)
         else:
              print(c+1)
    else:
        print(c+2)


