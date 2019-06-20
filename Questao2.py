
num = input("Digite um inteiro de 4 dígitos: ")

if (len(num) == 4):
    num = int(num)
    digito1 = num // 1000 % 10
    digito2 = num // 100 % 10
    digito3 = num // 10 % 10 
    digito4 = num // 1 % 10

    digito1 = (digito1 + 6) % 10
    digito2 = (digito2 + 6) % 10
    digito3 = (digito3 + 6) % 10
    digito4 = (digito4 + 6) % 10

    aux1 = digito1
    aux2 = digito2
    aux3 = digito3
    aux4 = digito4
    
    digito1 = aux3
    digito2 = aux4
    digito3 = aux1
    digito4 = aux2

    print('Inteiro criptografado: %d%d%d%d' %(digito1, digito2, digito3, digito4))

    numcrip = int(input('Insira o o numero criptografado: '))

    num1 = numcrip // 1000 % 10
    num2 = numcrip // 100 % 10
    num3 = numcrip // 10 % 10
    num4 = numcrip // 1 % 10
    
    apoio1 = (num1 + 4) % 10
    apoio2 = (num2 + 4) % 10
    apoio3 = (num3 + 4) % 10
    apoio4 = (num4 + 4) % 10

    a1 = apoio1
    a2 = apoio2
    a3 = apoio3
    a4 = apoio4

    primitiva1 = apoio3
    primitiva2 = apoio4
    primitiva3 = apoio1
    primitiva4 = apoio2

    print('Inteiro descriptografado: %d%d%d%d' %(primitiva1, primitiva2, primitiva3, primitiva4))

else:
    print('O número informado não possui 4 dígitos!')

