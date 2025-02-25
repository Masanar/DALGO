import sys

def explorarTorre2(alturas: list, altura_orion: int, mayor_menor, izq: int, der:int, actual:int):
    if izq > der:
        return mayor_menor 
    
    actual = (der + izq + 1)//2

    if alturas[actual] > altura_orion:
        mayor_menor = alturas[actual]
        mayor_menor = explorarTorre2(alturas, altura_orion, mayor_menor, izq, actual - 1, actual)

    else:
        mayor_menor = explorarTorre2(alturas, altura_orion, mayor_menor, actual + 1, der, actual)

    return mayor_menor
        
def explorarTorre1(alturas: list, altura_orion: int, menor_mayor, izq: int, der:int, actual:int):
    if izq > der:
        return menor_mayor
    
    actual = (der + izq + 1)//2
    
    if alturas[actual] < altura_orion:
        menor_mayor = alturas[actual]
        menor_mayor = explorarTorre1(alturas, altura_orion, menor_mayor, actual + 1, der, actual)
    
    else:
        menor_mayor = explorarTorre1(alturas, altura_orion, menor_mayor, izq, actual - 1, actual)

    return menor_mayor


def main():
    N = int(sys.stdin.readline().strip())
    alturas = list(map(int, sys.stdin.readline().split()))
    Q = int(sys.stdin.readline().strip())
    alturas_orion = list(map(int, sys.stdin.readline().split()))

    resultados = []
    for altura_orion in alturas_orion:
        menor = explorarTorre1(alturas, altura_orion, "X", 0, N - 1, 0)
        mayor = explorarTorre2(alturas, altura_orion, "X", 0, N - 1, 0)
        resultados.append(f"{menor} {mayor}")

    print("\n".join(resultados) + "\n")

main()