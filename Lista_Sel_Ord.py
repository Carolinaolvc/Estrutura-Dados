## 01.

def ordenar_vetor(vetor):
    n = len(vetor)

    for i in range(n):
        indice_minimo = i

        for j in range(i + 1, n):
            if vetor[j] < vetor[indice_minimo]:
                indice_minimo = j

        vetor[i], vetor[indice_minimo] = vetor[indice_minimo], vetor[i]

vetor = [55, 29, 47, 25, 12]
ordenar_vetor(vetor)
print(f"Vetor ordenado em ordem crescente: {vetor}.")

## 02.

def ordenar_vetor(vetor, ordem):
    n = len(vetor)
    if ordem == 0:    
        for i in range(n):
            indice_minimo = i
            for j in range(i + 1, n):
                if vetor[j] < vetor[indice_minimo]:
                    indice_minimo = j
            vetor[i], vetor[indice_minimo] = vetor[indice_minimo], vetor[i]
    else:
        for i in range(n):
            indice_minimo = i
            for j in range(i + 1, n):
                if vetor[j] > vetor[indice_minimo]:
                    indice_minimo = j
            vetor[i], vetor[indice_minimo] = vetor[indice_minimo], vetor[i]


vetor=[5,7,4,3]
ordenar_vetor(vetor,0)
print(vetor)
ordenar_vetor(vetor,1)
print(vetor) 

## 03.

def encontrar_maximo(vetor):
    maximo = vetor[0]
    for elemento in vetor:
        if elemento > maximo:
            maximo = elemento
    return maximo

def encontrar_minimo(vetor):
    minimo = vetor[0]
    for elemento in vetor:
        if elemento < minimo:
            minimo = elemento
    return minimo

vetor=[5,7,4,3]

print(encontrar_maximo(vetor))
print(encontrar_minimo(vetor))

## 04.

def encontrar_segundo_menor(vetor):
    if len(vetor) < 2:
        return None
    
    menor = segundo_menor = float('inf')
    
    for numero in vetor:
        if numero < menor:
            segundo_menor = menor
            menor = numero
        elif menor < numero < segundo_menor:
            segundo_menor = numero
    
    return segundo_menor


vetor = [5, 7, 7, 4, 3]
segundo_menor_numero = encontrar_segundo_menor(vetor)

if segundo_menor_numero is not None:
    print(f"O segundo menor número é: {segundo_menor_numero}")
else:
    print("Não foi possível encontrar o segundo menor número no vetor.")

## 05.

def remover_duplicatas(vetor):
    vetor_s_d = []

    for numero in vetor:
        if numero not in vetor_s_d:
            vetor_s_d.append(numero)

    return vetor_s_d

vetor = [7, 8, 8, 4, 5, 3, 3, 1, 8]
vetor_s_d = remover_duplicatas(vetor)

print(f"Vetor anterior: {vetor}")
print(f"Vetor sem duplicatas: {vetor_s_d}")

## 06.

def selecao_ordenacao(vetor):
    n = len(vetor)
    for i in range(n):
        indice_minimo = i
        for j in range(i + 1, n):
            if vetor[j] < vetor[indice_minimo]:
                indice_minimo = j
        vetor[i], vetor[indice_minimo] = vetor[indice_minimo], vetor[i]

    c_pares = 0
    c_impares = 0

    for numero in vetor:
        if numero % 2 == 0:
            c_pares += 1
        else:
            c_impares += 1

    return c_pares, c_impares

vetor = [5, 7, 4, 3]
c_pares, c_impares = selecao_ordenacao(vetor)

print(f"Ordem crescente: {vetor}")
print(f"Quantidade de pares: {c_pares}")
print(f"Quantidade de impares: {c_impares}")

## 07.

def selecao_ordenacao(vetor):
    n = len(vetor)
    for i in range(n):
        indice_minimo = i
        for j in range(i + 1, n):
            if vetor[j] < vetor[indice_minimo]:
                indice_minimo = j
        vetor[i], vetor[indice_minimo] = vetor[indice_minimo], vetor[i]

def terceiro_maior(vetor):
    selecao_ordenacao(vetor)
    if len(vetor) < 3:
        print('Vetor menor que 3 elementos')
        return None
    
    return vetor[2]

vetor=[5,7,3]

print(f"O terceiro maior número é: {terceiro_maior(vetor)}")      

## 08.

def selecao_ordenacao(vetor):
    n = len(vetor)
    for i in range(n):
        indice_minimo = i
        for j in range(i + 1, n):
            if vetor[j] < vetor[indice_minimo]:
                indice_minimo = j
        vetor[i], vetor[indice_minimo] = vetor[indice_minimo], vetor[i]

def encontrar_mediana(vetor):
    selecao_ordenacao(vetor)
    n = len(vetor)

    # Se o número de vetores for ímpar:
    if n% 2 == 0:
        mediana = n // 2
        return vetor[mediana]
    
    # Se o número de vetores for par:
    mediana2 = (n - 1) // 2
    mediana3 = n // 2
    return (vetor[mediana2] + vetor[mediana3]) / 2

vetor = [5, 7, 4, 3]
resultado = encontrar_mediana(vetor)

print(f"A mediana do vetor é: {resultado}")