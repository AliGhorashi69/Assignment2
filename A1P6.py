
n=int(input("Enter the size of fibonacci serie: "))
 
serie=[]
 

i=0

while n>i:
  
  if i==0:
   serie.append(1)
   
   
  elif i==1:
   serie.append(1)
   
  else:
      
      a=serie[i-1]
      b=serie[i-2]
      serie.append(a+b)
  i=i+1

  



print("The serie ia:" , serie)