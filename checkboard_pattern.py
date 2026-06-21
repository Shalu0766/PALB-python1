 n = int(input("enter the length of pattern :"))
 for i in range(n):
   for j in range(n):
      if (i + j) % 2 == 0:
        print("*", end=" ")
      else:
         print(" ", end=" ")
 print()
