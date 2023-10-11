## 01. 

def calcular_media(notas):
    return sum(notas) / len(notas)

def verificar_aprovacao(media):
    if media >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

notas = []
for i in range(5):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)

media = calcular_media(notas)

resultado = verificar_aprovacao(media)

print(f"A média do aluno é {media:.2f}")
print(f"O aluno está {resultado}")

## 02.

def calcular_fatorial(numero):
    if numero < 0:
        return "O fatorial não está definido para números negativos."
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

try:
    numero = int(input("Digite um número inteiro positivo: "))
    resultado = calcular_fatorial(numero)
    print(f"O fatorial de {numero} é {resultado}")
except ValueError:
    print("Valor inválido. Insira um número inteiro positivo válido.")


## 03.

palavra = input("Digite uma palavra para verificar se é um palíndromo: ")

for letra in reversed(palavra):
    print(letra) 

palavra_invertida = "".join(reversed(palavra)) 

if palavra == palavra_invertida:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo!") 

## 04.

numero = input("Digite um número inteiro positivo: ")

if int(numero) > 0:
    soma = sum(int(digito) for digito in numero)
    print(f"A soma dos digitos de {numero} é {soma}.")
else:
    print(f"ERRO. Insira um número inteiro positivo válido.")  

## 05.

numero = int(input("Digite um número para verificar se ele é primo: "))
divisiveis = 0

for p in range(1, numero + 1):
    if numero % p == 0:
        divisiveis += 1

if divisiveis == 2:        
        print(f'{numero} é um número primo!')
else:
        print(f'{numero} não é um número primo!')

## 06.

def contador(string):

    vogais = 0

    lista_vogais = ['a', 'e', 'i', 'o', 'u']

    for caractere in texto:
        if caractere in lista_vogais:
            vogais += 1
        return vogais

texto = input("Digite uma string: ".lower())

quant_vogais = contador(texto)

print(f"A quantidade de vogais na string é: {quant_vogais}")

## 07. 

altura = float(input("Digite sua altura: ")) 
peso = float(input("Digite seu peso: "))
imc = peso / (altura*altura)
print(f"Seu imc é: {imc:.2f}")

## 08.

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


escolha = input("Escolha a conversão ('C' para Celsius -> Fahrenheit ou 'F' para Fahrenheit -> Celsius): ").strip().upper()

if escolha not in ["C", "F"]:
    print("Escolha de conversão inválida. Use 'C' ou 'F'.")

temperatura = float(input("Digite a temperatura: "))

if escolha == "C":
    resultado = celsius_para_fahrenheit(temperatura)
    print(f"{temperatura} graus Celsius são equivalentes a {resultado:.2f} graus Fahrenheit.")
else:
    resultado = fahrenheit_para_celsius(temperatura)
    print(f"{temperatura} graus Fahrenheit são equivalentes a {resultado:.2f} graus Celsius.")

## 09.

n1 = float(input("Digite o primeiro número: "))
operador = input("Digite um operador: + , - , / ou * :")
n2 = float(input("Digite o segundo número: "))

operadores_validos = ["+","-","/","*"]

if operador not in operadores_validos:
    print("Operador inválido, tente novamente.")

if operador == "+":
    print(f"{n1} + {n2} = {n1 + n2}")

elif operador == "-":
    print(f"{n1} - {n2} = {n1 - n2}")

elif operador == "/":
    print(f"{n1} / {n2} = {n1 / n2}")

else:
    print(f"{n1} * {n2} = {n1 * n2}")

## 10.

def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    while len(fib_sequence) < n:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

n = int(input("Digite quantos termos da sequência de Fibonacci você deseja gerar:  "))
if n <= 0:
    print("O número de termos deve ser maior que zero.")
else:
    result = fibonacci(n)
    print(result)