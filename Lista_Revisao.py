## 1.

x = float(input("Vamos calcular a média de 3 valores? \n"
                "Insira um número: \n"))
y = float(input("Insira outro número: \n"))
z = float(input("Insira o terceiro número: \n"))

media = (x + y + z) / 3

print(f"A média dos valores inseridos é: {media:.2f}")

## 2.

numero = float(input("Insira um número para verificar se é par ou impar: \n"))

    # Qualquer número dividido por 2 com resto zero é par!

if numero % 2 == 0:
    print("O número é PAR.")
else:
    print("O número é ÍMPAR.")

## 3.

numero_par = int(input("Insira um número: "))
print(f"Os números pares de 0 até {numero_par} são: ")

for i in range(0, numero_par, 2):
    print(i)

## 4.

primeiro = (input("Insira o primeiro número: "))
segundo = (input("Insira o segundo número: "))
terceiro = (input("Insira o terceiro número: ")) 

    # Maior número

maior = primeiro

if (segundo > maior):
    maior = segundo
if (terceiro > maior):
    maior = terceiro

print(f"O maior número é: {maior}")

    # Menor número
    
menor = primeiro

if (segundo < menor):
    menor = segundo
if (terceiro < maior):
    menor = terceiro

print(f"O menor número é: {menor}")

## 5.

lista = input("Digite uma lista de números usando espaço entre eles: ")
numeros = [int(num) for num in lista.split()]

num_pares = []

for num in numeros:
    if num % 2 == 0:
        num_pares.append(num)

media = sum(num_pares) / len(num_pares)

if num_pares:
    print(f"A média dos números pares inseridos é {media:.2f}.")
else:
    print("Não foram inseridos números pares.")

## 6. 

int_positivo = int(input("Insira um número inteiro positivo: "))
numero = int_positivo
fator = 1

while numero > 0:
    print(numero, end = ' ')
    print(" x " if numero > 1 else f" = {fator}", end=" ")
    fator = fator * numero
    numero -= 1


print(f"\nO fatorial de {int_positivo} é {fator}")

## 7.

valor = int(input("Digite um número inteiro para ver a sequencia de números de Fibonacci até esse valor: "))

n1 = 0
n2 = 1
print(f"{n1} - {n2}", end = ' ')

cont = 3
while cont <= valor:
    n3 = n1 + n2
    print(f"- {n3}", end = ' ')
    n1 = n2
    n2 = n3
    cont += 1
print("- FIM")    

## 8.

num_8 = int(input("Insira um número para verificar se é um número primo: "))
divisiveis = 0

for p in range(1, num_8 + 1):
    if num_8 % p == 0:
        divisiveis += 1

if divisiveis == 2:        
        print(f'{num_8} é um número primo!')
else:
        print(f'{num_8} não é um número primo!')

## 9.

lista = input('Digite uma lista de nomes separados por espaços: ')
nomes = lista.split()

print('\n~~ Lista de nomes inseridos: ')
for nome in nomes:
    print(nome.capitalize())

a = [nome for nome in nomes if nome.lower().startswith('a')]

print('\n ~~ Nomes que começam com a letra A: ')
for nome in a:
    print(nome.capitalize())

## 10.

import random

pc = ['PEDRA','PAPEL','TESOURA']
computador = random.choice(pc)

print("PEDRA, PAPEL OU TESOURA\n")
user = input("Digite uma opção para jogar: \n").strip().upper()


if user == 'PEDRA' and computador == 'PEDRA':
    print('PEDRA x PEDRA! \n EMPATE!')
elif user == 'PEDRA' and computador == 'PAPEL':
    print('PEDRA x PAPEL \n VOCÊ PERDEU!')
elif user == 'PEDRA' and computador == 'TESOURA':
    print('PEDRA x TESOURA \n VOCÊ VENCEU!')

if user == 'PAPEL' and computador == 'PAPEL':
    print('PAPEL x PAPEL \n EMPATE!')
elif user == 'PAPEL' and computador == 'PEDRA': 
    print('PAPEL x PEDRA \n VOCÊ VENCEU!')
elif user == 'PAPEL' and computador == 'TESOURA':
    print('PAPEL x TESOURA \n VOCÊ PERDEU!')

if user == 'TESOURA' and computador == 'TESOURA':
    print('TESOURA x TESOURA \n EMPATE!')
elif user == 'TESOURA' and computador == 'PEDRA': 
    print('TESOURA x PEDRA \n VOCÊ PERDEU!')
elif user == 'TESOURA' and computador == 'PAPEL':
    print('TESOURA x PAPEL \n VOCÊ VENCEU!')

else:
    print('Opção inválida!')