import math
# защищено на первом занятии
def f(x):
    return 0.1 * x ** 2 - x * math.log(x)

L = 1.0
R = 2.0
eps = 0.0001

f_L = f(L)
step = 0
B = (L + R) / 2.0

while (R - L) > eps:
    step += 1
    B = (L + R) / 2.0
    
    f_B = f(B)
    
    if f_B == 0.0:  break
        
    if f_L * f_B < 0:
        R = B
    else:
        L = B
        f_L = f_B

print('метод половинного деления')
print(f"x = {B}")
print(f"нашли за {step} шагов")
# output:
# x = 1.11834716796875
# нашли за 14 шагов


print('===========')


L = 1.0
R = 2.0
eps = 0.0001

f_L = f(L)
f_R = f(R)

x_prev = L 
x_curr = L - (f_L * (R - L)) / (f_R - f_L)  # по формуле из методички

step = 0

while abs(x_curr - x_prev) > eps:
    step += 1
    x_prev = x_curr
    
    f_x = f(x_curr)
    
    if f_x == 0.0:  break
        
    # Пункт 3
    if f_x * f_R > 0:
        R = x_curr
        f_R = f_x
    else:
        L = x_curr
        f_L = f_x
        
    # вычисляем следующий икс по формуле из методички
    x_curr = L - (f_L * (R - L)) / (f_R - f_L)

print("метод хорд")
print(f"x = {x_curr}")
print(f"нашли за {step} шагов")
# output:
# x = 1.118315636619269
# нашли за 5 шагов