"""
 Esta função considera posição inicial == 0
"""
def Fibo(posi):
    if posi == 0:
        return 0
    elif posi == 1:
        return 1
    else:
        return Fibo(posi-1) + Fibo(posi-2)   

posicao = int(input('Digite o valor desejado: '))

while True:     
    if posicao < 0 :
        posicao = int(input("Digite um número positivo: "))
    else:
        fibo = Fibo(posicao)
        print(f'O valor fibonacci na posição {posicao} é {fibo}')
        break