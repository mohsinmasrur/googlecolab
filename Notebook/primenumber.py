#PRIME NUMBER

n=int(input("enter a number grater than 1: "))
Match=True
for num in range(2,n):
  n%num
  if n%num==0:
    Match=False


if Match:
  print("num is prime")
else:
  print("num is not prime")