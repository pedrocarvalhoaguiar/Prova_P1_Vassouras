def distanciaEuclidiana(x1, y1, x2, y2):
    dist = ((x1**2) - (2*x1*x2) + (x2**2) + (y1**2) - (2*y1*y2) + (y2**2))**0.5
    return dist

x1 = int(input('Digite o X do primeiro ponto: '))
y1 = int(input('Digite o Y do primeiro ponto: '))
x2 = int(input('Digite o X do segundo ponto: '))
y2 = int(input('Digite o Y do segundo ponto: '))

distancia = distanciaEuclidiana(x1, y1, x2, y2)

print(f'A distancia euclidiana entre os pontos {x1, y1} e {x2, y2} é {distancia:.2f}')