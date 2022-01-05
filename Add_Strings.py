# Add Strings
# You are given two non-negative integers N and M represented as strings.
# The task is to display the sum of
# N and M .

# Input Format
# The first line of input contains a single integer T - denoting the number of test cases.
# The only line of each test case contains two space-separated strings -  N and M.

# Output Format
# Print the sum of the two input strings. Display answer for each test case in a new line.
#
# Constraints
# 1 ≤ T ≤ 1000

# 1 ≤ | N | , |M | ≤ 5100#, where  | N | , | M |  are the lengths of the strings N and M respectively.
# N and M contain only digits  0 − 9. N and  M
#  do not contain any leading zeros.
# Time Limit
# 1 second
#
# Examples
# Input
# 3
# 1 9
# 22 33
# 19 20
#
# Output
# 10
# 55
# 39

def addStrings(num1, num2) -> str:
    res = []
    ptr1, ptr2, carry = len(num1) - 1, len(num2) - 1, 0

    while ptr1 >= 0 or ptr2 >= 0:
        ans = carry

        if ptr1 >= 0:
            ans += ord(num1[ptr1]) - ord('0')
            ptr1 -= 1

        if ptr2 >= 0:
            ans += ord(num2[ptr2]) - ord('0')
            ptr2 -= 1

        # get the lowest digit
        res.append(str(ans % 10))

        # get carry if it has one
        carry = (ans // 10)

    if carry:
        res.append(str(carry))

    return "".join(reversed(res))
t=int(input())
while t>0:
    str1,str2=input().split()
    print(addStrings(str1, str2))
    t=t-1