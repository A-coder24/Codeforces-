for _ in range(int(input())):
    n, x = map(int, input().split())
    s = sum(x in map(int, input().split()) for _ in range(n - 1))
    print(s)
    print("Ayush" if s <= 1 or n % 2 == 0 else "Ashish")
