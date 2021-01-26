def plus_function(x,y):
    if (type(x) is not str) and (type(y) is not str):
        return x + y
    else:
        return TypeError

def minus_function(x,y):
    if (type(x) is not str) and (type(y) is not str):
        return x - y
    else:
        return TypeError

def times_function(x,y):
    if (type(x) is not str) and (type(y) is not str):
        return x * y
    else:
        return TypeError

def division_function(x,y):
    if (type(x) is not str) and (type(y) is not str):
        return x / y
    else:
        return TypeError

def remainder_function(x,y):
    if (type(x) is not str) and (type(y) is not str):
        return x % y
    else:
        return TypeError

def quotient_function(x,y):
    if (type(x) is not str) and (type(y) is not str):
        return x // y
    else:
        return TypeError

def power_function(x,y):
    if (type(x) is not str) and (type(y) is not str):
        return x ** y
    else:
        return TypeError

def divmod_function(x,y):
    if (type(x) is not str) and (type(y) is not str):
        return divmod(x,y)
    else:
        return TypeError

x = 20
y = 5

a = "10"
b = 7

p = 3.14
q = 2

print(plus_function(x,y))
print(plus_function(a,b))
print(plus_function(p,q))

print(minus_function(x,y))
print(minus_function(a,b))
print(minus_function(p,q))

print(times_function(x,y))
print(times_function(a,b))
print(times_function(p,q))

print(division_function(x,y))
print(division_function(a,b))
print(division_function(p,q))

print(remainder_function(x,y))
print(remainder_function(a,b))
print(remainder_function(p,q))

print(quotient_function(x,y))
print(quotient_function(a,b))
print(quotient_function(p,q))

print(power_function(x,y))
print(power_function(a,b))
print(power_function(p,q))

print(divmod_function(x,y))
print(divmod_function(a,b))
print(divmod_function(p,q))

'''result
25
<class 'TypeError'>
5.140000000000001
15
<class 'TypeError'>
1.1400000000000001
100
<class 'TypeError'>
6.28
4.0
<class 'TypeError'>
1.57
0
<class 'TypeError'>
1.1400000000000001
4
<class 'TypeError'>
1.0
3200000
<class 'TypeError'>
9.8596
(4, 0)
<class 'TypeError'>
(1.0, 1.1400000000000001)
'''