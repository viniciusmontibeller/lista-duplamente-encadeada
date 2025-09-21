# Lista Duplamente Encadeada Circular (com Cursor)

Implementação de uma **lista duplamente encadeada _circular_** em Python, usando um **cursor** para operações relativas ao “elemento atual”. O projeto é didático e assume **valores únicos** para cada `Elemento`, sem levar em consideração acessar informação do elemento.

> **Ideia-chave:** a estrutura é circular (o `próximo` do último aponta para o primeiro e o `anterior` do primeiro aponta para o último). Um **cursor** pode (ou não) apontar para um item; algumas operações exigem que o cursor esteja selecionado.

## Sumário

- [Visão geral](#visão-geral)  
- [Comportamento](#comportamento)
- [Classes](#classes)
- [Exemplos rápidos](#exemplos-rápidos)  
- [Testes](#testes)
- [Limitações](#boas-práticas-e-limitações)  
- [Ideias alternativas](#ideias-de-evolução)

## Visão geral

- **Circular:** não há `None` nas pontas; a lista “fecha” em si mesma.  
- **Duplamente encadeada:** cada item aponta para o **anterior** e para o **próximo**.  
- **Cursor:** ponteiro para o “elemento atual”. Algumas operações são **relativas ao cursor** (inserir antes/depois, excluir atual).  
- **Valores únicos:** cada `Elemento` guarda um único `valor` e assume-se que **não há duplicatas**.

## Comportamento

### Seleção do cursor
- **Inserções públicas por posição:**  
  `inserirComoPrimeiro`, `inserirComoUltimo`, `inserirNaPosicao`  
  → **não deixam** nenhum item selecionado ao final (**cursor = None**).
- **Inserções relativas ao cursor:**  
  `inserirAntesDoAtual`, `inserirApósAtual`  
  → **preservam** a seleção (o cursor permanece onde estava).
- **Exclusões:**  
  `excluirAtual`, `excluirPrim`, `excluirUlt`  
  → **não deixam** item selecionado (**cursor = None**).

### Busca e posição (sentinela “fake”)
- `buscar(valor)` cria temporariamente um **fake** para garantir término do laço com **uma única comparação por iteração**.  
  - **Retorna `True`** e **deixa o cursor no item encontrado**; ou  
  - **Retorna `False`** e **cursor = None**.  
  O **fake** é removido antes de terminar.
- `posiçãoDe(valor)` retorna o índice (0-based).  
  - Se **não encontrar**, lança `ValueError`.  
  - Se **encontrar**, **deixa o cursor no item encontrado**.

### Exclusão do único elemento
- Em `excluirAtual`, se `atual.getProximo() is atual`, a lista torna-se vazia (`__inicio = None`, **cursor = None**).

> Foi estruturado de maneira que o cursor deve ser explicitamente alocado para evitar modificações na lista por acidente, cursor residual indesejado.

## Classes

### Classe `Elemento`

- `getValor()` / `setValor(v)`  
- `getAnterior()` / `setAnterior(no)`  
- `getProximo()` / `setProximo(no)`

> Classe de item simples; o projeto é didático e usa getters/setters.

### Classe `ListaDuplamenteEncadeada`

#### Acesso/estado
- `vazia() -> bool`  
- `acessarAtual() -> Elemento | None`

#### Inserções **públicas** (cursor **fica `None`** ao final)
- `inserirComoPrimeiro(novo: Elemento)`  
- `inserirComoUltimo(novo: Elemento)`  
- `inserirNaPosicao(k: int, novo: Elemento)`  
  - `k == 0` → insere na cabeça  
  - `k == tamanho` → **append** (insere após o último)  
  - `k < 0` → `ValueError`  
  - `k > tamanho` → `IndexError`

#### Inserções **relativas ao cursor** (cursor **permanece selecionado**)
- `inserirAntesDoAtual(novo: Elemento)` → exige cursor selecionado, senão `ValueError`  
- `inserirApósAtual(novo: Elemento)` → exige cursor selecionado, senão `ValueError`

#### Exclusões (cursor **fica `None`**)
- `excluirAtual()` → exige cursor selecionado, senão `ValueError`  
- `excluirPrim()` → lista vazia lança `ValueError`  
- `excluirUlt()` → lista vazia lança `ValueError`

#### Busca/posição (com sentinela “fake”)
- `buscar(valor) -> bool`  
  - `True`: cursor no item encontrado  
  - `False`: cursor `None`
- `posiçãoDe(valor) -> int`  
  - Se não achar: `ValueError("Item com essa chave não encontrado na lista.")`  
  - Se achar: cursor no item encontrado

## Exemplos rápidos

```python
from lista_duplamente_encadeada import Elemento, ListaDuplamenteEncadeada

L = ListaDuplamenteEncadeada()

# Inserções básicas (cursor = None após cada uma)
L.inserirComoPrimeiro(Elemento(10))
L.inserirComoUltimo(Elemento(20))
L.inserirNaPosicao(1, Elemento(15))  # 10, 15, 20
L.inserirNaPosicao(0, Elemento(5))   # 5, 10, 15, 20
L.inserirNaPosicao(4, Elemento(25))  # append -> 5, 10, 15, 20, 25

# Buscar (cursor fica no encontrado)
if L.buscar(15):
    atual = L.acessarAtual()            # item com valor 15
    L.inserirApósAtual(Elemento(16))    # 16 após o 15 (cursor preservado)

# Excluir atual (cursor deve estar selecionado)
L.buscar(10)
L.excluirAtual()  # remove o 10; cursor = None
```

## Testes
O projeto inclui um arquivo de testes por prints que exercita as operações e imprime o estado da lista a cada passo

### Requisitos: 
1) Python 3.8+ (recomendado)
2) Estrutura: lista_duplamente_encadeada.py
3) Testes: testes.py

```
python testes.py
# ou
python3 testes.py
```

> **Nota**: print_lista chama buscar, então move a seleção do cursor — isso é intencional no contexto de testes, apenas para imprimir a partir de um valor conhecido.

## Limitações
* Como o cursor sempre deve ser explicitamente apontado, existe uma atribuição do cursor prévia para os métodos relativos.

* Exceção: Casos especificos lançam exceções mas não as tratam, usuário deve tratar exceções.

* Suporte apenas uma Thread: evite concorrência sobre a mesma instância.

* Sentinela “fake”: no fluxo normal ele é sempre removido. Poderia sobrar apenas em interrupções assíncronas (ex.: KeyboardInterrupt) ou se a lista for corrompidos por código externo.

## Ideias alternativas

* Pode-se interpretar o cursor como o caret de digitação, facilitando e agilizando operações sobre o cursor, dando mais fluidez para o usuário, porém com maior risco de erros.
  * Cursor sempre estara em algum ponto da lista, fora a lista vazia.
  * Nesse caso, com inclusões e exclusoes o cursor vai para o item adjacente.

* Pode-se ainda ter um contador dentro da lista, com a finalizadade de facilitar operações de posição.