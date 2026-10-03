age = 950
hgt = 7.1
cmplx = 1 + 3j

bse = float(input("Enter Base : "))
hgt2 = float(input("Enter height : "))
area = 0.5 * bse * hgt2
print("Area of triangle is : ", area)

sdea = float(input("Enter side a : "))
sdeb = float(input("Enter side b : "))
sdec = float(input("Enter side c : "))
print("Perimeter of triangle is : ", sdea + sdeb + sdec)

lgth = float(input("Enter length : "))
wdth = float(input("Enter width : "))
area_rect = lgth * wdth
print("Area of rectangle is : ", area_rect)
print("Perimeter of rectangle is : ", 2 * (lgth + wdth))

rad = float(input("Enter radius : "))
area_circle = 3.14 * rad * rad
print("Area of circle is : ", area_circle)
print("Circumference of circle is : ", 2 * 3.14 * rad)

xintcpt = float(input("Enter x-intercept : "))
yintcpt = float(input("Enter y-intercept : "))
eqn = (2 * xintcpt) - 2 
print("Slope of the line is : ", eqn)

pnta1 = 2
pnta2 = 2
pntb1 = 6
pntb2 = 10
slp = (pntb2 - pnta2) / (pntb1 - pnta1)
print("Euclidean Distance between the points A and B is : ", ((pntb1 - pnta1) ** 2 + (pntb2 - pnta2) ** 2) ** 0.5)
print("Slope of the line is : ", slp)

print("The difference between the slopes of the two lines is : ", abs(slp - eqn))

xval = float(input("Enter x value : "))
yval = xval ** 2 + 6 * xval + 9
print("The value of y is : ", yval)
print("For Y to be 0, x should be : ", (-6 + (36 - 4 * 9) ** 0.5) / 2)

print("The length of python is : ", len("python"))
print("The length of dragon is : ", len("dragon"))
print("The length of python and dragon is equal : ", len("python") == len("dragon"))
if "on" in "python" and "on" in "dragon":
    print("Yes, 'on' is found in both 'python' and 'dragon'")

sntnce = "I hope this course is not full of jargon."
if "jargon" in sntnce:
    print("Yes, 'jargon' is found in the sentence")

if "on" in "python" and "on" in "dragon":
    print("Yes, 'on' is found in both 'python' and 'dragon'")

print("The length of python is : ", len("python"), "now the length of python in float is : ", float(len("python")), "and now the length of python in string is : ", str(len("python")))

rndNum = float(input("Enter a number : "))
if rndNum % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")

print("The floor division of 7 by 3 is : ", 7 // 3)

print("The type of '10' is : ", type('10'), "and the type of 10 is : ", type(10))

print("The int('9.8') is : ", int(float('9.8')))

hrs = float(input("Enter hours : "))
rate = float(input("Enter rate per hour : "))
print("Your weekly earning is : ", hrs * rate)

yrs = float(input("Enter number of years you have lived : "))
print("You have lived for : ", yrs * 365 * 24 * 60 * 60, "seconds")

tup = [[1, 1, 1, 1, 1],
       [2, 1, 2, 4, 8],
       [3, 1, 3, 9, 27],
       [4, 1, 4, 16, 64],
       [5, 1, 5, 25, 125]]
print("The table is : ")
for i in tup:
    print(i)