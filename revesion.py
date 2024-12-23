# a=10
# b=30
# x=int(input("enter a num1"))
# y=int(input("enter a num1"))

# print(a+b,"\n")
# print(x-y,"\n")
# print("hello supan darling","\n")
# vowels=0
# const=1

# str=input("enter a string")
# for i in str:
#     if  i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
#         vowels=vowels+1
#     else:
#         const=const+1
        
# print(vowels)
# print(const)

# year=int(input("enter a year"))
# if year%4==0 and year%400 or  year%100==0:
#     print("leap year")
# else:
#     print("not leap year")

# num=int(input("enter a number"))
# str=input('enter a string for palindrome')
# revstr=str [::-1]
# if str== revstr:
#     print("palindrome")
# else:
#     print("not palindrome")


num1=int(input("enter a num1"))
num2=int(input("enter a num2"))
for i in range(1,100):
    if  num1%i==0 and num2%i==0:
        max=i
        
print(max)