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


    





