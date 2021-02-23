def isPrime(number):
    conti = 0
    for num in range(1, number + 1):
        if number % num == 0:
            conti += 1
    if conti == 2:
        return True
    else:
        return False

numero = int(input('Digite o valor desejado: '))

if isPrime(numero):
    print('É primo')
else:
    print('Não é primo')
