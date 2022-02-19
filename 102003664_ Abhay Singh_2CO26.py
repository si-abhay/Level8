
#------------------------------------QUESTION 1---------------------------------
def fact(n):
  if n == 0 or n == 1:
    return 1;
  
  return n*fact(n-1);

n = int(input("Enter the value of n "));
x = int(input("Enter the value of x "));

sum = 0;
for i in range(0,n+1):
  fac = fact(i);
  power = pow(x,i);
  sum += power/fac;

print(sum);


def checkPrime(n):
  if n == 1:
    return 0
  for i in range(2,n-1):
    if(n%i == 0):
      return 0

  return 1

randomList = []

for i in range(0,100):
  x = ran.randint(100,900)
  randomList.append(x)

print
odd = 0
even = 0
prime = 0

print("Even :");
for i in randomList:
  if i%2 == 0:
    print(i);
    even = even+1;

print("\nOdd :");
for i in randomList:
  if i%2 != 0:
    print(i);
    odd = odd+1;

print("\nPrime :");
for i in randomList:
  if checkPrime(i) != 0:
    print(i);
    prime = prime+1;
print("Total odd numbers are : ",odd)
print("Total even numbers are : ",even)
print("Total prime numbers are : ",prime)

#------------------------------QUESTION 3---------------------------------------


def checkPrime(n):
  if n == 1:
    return 0;
  for i in range(2,n-1):
    if(n%i == 0):
      return 0

  return 1

a = int(input("Enter a "));
b = int(input("Enter b "));

i = a
while i <= b:
  if checkPrime(i) == 1:
    print(" ",i)
  i = i+1


#------------------------------QUESTION 4---------------------------------------

a = []
b = []
m = int(input("Enter the number of elements in list 1 "))
n = int(input("Enter the number of elements in list 2 "))

print("Enter the elements of list 1")
for i in range (0,m):
  x = int(input())
  a.append(x)

print("Enter the elements of list 2")
for i in range (0,n):
  x = int(input())
  b.append(x)

print("Common Elements:")
for i in range (0,m):
  toFind = a[i]
  for j in range (0,n):
    if toFind == b[j]:
      print(toFind)

#------------------------------QUESTION 5---------------------------------------

a = int(input("Enter the year:"))
if a%100==0:
  if a%400==0:
    print("Leap Year")
  else:
    print("Not a Leap Year")
elif a%4==0:
  print("Leap Year")
else:
  print("Not a Leap Year")
  
  
#------------------------------QUESTION 6---------------------------------------

a = int(input("Enter Basic Salary: "))
if a<=10000:
  HRA=0.2*a
  DA=0.8*a
  total=a+HRA+DA
  print("Gross Salary Income: ",total)
elif a>10000 and a<=20000:
  HRA=0.25*a
  DA=0.9*a
  total=a+HRA+DA
  print("Gross Salary Income: ",total)
else:
  HRA=0.3*a
  DA=0.95*a
  total=a+HRA+DA
  print("Gross Salary Income: ",total)
  
#------------------------------QUESTION 7---------------------------------------


password = input("Enter the password : ")

smallLetter = 0
capitalLetter = 0
number = 0
special = 0
length = 0

for char in password:
  length = length + 1
  if char >= '0' and char <= '9':
    number = number + 1
  elif char >= 'a' and char <= 'z':
    smallLetter = smallLetter + 1
  elif char >= 'A' and char <= 'Z':
    capitalLetter = capitalLetter + 1
  else : 
    special = special + 1

flag = 0
if length <= 16 and length >= 6:
  if special >= 1:
    if number >= 1:
      if capitalLetter >= 1:
        if smallLetter >= 1:
          print("Valid Password")
          flag = 1

if flag == 0:
  print("Invalid Password")
  
#------------------------------QUESTION 8---------------------------------------

li = [10,20,30,40,50,60,70,80]

li.append(100)
li.append(200)


print("List after appending 100 and 200")
for i in li:
  print(i)

li.remove(10)
li.remove(30)

print("List after removing 10 and 30")
for i in li:
  print(i)

print("List after sorting in ascending order")
# sorting in ascending order
#using inbuilt function

# li.sort();  

# sorting using sorting algo
n = len(li)
for i in range(n-1):
    for j in range(0, n-i-1):
        if li[j] > li[j + 1] :
            li[j], li[j + 1] = li[j + 1], li[j]

for i in li:
  print(i)

print("List after sorting in descending order")
# Sorting in descending order

# using inbuilt sort

# li.sort(reverse=True)

# using sorting algo
 
for i in range(n-1):
    for j in range(0, n-i-1):
        if li[j] < li[j + 1] :
            li[j], li[j + 1] = li[j + 1], li[j]
for i in li:
    print(i)

#------------------------------QUESTION 9---------------------------------------

D = {
    1: "One",
    2: "Two", 
    3: "Three", 
    4: "Four", 
    5: "Five"
}

D["6"] = "Six"
D.pop(2)

if "6" in D:
  print("6 is present")
else:
  print("6 is not present")

count = 0
for i in D:
  count = count + 1

print("Elements in D are : ",count)

ans = ""

# if i add all the string values
for i in D:
  ans = ans + D[i]

print(ans)

# if i add all the keys
sum = 0
for i in D:
  sum = sum + int(i)

print(sum)


#------------------------------QUESTION 10---------------------------------------

#Que 10(a)-------
def compoundIntrest(p,r,t):
  A=p*pow((1+(r/100)),t)
  return A

p=int(input("Enter Principal amount:"))
r=int(input("Enter interest rate:"))
t=int(input("Enter time:"))
A=compoundIntrest(p,r,t)
print("Final Amount after applying compound interest: ",A)

#Que 10(b)--------

!cp /content/drive/MyDrive/Colab Notebooks (1)/myModule.py
import sys
sys.path.append('/content/drive/MyDrive/Colab Notebooks (1)/myModule.py')

p=int(input("Enter Principal amount:"))
r=int(input("Enter interest rate:"))
t=int(input("Enter time:"))
A=compoundInterest(p,r,t)
print("Final Amount after applying compound interest: ",A)
