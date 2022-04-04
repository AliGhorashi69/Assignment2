
n=int(input("please enter the number of student in class: "))

#initialization---------------------------
sum=0
a=0
x=range(n)
score=float(input("please ensert the first score: "))
max=score
min=score
#-------------------------------------------

for i in x[1:n]:
    score=float(input("please ensert the next score: "))
    if score>max:
        max=score
    if score<min:
        min=score
    sum=sum+score

Avg=sum/n

print("the average of the class is: ", Avg, " The maximum score is: ", max, "and the minimum score is: ", min)