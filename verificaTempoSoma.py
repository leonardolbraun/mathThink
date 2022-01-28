import timeit

##Time to execute every approach to calculate the sum of 1 to n numbers
def somaPython(n):
    return sum(range(n+1))

def somaFor(n):
    soma = 0
    for n in range(1, n+1):
        soma = soma + n
    return soma

def somaProgressaoAritmetica(n):
    return ((1 + n) * 100) / 2

#Is there another way?

n = 1000000000
loop = 1000

resultado = timeit.timeit('somaProgressaoAritmetica(n)', globals=globals(), number=loop)
tempo = resultado / loop
print(f"{tempo:.9f}" )

#Somar 100 numeros (1 a 100)
#test1 = 0.000001039
#test2 = 0.000003183
#test3 = 0.000000121
#
#Somar 100.000 numeros (1 a 100.000)
#test1 = 0.001928083
#test2 = 0.003756276
#test3 = 0.000000136
#
#Somar 1.000.000 numeros (1 a 1.000.000)
#test1 = 0.028677143
#test2 = 0.039949356
#test3 = 0.000000128
