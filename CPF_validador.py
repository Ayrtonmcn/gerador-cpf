cpf_informado = input('Digite um CPF no seguinte formato [xxx.xxx.xxx-xx] para validar: ')

cpf_informado_ajustes = cpf_informado \
    .replace(' ', '') \
    .replace('.', '') \
    .replace('-', '') \

cpf_informado_fatiado = cpf_informado_ajustes[:9]

multiplicador = 10
soma_dig1 = 0
for numero in cpf_informado_fatiado:
    soma_dig1 = soma_dig1 + int(numero) * multiplicador
    multiplicador -= 1

cpf_dig1 = (soma_dig1 * 10) % 11
cpf_dig1 = cpf_dig1 if cpf_dig1 < 10 else 0
novo_cpf = cpf_informado_fatiado + str(cpf_dig1)

multiplicador = 11
soma_dig2 = 0
for numero in novo_cpf:
    soma_dig2 = soma_dig2 + int(numero) * multiplicador
    multiplicador -= 1

cpf_dig2 = (soma_dig2 * 10) % 11
cpf_dig2 = cpf_dig2 if cpf_dig2 < 10 else 0
novo_cpf = novo_cpf + str(cpf_dig2)

if novo_cpf == novo_cpf[0] * len(novo_cpf):
    print('O CPF não é válido!')
elif novo_cpf == cpf_informado_ajustes:
    print(f'O CPF {cpf_informado} é válido!')
else:
    print('O CPF não é válido!')    
        