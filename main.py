from dataclasses import dataclass
from typing import List, Tuple, Dict

# Modelo de Iniciativa
@dataclass(frozen=True)
class Iniciativa:
    nome_projeto: str
    impacto: int         
    horas_requeridas: int 


# FASE 1 — Estratégia Gulosa 
def seleciona_por_eficiencia(iniciativas: List[Iniciativa], capacidade: int) -> Tuple[int, List[Iniciativa]]:
    """
    Estratégia gulosa: escolhe repetidamente o projeto mais eficiente que ainda cabe.
    Complexidade: O(n^2) no pior caso (busca repetida).
    """
    restantes = iniciativas[:]
    escolhidos, total, usadas = [], 0, 0

    while restantes and usadas < capacidade:
        candidatos = [p for p in restantes if p.horas_requeridas + usadas <= capacidade]
        if not candidatos:
            break
        melhor = max(candidatos, key=lambda x: x.impacto / x.horas_requeridas)
        escolhidos.append(melhor)
        usadas += melhor.horas_requeridas
        total += melhor.impacto
        restantes.remove(melhor)

    return total, escolhidos


# FASE 2 — Solução Recursiva Pura
def otimizacao_recursiva(iniciativas: List[Iniciativa], capacidade: int) -> Tuple[int, List[Iniciativa]]:
    """
    Recursiva pura: calcula valor ótimo e depois reconstrói itens.
    Complexidade: O(2^n).
    """
    n = len(iniciativas)

    def valor(i: int, cap: int) -> int:
        if i == 0 or cap == 0:
            return 0
        atual = iniciativas[i - 1]
        if atual.horas_requeridas > cap:
            return valor(i - 1, cap)
        return max(valor(i - 1, cap),
                   atual.impacto + valor(i - 1, cap - atual.horas_requeridas))

    def reconstrucao(i: int, cap: int) -> List[Iniciativa]:
        if i == 0 or cap == 0:
            return []
        atual = iniciativas[i - 1]
        if atual.horas_requeridas > cap:
            return reconstrucao(i - 1, cap)
        if valor(i, cap) == valor(i - 1, cap):
            return reconstrucao(i - 1, cap)
        else:
            return reconstrucao(i - 1, cap - atual.horas_requeridas) + [atual]

    return valor(n, capacidade), reconstrucao(n, capacidade)


# FASE 3 — Programação Dinâmica Top-Down 
def otimizacao_topdown(iniciativas: List[Iniciativa], capacidade: int) -> Tuple[int, List[Iniciativa]]:
    """
    Top-Down com memoização: armazena apenas valores.
    Reconstrução feita separadamente.
    Complexidade: O(n * C).
    """
    n = len(iniciativas)
    memo: Dict[Tuple[int, int], int] = {}

    def valor(i: int, cap: int) -> int:
        if i == 0 or cap == 0:
            return 0
        if (i, cap) in memo:
            return memo[(i, cap)]
        atual = iniciativas[i - 1]
        if atual.horas_requeridas > cap:
            res = valor(i - 1, cap)
        else:
            res = max(valor(i - 1, cap),
                      atual.impacto + valor(i - 1, cap - atual.horas_requeridas))
        memo[(i, cap)] = res
        return res

    def reconstrucao(i: int, cap: int) -> List[Iniciativa]:
        if i == 0 or cap == 0:
            return []
        atual = iniciativas[i - 1]
        if atual.horas_requeridas > cap or valor(i, cap) == valor(i - 1, cap):
            return reconstrucao(i - 1, cap)
        else:
            return reconstrucao(i - 1, cap - atual.horas_requeridas) + [atual]

    return valor(n, capacidade), reconstrucao(n, capacidade)


# FASE 4 — Programação Dinâmica Bottom-Up 
def otimizacao_bottomup(iniciativas: List[Iniciativa], capacidade: int) -> Tuple[int, List[Iniciativa]]:
    """
    Bottom-Up com matriz de escolhas.
    Complexidade: O(n * C).
    """
    n = len(iniciativas)
    DP = [[0] * (capacidade + 1) for _ in range(n + 1)]
    escolha = [[False] * (capacidade + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        impacto = iniciativas[i - 1].impacto
        horas = iniciativas[i - 1].horas_requeridas
        for cap in range(capacidade + 1):
            if horas <= cap and impacto + DP[i - 1][cap - horas] > DP[i - 1][cap]:
                DP[i][cap] = impacto + DP[i - 1][cap - horas]
                escolha[i][cap] = True
            else:
                DP[i][cap] = DP[i - 1][cap]

    escolhidos = []
    cap = capacidade
    for i in range(n, 0, -1):
        if escolha[i][cap]:
            escolhidos.append(iniciativas[i - 1])
            cap -= iniciativas[i - 1].horas_requeridas

    escolhidos.reverse()
    return DP[n][capacidade], escolhidos


# TESTES
if __name__ == "__main__":
    testes = [
        ("Exemplo do Enunciado", 
         [Iniciativa("A", 12, 4), Iniciativa("B", 10, 3), Iniciativa("C", 7, 2), Iniciativa("D", 4, 3)], 10),

        ("Greedy falha (ótimo é B+C=220)", 
         [Iniciativa("A", 60, 10), Iniciativa("B", 100, 20), Iniciativa("C", 120, 30)], 50),

        ("Múltiplos ótimos (X=90 ou Y+Z=90)", 
         [Iniciativa("X", 90, 9), Iniciativa("Y", 40, 5), Iniciativa("Z", 50, 5), Iniciativa("W", 30, 3)], 10),
    ]

    for titulo, iniciativas, capacidade in testes:
        print(f"\n--- {titulo} ---")
        g_val, g_itens = seleciona_por_eficiencia(iniciativas, capacidade)
        print("Greedy:", g_val, [p.nome_projeto for p in g_itens])

        r_val, r_itens = otimizacao_recursiva(iniciativas, capacidade)
        print("Recursiva:", r_val, [p.nome_projeto for p in r_itens])

        t_val, t_itens = otimizacao_topdown(iniciativas, capacidade)
        print("Top-Down:", t_val, [p.nome_projeto for p in t_itens])

        b_val, b_itens = otimizacao_bottomup(iniciativas, capacidade)
        print("Bottom-Up:", b_val, [p.nome_projeto for p in b_itens])


