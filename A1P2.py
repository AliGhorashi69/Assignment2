
from re import S


while True:
    h=int(input("plase enter hour: "))
    if h>24 or h<0:
        print("Invalid number, please insert correct number for hour")
    else:
        break

while True:
    m=int(input("plase enter minute: "))
    if m>60 or h<0:
        print("Invalid number, please insert correct number for minute")
    else:
        break

 

while True:
    s=int(input("plase enter second: "))
    if s>60 or s<0:
        print("Invalid number, please insert correct number for second")
    else:
        break

        

time=3600*h + 60*m+ S

print ("The total time to S is: ", time)
