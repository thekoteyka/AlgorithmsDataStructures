import math

# Номер 1
# Нечетный вариант

def gcd_div(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def gcd_div_three(a,b,c):
    result = gcd_div(gcd_div(a, b), c)
    return result

print("НОД трех чисел (деление)")
n1 = int(input("Введите 1-е число: "))
n2 = int(input("Введите 2-е число: "))
n3 = int(input("Введите 3-е число: "))

# Ищем НОД первых двух, а затем НОД результата и третьего числа
result = gcd_div_three(n1,n2,n3)
print(f"НОД: {result}\n")


# Чётный вариант
def gcd_sub(a, b):
    # Если одно из чисел 0, возвращаем второе
    if a == 0: return b
    if b == 0: return a
    
    # Пока числа не равны, вычитаем меньшее из большего
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

print("НОД четырех чисел (вычитание)")
m1 = int(input("Введите 1-е число: "))
m2 = int(input("Введите 2-е число: "))
m3 = int(input("Введите 3-е число: "))
m4 = int(input("Введите 4-е число: "))

def gcd_sub_four(a,b,c,d):
    res1 = gcd_sub(a, b)
    res2 = gcd_sub(res1, c)
    final = gcd_sub(res2, d)

    return final


final_result = gcd_sub_four(m1,m2,m3,m4)
print(f"НОД: {final_result}")

# Номер 2
def sieve(limit):
    """Возвращает список простых чисел до limit включительно."""
    sieve_list = [True] * (limit + 1)
    sieve_list[0] = sieve_list[1] = False # 0 и 1 не простые
    
    for p in range(2, int(math.sqrt(limit)) + 1):
        if sieve_list[p]:
            # Вычеркиваем все числа, кратные p
            for i in range(p+1, limit + 1, p):
                sieve_list[i] = False
                
    return [p for p in range(2, limit + 1) if sieve_list[p]]

def factorize_brute_force(n):
    # Генерируем простые числа до n
    primes = sieve(n)
    factors = {} # {множитель: кратность}
    
    for p in primes:
        if p * p > n and n > 1: # Если квадрат простого больше остатка числа, значит сам остаток простое число
            if n not in factors:
                factors[n] = 0
            factors[n] += 1
            break
            
        count = 0
        while n % p == 0:
            count += 1
            n //= p
        
        if count > 0:
            factors[p] = count
            
        if n == 1:
            break
            
    return factors

number = int(input("Введите число для факторизации: "))
res = factorize_brute_force(number)
for prime, count in res.items():
    print(f"Множитель: {prime}; Кратность: {count}")


# Задание 3

def is_prime_sieve(n):
    if n < 2: return False
    primes = sieve(n)
    return n in primes

def ferma(n):
    """Разбивает число на 2 множителя методом Ферма"""
    if n % 2 == 0:
        return 2, n // 2
        
    a = math.ceil(math.sqrt(n))
    b2 = a * a - n
    b = math.isqrt(b2) # целочисленный корень
    
    # Пока b^2 не является полным квадратом, увеличиваем a
    while b * b != b2:
        a += 1
        b2 = a * a - n
        b = math.isqrt(b2)
        
    return a - b, a + b

def full_ferma(n):
    """Рекурсивно разбивает число до простых множителей"""
    factors_count = {}
    
    def factorize(num):
        if num == 1:
            return
        # Если число простое, записываем и выходим
        if is_prime_sieve(num):
            factors_count[num] = factors_count.get(num, 0) + 1
            return
            
        # Разбиваем на два множителя
        x, y = ferma(num)
        
        # Если Ферма вернул (1, num), то это простое
        if x == 1:
            factors_count[y] = factors_count.get(y, 0) + 1
            return
            
        # Рекурсивно факторизуем обе части
        factorize(x)
        factorize(y)

    factorize(n)
    return factors_count

number_fermat = int(input("Введите нечетное число для факторизации методом Ферма: "))
if number_fermat % 2 == 0:
    print("Число должно быть нечетным.")
else:
    res = full_ferma(number_fermat)
    print("Простые множители и их кратность:")
    for prime, count in res.items():
        print(f"Множитель: {prime}, Кратность: {count}")

# Задание 4 
def lucas_lehmer_test(p):
    # p должно быть простым нечетным числом (по условию алгоритма)
    if p == 2:
        return True # M_2 = 3 - простое
        
    m = p**2 - 1
    s = 4
    
    # Выполняем цикл p - 2 раза
    for i in range(p - 2):
        s = (s * s - 2) % m
        
    return s == 0

p = int(input("Введите номер числа Мерсенна (степень p): "))
m_val = (2 ** p) - 1
print(f"Рассматриваем число M_{p} = {m_val}")

if lucas_lehmer_test(p):
    print("Число простое.")
else:
    print("Число составное.")

# Задание 5
def neyman(seed, count=10):
    sequence = []
    current = seed
    
    for _ in range(count):
        square = current ** 2
        current = (square // 100) % 100000
        sequence.append(current)
        
    return sequence

seed = int(input("Введите начальное пятизначное число: "))
random_numbers = neyman(seed)

print("Последовательность:")
for i, num in enumerate(random_numbers, 1):
    # zfill(5) добавляет нули слева, если число получилось короче 5 цифр
    print(f"{i}. {str(num).zfill(5)}")

# Задание 6
def sieve_sundaram(limit):
    # Алгоритм Сундарама ищет простые нечетные числа до limit.
    # Поэтому размер массива k мы берем как (limit - 1) // 2
    n = (limit - 1) // 2
    marked = [False] * (n + 1)
    
    # Вычеркиваем числа по формуле i + j + 2*i*j
    for i in range(1, n + 1):
        j = i
        while (i + j + 2 * i * j) <= n:
            marked[i + j + 2 * i * j] = True
            j += 1
            
    # Собираем результат
    primes = [2] # 2 - единственное четное простое число, добавляем вручную
    
    # Для каждого невычеркнутого k, число 2*k + 1 является простым
    for k in range(1, n + 1):
        if not marked[k]:
            primes.append(2 * k + 1)
            
    return primes

limit = int(input("Введите границу поиска простых чисел (Решето Сундарама): "))
primes_sundaram = sieve_sundaram(limit)
print(f"Простые числа до {limit}:")
print(primes_sundaram)