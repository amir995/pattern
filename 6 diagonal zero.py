a=int(input("Enter a value: "))

for i in range(1,a+1):
  for j in range(1,a+1):
    if i==j:
      print("0",end=" ")
    else:
      print(i,end=" ")
  print()
