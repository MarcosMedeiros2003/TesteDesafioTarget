def Seqfibonacci(n):
    n1, n2 = 0, 1
    while n1 <= n:
        if n1 == n:
            return True
        n1, n2 = n2, n1 + n2
    return False


numero = int(input("Informe um número: "))  #solicita um numero

if Seqfibonacci(numero): #verifica se o numero perterce a sequencia fibo ou não.
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
