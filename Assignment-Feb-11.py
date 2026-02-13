# 16. Check for Palindrome String

str1=input("Enter a string:").lower()

rev=str1[::-1]
if str1==rev:
    print("Palindrome")
else:
    print("Not a Palindrome")

# OUTPUT:
# Enter a string:Madam
# Palindrome

#using for loop:

str1=input("Enter a string:").lower()
rev=""

for ch in str1:
    rev=ch+rev
if rev==str1:
    print("Palindrome")
else:
    print("Not a palindrome")

# OUTPUT:
# Enter a string:Madam
# Palindrome

#using while loop:
str1=input("Enter a string:").lower()
rev=""
i=len(str1)-1

while i>=0:
    rev=str1[i]+rev
    i-=1
if rev==str1:
    print("Palindrome")
else:
    print("Not a palindrome")


# OUTPUT:
# Enter a string:Madam
# Palindrome

# 17. Sum of Digits

num=int(input("Enter a number :"))
sum_dig=0

while num>0:
    sum_dig+=num%10
    num//=10
print("Sum of digits =",sum_dig)

# OUTPUT:
# Enter a number :123
# Sum of digits = 6

# 18. Product of Digits

num=int(input("Enter a number :"))
prod_dig=1

while num>0:
    prod_dig*=num%10
    num//=10
print("Sum of digits =",prod_dig)

# OUTPUT:
# Enter a number :235
# Sum of digits = 30

# 19. Armstrong Number Check

num=int(input("Enter armstrong number:"))
temp=num
sum_digits=0
power=len(str(num))
while temp>0:
    digit=temp%10
    sum_digits+= digit**power
    temp//=10
if sum_digits==num:
    print("Armstrong number")
else:
    print("not an Armstrong number")

# OUTPUT:
# Enter armstrong number:153
# Armstrong number

# 20. Reverse a Number

num=int(input("Enter a number:"))
rev_num=0

while num>0:
    digit=num%10
    rev_num=rev_num*10+digit
    num//=10
print("Reversed number:",rev_num)

# OUTPUT:
# Enter a number:1234
# Reversed number: 4321


