# You are provided with two numbers A and B. Your task is to add these two numbers. 
A = 10
B = 20
C = A + B
print(C);

# You are given two number first as A and second as B and check if both conditions (A<10 and A>B are satisfied or not with the help of operators.
A = 5
B = 3
if A<10 and A>B:
    print("Both conditions are satisfied")
else:
    print("At least one condition is not satisfied");

# You are given two numbers A and B You need to do the following checks: 1. if both are divisible by 10 console true. 2. 3. if both are not divisible by 10 console false. if one of them only is divisible by 10 console true. Use operator to do this. 
A = 20
B = 30
if A % 10 == 0 and B % 10 == 0:
    print("True")
elif A % 10 != 0 and B % 10 != 0:
    print("False")
else:
    print("True");


#You are provided a four digit number N only. Your task is to print out the last digit of that number. 
N = 1234
last_digit = N % 10
print(last_digit);

#You are provided a four digit number N only. Your task is to print out the first digit of that number. 
N = 1234
first_digit = N // 1000
print(first_digit);

#You are provided with two numbers A and B where A as divisor and B as dividend.Your task is find the remainder. 
A = 3
B = 10
remainder = B % A
print(remainder);

#You are provided with two numbers A and B Your task is to multiply these two numbers. 
A = 5
B = 4
C = A * B
print(C);

#Shyam has got his marks in three subjects as A, B and C (out of 100).Write a program to calculate his total marks and his average. 
A = 85
B = 90
C = 78
total = A + B + C
average = total / 3
print("Total marks:", total)
print("Average marks:", average)