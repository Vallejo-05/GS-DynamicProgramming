
# FASE 1 – ABORDAGEM GULOSA

projects = [
    ("A", 12, 4),
    ("B", 10, 3),
    ("C", 7, 2),
    ("D", 4, 3)
]

CAPACITY = 10

def greedy_selection(projects, capacity):
    sorted_projects = sorted(projects, key=lambda p: p[1] / p[2], reverse=True)
    
    total_value = 0
    chosen = []
    remaining = capacity

    for name, value, cost in sorted_projects:
        if cost <= remaining:
            chosen.append(name)
            total_value += value
            remaining -= cost
    
    return chosen, total_value

print("Fase 1 (Greedy):", greedy_selection(projects, CAPACITY))


# FASE 2 – RECURSÃO PURA 

def recursive_knapsack(i, capacity, projects):
    if i == 0 or capacity == 0:
        return 0

    name, value, cost = projects[i - 1]


    option1 = recursive_knapsack(i - 1, capacity, projects)


    if cost <= capacity:
        option2 = value + recursive_knapsack(i - 1, capacity - cost, projects)
        return max(option1, option2)
    else:
        return option1

print("Fase 2 (Recursiva):", recursive_knapsack(len(projects), CAPACITY, projects))


# FASE 3 – TOP-DOWN COM MEMOIZAÇÃO

def memo_knapsack(i, capacity, projects, memo):
    if (i, capacity) in memo:
        return memo[(i, capacity)]

    if i == 0 or capacity == 0:
        return 0

    name, value, cost = projects[i - 1]

    option1 = memo_knapsack(i - 1, capacity, projects, memo)

    if cost <= capacity:
        option2 = value + memo_knapsack(i - 1, capacity - cost, projects, memo)
        best = max(option1, option2)
    else:
        best = option1

    memo[(i, capacity)] = best
    return best


memo = {}
print("Fase 3 (Memoização):", memo_knapsack(len(projects), CAPACITY, projects, memo))


# FASE 4 – BOTTOM-UP (ITERATIVA)

def bottomup_knapsack(projects, capacity):
    n = len(projects)
    T = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        name, value, cost = projects[i - 1]
        for c in range(1, capacity + 1):
            if cost <= c:
                T[i][c] = max(
                    T[i - 1][c],                
                    value + T[i - 1][c - cost] 
                )
            else:
                T[i][c] = T[i - 1][c]

    return T[n][capacity]

print("Fase 4 (Bottom-Up):", bottomup_knapsack(projects, CAPACITY))
