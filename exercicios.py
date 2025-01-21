import math

#Exercícios

### Inteiros (int)

#1 Escreva um programa que soma dois números inteiros inseridos pelo usuário.

    # num01 = int(input("Digite o primeiro número:"))
    # num02 = int(input("Digite o segundo número:"))

    # resultado = num01 + num02

    # print(f"A soma dos numero digitados é {resultado}")

#2 Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

    # num01 = int(input("Digite um numero: "))

    # resultado = num01 % 5

    # print(f"O resto da divisão é: {resultado}")

#3 Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

    # num01 = int(input("Digite o primeiro número: "))
    # num01 = int(input("Digite o segundo número: "))

    # resultado = num01 * num01
    # print (f"O resultado da multiplicação é {resultado}")

#4 Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

    # num01 = int(input("Digite o primeiro número: "))
    # num02 = int(input("Digite o segundo número: "))
    # resultado = num01 // num02
    # print(f"A divisão entre os números digitados: {resultado}")
#5 Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

# num01 = int(input("Digite um número: "))

# resultado = num01 ** 2

# print(f"O resultado do npumero digitado elevado ao quadrado é: {resultado}")


### Números de Ponto Flutuante (float)

#6 Escreva um programa que receba dois números flutuantes e realize sua adição.

    # num01 = float(input("Digite o primeiro número: "))
    # num02 = float(input("Digite o segundo número: "))

    # resultado = num01 + num02

    # print(f"A soma dos dois números é: {resultado}")

#7 Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

    # num01 = float(input("Digite o primeiro número: "))
    # num02 = float(input("Digite o segundo número: "))

    # resultado = (num01 + num02) / 2

    # print(f"A média dos dois números é: {resultado}")

#8 Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

    # base = float(input("Digite digite a base: "))
    # expoente = float(input("Digite o expoente: "))

    # resultado = base ** expoente

    # print(f"O resultado da potência é: {resultado}")

#9 Faça um programa que converta a temperatura de Celsius para Fahrenheit.

    # tem_celsius = float(input("Digite a temperatura atual em celsius: "))

    # resultado = (tem_celsius * 1.8) + 32

    # print(f"A temperatura em Fahrenheit é de {resultado}°")


#10 Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

    # raio_do_circulo = float(input("Digite o raio: "))
    # area_do_circulo = math.pi * raio_do_circulo ** 2

    # print(f"A área do circulo é {area_do_circulo:.2f}")

### Strings (str)

#11 Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

    # nome = input("Digite o seu nome: ")
    # str_maiscula = nome.upper()

    # print(f'Nome digitado: {str_maiscula}')

#12 Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

    # nome_completo = input("Digite o seu nome completo: ")
    # str_minuscula = nome_completo.lower()

    # print(f'Nome digitado: {str_minuscula}')

#13 Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

    # frase = input("Digite uma frase: ")
    # sem_espacos_ini_fim = frase.strip()

    # print(f'Frase digitada sem espaços no inicio e no fim: {sem_espacos_ini_fim}')

#14 Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

    # data = input("Digite uma data no formato dd/mm/aaaa: ")
    # split_data = data.split("/")
    # dia = split_data[0]
    # mes = split_data[1]
    # ano = split_data[2]

    # print(f"Dia: {dia}, Mês: {mes}, Ano: {ano}")

#15 Escreva um programa que concatene duas strings fornecidas pelo usuário.

    # palavra00 = input("Digite a primeira palavra: ")
    # palavra01 = input("Digite a segunda palavra: ")

    # resultado = palavra00 + ' ' + palavra01

    # print(f"a concatenação das palavras digitadas é {resultado}")

### Booleanos (bool)

#16 Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

    # valor00 = True
    # valor01 = False

    # resultado = valor00 and valor01 

    # print(f"O Resultado do valor lógico AND é: {resultado}")

#17 Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.

    # resultado = True or False
    # print(f"O resultado do valor lógico OR é: {resultado}")

#18 Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.

    # valor = False
    # resultado = not valor

    # print(f"Resultado do valor lógico invertido NOT: {resultado}")

#19 Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

    # num000 = int(input("Digite o primeiro número: "))
    # num001 = int(input("Digite o segundo número: "))

    # resultado = (num000 == num001)

    # print(f"Resultado da igualdade: {resultado}")

#20 Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

    # num000 = int(input("Digite o primeiro número: "))
    # num001 = int(input("Digite o segundo número: "))

    # resultado = (num000 != num001)

    # print(f"Resultado da diferença: {resultado}")


# Aqui estão cinco exercícios que envolvem TypeError, verificação de tipo (type check), o uso de try-except para tratamento de exceções e a utilização da estrutura condicional if. 
# Esses exercícios aumentam progressivamente em dificuldade e abordam situações práticas onde você pode aplicar esses conceitos.

# Exercício 21: Conversor de Temperatura

# Escreva um programa que converta a temperatura de Celsius para Fahrenheit. O programa deve solicitar ao usuário a temperatura em Celsius e, utilizando try-except, 
# garantir que a entrada seja numérica, tratando qualquer ValueError. Imprima o resultado em Fahrenheit ou uma mensagem de erro se a entrada não for válida.

    # try:
    #     tem_celsius = float(input("Digite a temperatura atual em celsius: "))

    #     resultado = (tem_celsius * 1.8) + 32

    #     print(f"A temperatura em Fahrenheit é de {resultado}°")
    # except:
    #    print("Parece que você não digitou o valor numérico para temperatura, tente novamente!") 

# Exercício 22: Verificador de Palíndromo
# Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações). 
# Utilize try-except para garantir que a entrada seja uma string. Dica: Utilize a função isinstance() para verificar o tipo da entrada.

    # entrada = input("Digite uma palavra ou frase: ")
    # if isinstance(entrada, str):
    #     formatado = entrada.replace(" ", "").lower()
    #     if formatado == formatado[::-1]:
    #         print("É um palíndromo.")
    #     else:
    #         print("Não é um palíndromo.")
    # else:
    #     print("Entrada inválida. Por favor, digite uma palavra ou frase.")

# Exercício 23: Calculadora Simples
# Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. Use try-except para lidar com divisões por zero e entradas não numéricas.
# Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. Imprima o resultado ou uma mensagem de erro apropriada.

try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operador = input("Digite o operador (+, -, *, /): ")
    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/' and num2 != 0:
        resultado = num1 / num2
    else:
        print("Operador inválido ou divisão por zero.")

except ValueError:
    print("ERRO: Entrada Inválida. Certifique-se de inserir números.")

# Exercício 24: Classificador de Números
# Escreva um programa que solicite ao usuário para digitar um número. Utilize try-except para assegurar que a entrada seja numérica e utilize if-elif-else para classificar o número como 
# "positivo", "negativo" ou "zero". Adicionalmente, identifique se o número é "par" ou "ímpar".

# Exercício 25: Conversão de Tipo com Validação
# Crie um script que solicite ao usuário uma lista de números separados por vírgula. O programa deve converter a string de entrada em uma lista de números inteiros.
# Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. Se a conversão falhar ou um elemento não for um inteiro, 
# imprima uma mensagem de erro. Se a conversão for bem-sucedida para todos os elementos, imprima a lista de inteiros.