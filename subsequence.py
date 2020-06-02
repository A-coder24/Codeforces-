""" B. Subsequence Hate
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
Shubham has a binary string s. A binary string is a string containing only characters "0" and "1".

He can perform the following operation on the string any amount of times:

Select an index of the string, and flip the character at that index. This means, if the character was "0", it becomes "1", and vice versa.
A string is called good if it does not contain "010" or "101" as a subsequence  — for instance, "1001" contains "101" as a subsequence, hence it is not a good string, while "1000" doesn't contain neither "010" nor "101" as subsequences, so it is a good string.

What is the minimum number of operations he will have to perform, so that the string becomes good? It can be shown that with these operations we can make any string good.

A string a is a subsequence of a string b if a can be obtained from b by deletion of several (possibly, zero or all) characters.

Input
The first line of the input contains a single integer t (1≤t≤100) — the number of test cases.

Each of the next t lines contains a binary string s (1≤|s|≤1000).

Output
For every string, output the minimum number of operations required to make it good.

Example
inputCopy
7
001
100
101
010
0
1
001100
outputCopy
0
0
1
1
0
0
2
Note
In test cases 1, 2, 5, 6 no operations are required since they are already good strings.

For the 3rd test case: "001" can be achieved by flipping the first character  — and is one of the possible ways to get a good string.

For the 4th test case: "000" can be achieved by flipping the second character  — and is one of the possible ways to get a good string.

For the 7th test case: "000000" can be achieved by flipping the third and fourth characters  — and is one of the possible ways to get a good string."""



tests=int(input())
for _ in range(tests):
    n=input()
    i=0
    num_1=n.count("1")
    num_0=n.count("0")
    num1_and_remain0=[]
    num0_and_remain1=[]
    number_1=0
    number_0=0
    for i in n:
        if i=="1":
            number_1+=1
        else:
            number_0+=1
        num0_and_remain1.append(number_0+num_1-number_1)
        num1_and_remain0.append(number_1+num_0-number_0)
    print(min(min(num0_and_remain1),min(num1_and_remain0)))


    





