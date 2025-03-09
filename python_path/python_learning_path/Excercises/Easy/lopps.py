'''Task
The provided code stub reads and integer, n, from STDIN. For all non-negative integers i < n, print i**2.

Example:

n = 3

The list of non-negative integers that are less than  is . Print the square of each number on a separate line.

0
1
2

Input Format

The first and only line contains the integer, .

Constraints

1 <= n <= 20

Output Format

Print  lines, one corresponding to each .

Sample Input : 5

Result:

0
1
4
9
16'''


num = int(input())

for i in range(num):
    print(i**2)


'''for i in range(num):
    if 1 <= i >= 20:
        break
    else:
        print(i**2)'''