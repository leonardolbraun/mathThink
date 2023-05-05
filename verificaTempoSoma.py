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
    return ((1 + n) * n) / 2

def somaListComprehension(n):
    return sum([x for x in range(1, n+1)])

n = 1000000000
loop = 1

for func_name in ('somaPython', 'somaFor', 'somaProgressaoAritmetica', 'somaListComprehension'):
    resultado = timeit.timeit(f'{func_name}(n)', globals=globals(), number=loop)
    tempo = resultado / loop
    print(f"{func_name}: {tempo:.9f}")

#Somar 1000 numeros (1 a 1000)
#somaPython: 0.000013544
#somaFor: 0.000043404
#somaProgressaoAritmetica: 0.000000169
#somaListComprehension: 0.000036279
#
#Somar 100.000 numeros (1 a 100.000)
#somaPython: 0.002243874
#somaFor: 0.004769934
#somaProgressaoAritmetica: 0.000000188
#somaListComprehension: 0.005715858
#
#Somar 1.000.000 numeros (1 a 1.000.000)
#somaPython: 0.029584044
#somaFor: 0.050592506
#somaProgressaoAritmetica: 0.000000349
#somaListComprehension: 0.082341479
#
#Somar 1.000.000.000 numeros (1 a 1.000.000)
#somaPython: 30.258568400
#somaFor: 55.474500000
#somaProgressaoAritmetica: 0.000013500
#somaListComprehension: Memory Error :p
