#1 write a  function to check whether a number is positive or negative. 

#def check_number(num):
 #   if num > 0:
  #      print("Positive")
   # elif num < 0:
    #    print("Negative")
    # else:
       # print("Zero")
#check_number(10)


#2 write a  function to check whether a number is  even or odd

#def check_even_odd(num):

 #   if num % 2 == 0:
  #      print("Even")
   # else:
    #    print("odd")
#check_even_odd(235)




#3write a function that accept two number or retruns the greater number 

#def greater_number(num1, num2):
 #   if num1 > num2:
  #      print("num1")
   # else:
    #    print("num2")

#greater_number(num1=8 , n



#4 check whether a person is eligible to vote (age ≥ 18)
#def check(age):
 #   if age >= 18:
  #      print("Eligible to vote")
   # else:
    #    print("Not eligible to vote")
#check(17)


#5 check whether a number is divisible by 5

#def check_divisible(num):
 #   if num % 5 == 0:
  #      print("Divisible by 5")
   # else:
    #    print("Not divisible by 5")
#check_divisible(15)



#6 check whether a given year is a leap year or not

#def check_leap_year(year):
 #   if (year % 4 == 0):
  #      print("Leap Year")
   # else:
    #    print("Not a Leap Year")

#check_leap_year(2026)


#7 check whether a character is a vowel or a consonant.

#def check(ch):
#    if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
 #       print("Vowel")
  #  else:
   #     print("Consonant")

#check('z')



# 8 the largest among three numbers.

#def check  (a, b, c):
 #   if a >= b and a >= c:
  #      print("Largest number is:", a)
   # elif b >= a and b >= c:
    #    print("Largest number is:", b)
    #else:
     #   print("Largest number is:", c)
#check(6,7,8)



# 9 function to calculate the sum of 1 to 100

#def sum_numbers():
 #   sum= 0
  #  for i in range(1, 101):
   #     sum = sum+ i
    #print("Sum =", sum)

#sum_numbers()


# 10 Write a function that prints the multiplication table of a given number

#def multiplication (num):
 #   for i in range(1, 11):
  #      print(num, "x", i, "=", num * i)
#
#multiplication (9)


# 11 Write a function to calculate and return the square of a number

#def cal(num):
 #   sq = num * num
  #  print(sq)

#num = int(input("Enter a number: "))
 # cal(num)




#12 Write a function to calculate the factorial of a number using a loop 

#def fact (num):
 #   fact = 1
  #  for i in range(1, num + 1):
   #     fact = fact * i
    #print(fact)

#n = int(input("Enter a number: "))
#fact (n)



# 13 Write a function to check whether a number is prime

#def prime(num):
 #   for i in range(2, num):
  #      if num % i == 0:
   #         print("Not Prime")
   # else:
    #    print("Prime")

#n = int(input("Enter a number: "))
#prime(n)


# 14 Write a function to calculate the sum of digits of a number

#def summ(num):
 #   num = abs(num)
  #  total = 0

   # while num > 0:
     #   total += num % 10
      #  num //= 10

    #return total
#print(summ(10))   
#print(summ(123))  



# 15 Write a function that accepts a number n and returns the sum of all numbers from 1 to n

#def summ(num):
 #   num = abs(num)
  #  total = 0

   # while num > 0:
    #    total += num % 10
     #   num //= 10

    #return total
#print(summ(10))   
#print(summ(1356))  



 # 16 Create a list of 10 numbers and print all the elements

#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#for num in numbers:
 #   print(num)




# 17 Write a program to find the largest element in a list
#numbers = [82, 90, 7, 4, 9, 6, 3]
#largest = max(numbers)
#print("Largest element:", largest)



# 18 Write a program to find the smallest element in a list
#numbers = [10 , 23 , 45, 87 , 98]
#smallest = min(numbers)
#print("Smallest element:", smallest)


# 19 Write a program to calculate the sum of all elements in a list
#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100]
#sum = sum(numbers)
#print("Sum of all elements:", sum)



# 20 Write a program to calculate the average of all elements in a list
#numbers = [11, 12, 13, 14, 15, 16, 17, 18, 19,200]
#average = sum(numbers) /len(numbers)
#print("Average of all elements:", average)


# 21 Write a program to count how many even numbers are present in a list
#numbers = [8, 67, 765,789,43,0]
#ount = 0
#for num in numbers:
 #   if num % 2 == 0:
  #      count += 1
#print("Number of even elements:", count)



# 22 Write a program to create a new list containing only the odd numbers from an existing list
#numbers = [87, 89,64,756,33,22,45,66,80]
#odd = []
#for num in numbers:
 #   if num % 2 != 0:
  #      odd.append(num)
#print("Odd numbers:", odd )



# 23 Write a program to find whether a given element exists in a list
#numbers = [12, 45, 7, 89, 34, 56, 23]
#element = 34
#if element in numbers:
 #   print(element, "exists in the list.")
#else:
 #   print(element, "does not exist in the list.")



# 24 Write a program to reverse a list without using built-in reverse functions
#numbers = [56, 89,76,43,27,91,22]
#reversed_list = []
#for i in range(len(numbers) - 1, -1, -1):
 #   reversed_list.append(numbers[i])
#print("Original List:", numbers)
#print("Reversed List:", reversed_list)



# 25 Write a program to find the second largest element in a list
#numbers = [57, 78,34,90,66,45]
#largest = second = float('-inf')

#for num in numbers:
 #   if num > largest:
  #      second = largest
   #     largest = num
    #elif num > second  and num != largest:
     #   second= num
#print("Second largest element:", second )



# 26 Create a dictionary to store a student's name, age, and city, and print the dictionary
#student =("name:pooja","age:18","city:pune")
#print(student)



# 27 Write a program to print all the keys of a dictionary
#student = {"name":"pooja", "age":18, "city":"pune"}
#print(student.keys())



# 28 Write a program to print all the values of a dictionary
#student = {"name":"pooja", "age":18, "city":"pune"}
#print(student.values())



# 29 Write a program to add a new key-value pair to an existing dictionary
#student = {"name":"pooja", "age":18, "city":"pune"}
#student["course"] = "Diploma"
#print(student)



# 30 Write a program to check whether a given key exists in a dictionary
#if "age" in student:
 #   print("Key exists")
#else:
 #   print("Key does not exist")


# 31 Write a program to remove a key-value pair from a dictionary
#student = {"name":"pooja", "age":18, "city":"pune"}
#del student["age"]
#print(student)


# 32 Write a program to count the total number of key-value pairs in a dictionary
#student = {"name":"pooja", "age":18, "city":"pune"}
#print(len(student))



# 33 Write a program to iterate through a dictionary and print all keys and their corresponding values 
#student = {"name":"pooja", "age":18, "city":"pune"}
#for key, value in student.items():
 #  print(key, ":", value)



# 34 Create a dictionary of student names and marks, then find the student with the highest marks
#student = {"pooja":85, "Riya":92, "Neha":78}
#highest = max(student, key=student.get)
#print("Student with highest marks:", highest)
#print("Marks:", student[highest])