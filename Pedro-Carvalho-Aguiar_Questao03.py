"""
 Esta função considera posição inicial == 0
"""
def Fibo(posi):
    if posi == 1:
        return 0
    elif posi == 2:
        return 1
    elif posi > 2:
        return Fibo(posi-1) + Fibo(posi-2)   

posicao = int(input('Digite o valor desejado: '))

while True:     
    if posicao <= 0 :
        posicao = int(input("Digite um número positivo: "))
    else:
        fibo = Fibo(posicao)
        print(f'O valor fibonacci na posição {posicao} é {fibo}')
        break

"""
Essa é a função para considerar a posição 1 == 1
def fibo(posi):
    if posi == 1:
        return 1
    elif posi == 2:
        return 1
    elif posi > 2:
        return fibo(posi-1) + fibo(posi-2)
"""