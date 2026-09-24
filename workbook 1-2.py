'task 1'
def binary_search(lst, key):
    low = 0
    high = len(lst) - 1
    is_reversed = len(lst) > 1 and lst[0] > lst[-1]

    while low <= high:
        mid = (low + high) // 2
        midVal = lst[mid]
        
        if midVal == key:
            return mid
            
        # если убывает
        if is_reversed:
            if midVal < key: 
                high = mid - 1
            else:
                low = mid + 1 
                
        # если возрастает 
        else:
            if midVal > key:
                high = mid - 1
            else:
                low = mid + 1
    lst.insert(low, key)
    
    return low


a = [8, 7, 3, 1]
print (binary_search(a, 2)) # 3

a = [8, 7, 3, 1]
print (binary_search(a, 7)) # 1

a = [1, 2, 4, 6, 8, 10, 12]
print (binary_search(a, 3)) # 2

a = [1, 2, 4, 6, 8, 10, 12]
print (binary_search(a, 0)) # 0

a = [1, 2, 4, 6, 8, 10, 12]
print (binary_search(a, 100)) # 7

'task 2'
def solve2(arr):
    if len(arr) < 3: return 'не горный'
    low = 0
    high = len(arr) - 1
    
    while low < high:
        mid = (low + high) // 2
        
        if arr[mid] < arr[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return low if low not in (0,len(arr)-1) else 'не горный'

print(solve2([1, 3, 5, 6, 7, 4, 2])) # 4
print(solve2([1, 4])) # не горный
print(solve2([1,2,3,4])) # не горный
print(solve2([4,3,2,1])) # не горный

'task 3'
def solve3(lst):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] < 0:
            low = mid + 1
        else:
            high = mid - 1
    negative = low 

    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] <= 0:
            low = mid + 1
        else:
            high = mid - 1
    
    positive = len(lst) - low
    return max(negative, positive)

a = [-5, -3, -2, -1, 0, 0, 0, 4, 4, 4, 4, 6, 100]
print(solve3(a)) # 6

a = [-5, -3, -2, -1, 4, 6, 100] 
print(solve3(a)) # 4

a = [-4, -3, -1] 
print(solve3(a)) # 3

a = [2, 3, 5] 
print(solve3(a)) # 3



'task 4'
def solve4(nums):
    counts = []
    for i in range(len(nums)):
        c = 0
        for j in range(i+1, len(nums)):
            ii = nums[i]
            jj = nums[j]
            if ii > jj:
                c += 1
        counts += [c]
    return counts

print(solve4([5,2,6,1]))  # [2, 1, 1, 0]
print(solve4([5,4,3,2,1])) # [4, 3, 2, 1, 0]
print(solve4([1,2,3])) # [0, 0, 0]