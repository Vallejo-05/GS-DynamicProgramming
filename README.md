# 📘 Global Solution – Dynamic Programming  
### Otimização no futuro do trabalho
**FIAP – Engenharia de Software – 2025**  
**Disciplina:** Dynamic Programming  

---

# 👥 Integrantes do Grupo

| Nome | RM |
|------|------|
| Gabriel Guerreiro Escobosa Vallejo | 554973 |
| Lucas Catroppa Piratininga Dias | 555540 |
| Luiz Felipe Coelho Ramos | 555074 |

---

## 📌 Descrição do Projeto

Este projeto implementa uma solução completa do **Problema da Mochila 0/1 (0/1 Knapsack)** aplicada a iniciativas estratégicas, onde cada projeto possui:

- **Impacto** (valor/retorno)
- **Horas requeridas** (custo)
- **Capacidade máxima** (horas totais disponíveis)

O objetivo é selecionar o melhor conjunto de iniciativas que **maximiza o impacto total**, sem ultrapassar as horas disponíveis.

O desenvolvimento segue exatamente **as quatro fases obrigatórias** do enunciado da Global Solution.

---

## 🧩 Modelagem

Cada iniciativa é representada pela seguinte classe:

```python
@dataclass(frozen=True)
class Iniciativa:
    nome_projeto: str
    impacto: int
    horas_requeridas: int
```

---

## 🚀 Fase 1 — Estratégia Gulosa (Greedy)

### 📘 Descrição
Seleciona repetidamente a iniciativa com maior razão impacto/horas.  
Não garante solução ótima.

### 🕒 Complexidade
O(n²)

### 📁 Função

```python
seleciona_por_eficiencia()
```

---

## 🔁 Fase 2 — Recursiva Pura

### 📘 Descrição
Explora todas as combinações possíveis (força bruta).  
A solução é dividida em:
1. Cálculo do valor ótimo  
2. Reconstrução dos itens

### 🕒 Complexidade
O(2ⁿ)

### 📁 Função

```python
otimizacao_recursiva()
```

---

## 🧠 Fase 3 — Programação Dinâmica Top-Down (Memoização)

### 📘 Descrição
Versão otimizada da recursiva, utilizando memoização.

### 🕒 Complexidade
O(n * C)

### 📁 Função

```python
otimizacao_topdown()
```

---

## 📊 Fase 4 — Programação Dinâmica Bottom-Up (Iterativa)

### 📘 Descrição
Monta uma tabela DP e resolve iterativamente.

### 🕒 Complexidade
O(n * C)

### 📁 Função

```python
otimizacao_bottomup()
```

---

## 🧪 Testes

Inclui três cenários:

- Exemplo do enunciado  
- Caso onde Greedy falha  
- Caso com múltiplas soluções ótimas

---

## 📈 Exemplo de Saída

```
--- Exemplo do Enunciado ---
Greedy:     29 ['A', 'B', 'C']
Recursiva:  29 ['A', 'B', 'C']
Top-Down:   29 ['A', 'B', 'C']
Bottom-Up:  29 ['A', 'B', 'C']
```

---

## 🧮 Tabela de Complexidades

| Fase | Estratégia | Complexidade |
|------|------------|--------------|
| 1 | Greedy | O(n²) |
| 2 | Recursiva | O(2ⁿ) |
| 3 | Top-Down | O(n * C) |
| 4 | Bottom-Up | O(n * C) |

---

## 🎯 Conclusão

O projeto implementa as quatro fases exigidas, seguindo boas práticas, documentação clara e soluções completas de programação dinâmica.
