N = 5

# first  integers
# 1+2+3+4 = 10

# first 3 int
# 1+2+3 = 6


# first 10 int
# 1+2...+3

total = 0
for i in range(N+1):
    total = total + i
    print(total)

print("Final ", total)