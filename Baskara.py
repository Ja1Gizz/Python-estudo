def delta(a, b, c):
    return (b * b) - (4 * a * c)


def maior(num1, num2):

    if num1 > num2:
        return num1
    else:
        return num2


def menor(num1, num2, num3):

    menor = num1

    if num2 < menor:
        menor = num2

    if num3 < menor:
        menor = num3

    return menor


def crescente(a, b):

    if a < b:
        print(a, b)
    else:
        print(b, a)


def soma(lista):

    s = 0

    for numero in lista:
        s += numero

    return s


def media(lista):

    return soma(lista) / len(lista)


def maior_lista(lista):

    maior = lista[0]

    for numero in lista:

        if numero > maior:
            maior = numero

    return maior


opcao = -1

while opcao != 0:

    print("\n1 - Delta")
    print("2 - Maior número")
    print("3 - Menor número")
    print("4 - Ordem crescente")
    print("5 - Somar lista")
    print("6 - Média")
    print("7 - Maior da lista")
    print("0 - Sair")

    opcao = int(input("Escolha: "))

    if opcao == 1:

        a = int(input("Digite A: "))
        b = int(input("Digite B: "))
        c = int(input("Digite C: "))

        print("Delta =", delta(a, b, c))

    elif opcao == 2:

        n1 = int(input("Número 1: "))
        n2 = int(input("Número 2: "))

        print("Maior:", maior(n1, n2))

    elif opcao == 3:

        n1 = int(input("Número 1: "))
        n2 = int(input("Número 2: "))
        n3 = int(input("Número 3: "))

        print("Menor:", menor(n1, n2, n3))

    elif opcao == 4:

        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo valor: "))

        print("Ordem crescente:")
        crescente(n1, n2)

    elif opcao == 5:

        lista = [5, 8, 2]

        print("Resultado da soma:", soma(lista))

    elif opcao == 6:

        lista = [5, 8, 2]

        print("Média da lista:", media(lista))

    elif opcao == 7:

        lista = [5, 8, 2]

        print("Maior valor:", maior_lista(lista))

    elif opcao == 0:

        print("Fim do programa")

    else:
        print("Opção inválida")
