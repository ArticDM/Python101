x = 3.3
y = 1.1+2.2
print(x)
print(y)
print(x==y)

y_str = format(y,".2g")
print(y_str)
print(y_str==str(x))

print('*'*10)
print(y,x)
tol = 0.0001
print(abs(x - y) < tol)

y_round = round(y,2)
print(x,y_round,x==y_round)