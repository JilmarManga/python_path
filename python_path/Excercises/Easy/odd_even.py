"""Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5 , print Not Weird
If  is even and in the inclusive range of 6 to 20, print Weird
If  is even and greater than 20, print Not Weird
Input Format

A single line containing a positive integer, n .

Constraints
* 1 <= n <= 100

Output Format

Print Weird if the number is weird. Otherwise, print Not Weird."""

# Solution No.1: -------------------------------------------------------
# Traditional statemen solution ans estructure if - else

#imput a single integer only
user_input = input('Enter a number: ').strip()
try:
#Check if input (user_input) is a valid number
    n = float(user_input)
#conditional checks    
    if n % 2 == 1: #print('Weird') #check if n is odd 
        print('Weird') 
    elif 2 <= n <= 5: #Even and in the range 2 to  5
        print('Not Weird')
    elif 6 <= n <= 20: #Even and in the range 6 to 20 
        print('Weird')
    elif n > 20:
        print('Not Weird') #Even and greater then 20
        
except:
    print('This is not  valid number, please writea nunber') #Input is not a valid number
    



# Solution No.2: -------------------------------------------------------- 
# ternary expression or conditional expresion if - else (shorthand way of writing an if-else statement) extructure: value-if-true + if + condition + else + value-if-false  

n = int(input())

print("Not Weird") if n % 2==0 and (n >= 0 and (n <= 5 or n > 20)) else print("Weird")
    


