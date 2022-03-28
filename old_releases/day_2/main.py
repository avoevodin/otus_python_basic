str_var = "The quick brown fox jumps over the lazy dog"

for word in str_var.split(' '):
    print(word)

num_list = [i for i in range(3, 43, 1)]
sq_list = [i ** 2 for i in num_list]

print(sq_list)

dct = {}

for i in sq_list:
    dct[i] = str(i) * 3

def getPrimeNums(*nums):
    primeNums = []
    for num in nums:
        isPrime = True
        for divider in range(2, num // 2 + 1, 1):
            if num % divider == 0:
                isPrime = False
                break
        if isPrime:
            primeNums.append(num)
    return primeNums

def getUniqSym(str_val):
    return list(set(str_val))
