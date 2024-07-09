#CHECK THE TRINGLE IS EQUILATERAL , ISOSCELES , OR SCALENE#
a=int(input("Enter the length of a: "))
b=int(input("Enter the length of b: "))
c=int(input("Enter the length of c: "))
if a==b==c:
    print("Equilateral Tringle")
elif (a==b) or (a==c) or (b==c):
    print("Isosceles Tringle")
else:
    print("Scalene Tringle")