#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Función booleana para saber si los primeros k 
# elementos de a forman una solución completa 
# para UNA solución del problema
def is_a_solution(a:list,k:int,additional_input:int) -> bool:
    return k == additional_input-1

# Asigna valores a c con el posible conjunto de
# valores candidatos para la posición k de a, 
# basados en las k-1 posiciones. El numero de
# candidatos es retornado en nc.
def construct_candidates(a:list,k:int,additional_input:int,c:list) -> int:
    c[0] = True
    c[1] = False
    return 2

# Guarda, 'printea', cuenta o procesa la solución
def process_solution(a:list,k:int,additional_input: int) -> None:
    print('{',end='')
    for i in range(len(a)):
        if a[i]:
            print(f' {i}',end='')
    print(' }')

def backtrack(a: list, k: int, additional_input: int) -> None:
    c = [False for _ in range(2)]
    nc = 0
    if is_a_solution(a,k,additional_input):
        process_solution(a,k,additional_input)
    else:
        k = k + 1
        nc = construct_candidates(a,k,additional_input,c)
        for i in range(0,nc):
            a[k] = c[i]
            backtrack(a,k,additional_input)

def generate_subsets(n:int):
    a = [-1 for _ in range(n)]
    backtrack(a,-1,n)

generate_subsets(4)

    




