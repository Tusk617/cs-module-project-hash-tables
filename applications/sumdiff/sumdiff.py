"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here
a=b=c=d=0

a = q[0]
b = q[1]
c = q[-1]
d = q[-2]

print(f(c) - f(d))
print(f(a) + f(a))

if f(a) + f(a) == f(c) - f(d):
    print("Yes!")
