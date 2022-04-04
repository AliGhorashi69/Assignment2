
while True:
    second=int(input("please enter a time based on seconds"))
    if second<0:
        print("please enter a valid number")
    else:
     break

h=int(second/3600)

m= int((second - h*3600)/60)

s=second-h*3600- m*60

print("your time is: ", h, ":",m,":",s)