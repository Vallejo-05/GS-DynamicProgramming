# 📘 Global Solution 2025
## Dynamic Programming

---

## 👨‍🏫 Informações do Projeto

**Curso:** Engenharia de Software  
**Disciplina:** Dynamic Programming  
**Semestre:** 2º Semestre / 2025  
**Tema:** O Futuro do Trabalho  

---

# 👥 Integrantes do Grupo

| Nome | RM |
|------|------|
| Gabriel Guerreiro Escobosa Vallejo | 554973 |
| Lucas Catroppa Piratininga Dias | 555540 |
| Luiz Felipe Coelho Ramos | 555074 |


---

# 🎯 Objetivo

Este projeto implementa a **Otimização de Portfólio de Projetos** utilizando quatro abordagens de Programação Dinâmica e resolução de problemas combinatórios, conforme solicitado no enunciado da Global Solution.

A empresa possui uma capacidade limitada de **Horas-Especialista**, e precisa decidir quais projetos aceitar para **maximizar o valor total** sem ultrapassar o limite disponível.

Este problema corresponde diretamente ao clássico **0/1 Knapsack Problem**.

---

# 📊 Dados Utilizados

Capacidade total:

```
C = 10 horas
```

Projetos:

| Projeto | Valor (V) | Horas (E) |
|--------|-----------|-----------|
| A | 12 | 4 |
| B | 10 | 3 |
| C | 7 | 2 |
| D | 4 | 3 |

---

# 🧠 Fases da Implementação

O projeto possui quatro funções principais, cada uma representando uma abordagem diferente de resolução:

---

## 🟦 Fase 1 – Estratégia Gulosa (Greedy)

A estratégia gulosa utiliza a regra:

### **Selecionar projetos pela maior razão Valor/Horas (V/E)**.

É intuitiva, rápida e eficiente, mas **NÃO garante o resultado ótimo**, servindo como ponto de comparação com as abordagens de Programação Dinâmica.

---

## 🟩 Fase 2 – Solução Recursiva Pura (Força Bruta)

Implementa a solução recursiva clássica, testando **todas as combinações** de projetos.

Para cada projeto:

- Incluir  
- Não incluir  

É garantidamente ótima, mas extremamente ineficiente:

- Tempo: **O(2ⁿ)**  
- Mostra a redundância de chamadas recursivas.

---

## 🟧 Fase 3 – Programação Dinâmica Top-Down (Memoização)

Mesma lógica da recursiva, porém com **armazenamento de subproblemas (memo)**.

Quando `(i, capacidade)` aparece novamente, o valor já calculado é retornado imediatamente.

- Tempo: **O(N × C)**  
- Método recursivo otimizado  
- Evita recomputação

---

## 🟥 Fase 4 – Programação Dinâmica Bottom-Up (Iterativa)

Constrói uma **tabela completa** onde:

`T[i][c] = melhor valor possível usando os i primeiros projetos e capacidade c`

Essa é a abordagem:

- mais eficiente  
- mais usada em aplicações reais  
- garantidamente ótima  
- não usa recursão  

Tempo: **O(N × C)**

---

# 🧪 Casos de Teste

O projeto inclui pelo menos 4 cenários utilizados para validação:

1. Dados oficiais do enunciado  
2. Capacidade insuficiente  
3. Capacidade exata  
4. Caso onde a abordagem gulosa **falha** e a Programação Dinâmica encontra o valor ótimo  

---

# 🧮 Complexidade das Abordagens

| Fase | Método | Tempo | Espaço |
|------|--------|--------|---------|
| 1 | Greedy | O(N log N) | O(1) |
| 2 | Recursiva Pura | O(2ⁿ) | O(N) |
| 3 | Top-Down | O(N × C) | O(N × C) |
| 4 | Bottom-Up | O(N × C) | O(N × C) |

A abordagem mais eficiente é a **Bottom-Up (Iterativa)**.

---


# ▶️ Como Executar

1. Baixe o repositório.


2. Execute o arquivo principal:

```bash
python main.py
```

3. O terminal exibirá o resultado das **4 fases**.

---

# 🎉 Conclusão

Este projeto demonstra na prática:

- A falha de abordagens gulosas  
- A força da Programação Dinâmica  
- A diferença entre soluções recursivas, memoizadas e iterativas  
- A aplicação real do Problema da Mochila (Knapsack) no contexto de negócios
