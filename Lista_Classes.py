## 1. 

import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
        pi = math.pi
        area = pi * self.raio ** 2

        return area
    
raio_circulo = float(input("Digite o raio do círculo: "))
circulo = Circulo(raio_circulo)
area_circulo = circulo.calcular_area()

print(f"A área do círculo com raio {raio_circulo} é {area_circulo}")

## 2.

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def detalhes(self):
        return f"Título: {self.titulo} \nAutor: {self.autor}"
    
livros = Livro("Auto da Compadecida", "Ariano Suassuna") 
print(livros.detalhes())

## 3.

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

retangulo1 = Retangulo( 2 , 4 )
area = retangulo1.calcular_area()

print(f"A área do retângulo é: {area}")

## 4.

class ContaBancaria:
    def __init__ (self, titular, saldo):
        self.saldo = saldo
        self.titular = titular

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return f"Seu depósito no valor de R${valor} foi realizado. Seu saldo atual é: R${self.saldo}"    
        else:
            return "Valor inválido. O valor do depósito deve ser maior que zero."
        
    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            return f"Saque de R${valor} realizado com sucesso. Seu saldo atual é: R${self.saldo}."
        else:
            return "Algo deu errado! Verifique o valor ou saldo disponível."
        
conta_x = ContaBancaria("Carolina", 25000)
print(conta_x.depositar(200))
print(conta_x.sacar(150))

## 5.

class Pessoa:
    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f'{self.nome} está falando.')

pessoa_x = Pessoa("Rafa", 25)
pessoa_y = Pessoa("Igor", 26)

pessoa_x.falar()  
pessoa_y.falar()

## 6.

class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_total(self):
        return self.preco * self.quantidade
    
produto_x = Produto("Mochila", 80.00, 6)
produto_y = Produto("Tenis", 95.00, 7)

total_x = produto_x.calcular_total()
total_y = produto_y.calcular_total()

print(f"O valor total de {produto_x.nome} equivale a R${total_x}.")
print(f"O valor total de {produto_y.nome} equivale a R${total_y}.")

## 7.

class Carro:
    def __init__ (self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def detalhes(self):
        return f"Marca: {self.marca}. \nModelo: {self.modelo}. \nAno: {self.ano}\n."

carro_x = Carro("Volkswagen", "Gol", "2012")
carro_y = Carro("Fiat","Mobi","2015")
carro_z = Carro("Mitsubishi","Lancer","2023")

detalhes_carro_x = carro_x.detalhes()
detalhes_carro_y = carro_y.detalhes()
detalhes_carro_z = carro_z.detalhes()

print(detalhes_carro_x)
print(detalhes_carro_y)
print(detalhes_carro_z)

## 8.

class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        if len(self.notas) > 0:
            return sum(self.notas) / len(self.notas)
        else:
            return 0

aluno_x = Aluno("Rafa", [9.5, 8.5, 9.0])
aluno_y = Aluno("Vitor", [5.5, 7.5, 8.0])

media_aluno_x = aluno_x.calcular_media()
media_aluno_y = aluno_y.calcular_media()

print(f'A média de {aluno_x.nome} é {media_aluno_x}')
print(f'A média de {aluno_y.nome} é {media_aluno_y}') 

## 9.

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

triangulo1 = Triangulo(3, 4, 5)
triangulo2 = Triangulo(6, 8, 10)

perimetro1 = triangulo1.calcular_perimetro()
perimetro2 = triangulo2.calcular_perimetro()

print(f'O perímetro do primeiro triângulo é {perimetro1}')
print(f'O perímetro do segundo triângulo é {perimetro2}')

## 10.

class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def aumentar_salario(self, percentual_aumento):
        if percentual_aumento > 0:
            self.salario += (self.salario * percentual_aumento / 100)
            return f'O salário de {self.nome} foi aumentado em {percentual_aumento}%. Novo salário: R${self.salario:.2f}'
        else:
            return 'O percentual de aumento deve ser maior que zero.'

funcionario1 = Funcionario("Ana", 6000, "Analista")
funcionario2 = Funcionario("Isabel", 5500, "Desenvolvedor")

print(funcionario1.aumentar_salario(10))  
print(funcionario2.aumentar_salario(5))