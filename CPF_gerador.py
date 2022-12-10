import random

cpf_gerado = ''
for n in range(0,9):
    cpf_gerado += str(random.randint(0,9))

multiplicador = 10
soma_dig1 = 0
for numero in cpf_gerado:
    soma_dig1 = soma_dig1 + int(numero) * multiplicador
    multiplicador -= 1

cpf_dig1 = (soma_dig1 * 10) % 11
cpf_dig1 = cpf_dig1 if cpf_dig1 < 10 else 0
novo_cpf = cpf_gerado + str(cpf_dig1)

multiplicador = 11
soma_dig2 = 0
for numero in novo_cpf:
    soma_dig2 = soma_dig2 + int(numero) * multiplicador
    multiplicador -= 1

cpf_dig2 = (soma_dig2 * 10) % 11
cpf_dig2 = cpf_dig2 if cpf_dig2 < 10 else 0
novo_cpf = novo_cpf + str(cpf_dig2)

contador = 1
for digito in novo_cpf:
    if contador == 3 or contador == 6:
        print(f'{digito}.', end='')
    elif contador == 9:
        print(f'{digito}-', end='')
    else:
        print(digito, end='')
    contador += 1
