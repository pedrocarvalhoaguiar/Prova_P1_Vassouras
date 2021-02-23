tamanhoLista = int(input('Digite o tamanho da lista: '))
listaNumeros = []

def SomaLista(tamanho, lista):
    soma = 0
    while len(lista) < tamanhoLista:
        valor = int(input('Digite um valor para lista: '))
        lista.append(valor)
    for i in lista:
        soma += i
    return soma

somaDeTodos = SomaLista(tamanhoLista, listaNumeros)

print(f'A lista possui {tamanhoLista} valores, e a soma entre eles é {somaDeTodos}')