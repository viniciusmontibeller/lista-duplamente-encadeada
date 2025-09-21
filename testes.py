from lista_duplamente_encadeada import Elemento, ListaDuplamenteEncadeada

def print_lista(lista: ListaDuplamenteEncadeada, chavePrimeiroElemento: int):
    # Mostra os valores da lista.
    if lista.vazia():
        print("\nLista vazia")
        return

    achou = lista.buscar(chavePrimeiroElemento)
    if not achou:
        print(f"lista: valor inicial {chavePrimeiroElemento} não encontrado")
        return
    
    inicio = lista.acessarAtual()
    atual = inicio
    valores = []
    # Limite de tamanho para fins demonstrativos
    for _ in range(100):
        valores.append(atual.getValor())
        atual = atual.getProximo()
        if atual is inicio:
            break
    print("Lista: ", valores)

print("---- INÍCIO DOS TESTES ----")
lista = ListaDuplamenteEncadeada()
print("vazia?:", lista.vazia())

# 1) Operação relativa ao cursor em lista vazia (erro esperado)
print("\nTeste inserirAntesDoAtual em lista vazia (erro esperado)")
try:
    lista.inserirAntesDoAtual(Elemento(55))
except Exception as e:
    print("OK ->", repr(e))
print_lista(lista, 0)  # vazia

# 2) Inserções básicas
print("\nTeste inserirComoPrimeiro(10)")
lista.inserirComoPrimeiro(Elemento(10))
print("Cursor após inserirComoPrimeiro (esperado None):", lista.acessarAtual())
print_lista(lista, 10)

print("\nTeste inserirComoUltimo(20)")
lista.inserirComoUltimo(Elemento(20))
print("Cursor após inserirComoUltimo (esperado None):", lista.acessarAtual())
print_lista(lista, 10)

print("\nTeste inserirNaPosicao(1, 15)  # insere no meio")
lista.inserirNaPosicao(1, Elemento(15))
print("Cursor após inserirNaPosicao (esperado None):", lista.acessarAtual())
print_lista(lista, 10)

print("\nTeste inserirNaPosicao(0, 5)   # insere no inicio")
lista.inserirNaPosicao(0, Elemento(5))
print("Cursor após inserirNaPosicao (esperado None):", lista.acessarAtual())
print_lista(lista, 5)

print("\nTeste inserirNaPosicao(4, 25)  # insere no ultimo + 1, final da lista")
lista.inserirNaPosicao(4, Elemento(25))
print("Cursor após inserirNaPosicao (esperado None):", lista.acessarAtual())
print_lista(lista, 5)

# 3) posiçãoDe (existentes)
print("\nPosiçãoDe(5)  =", lista.posiçãoDe(5))
print("PosiçãoDe(15) =", lista.posiçãoDe(15))
print("PosiçãoDe(25) =", lista.posiçãoDe(25))
# após posiçãoDe cursor deve ser None
print("Cursor após posiçãoDe(25) (esperado None):", lista.acessarAtual())
print_lista(lista, 5)

# posiçãoDe (inexistente)
try:
    print("\nTeste inxistencia PosiçãoDe(999) =", lista.posiçãoDe(999))
except Exception as e:
    print("\nTeste inxistencia PosiçãoDe(999): OK ->", repr(e))
print("Cursor após posiçãoDe(999) (esperado None):", lista.acessarAtual())
print_lista(lista, 5)

# 4) buscar (existente e inexistente)
print("\nBusca existente(20)")
achou = lista.buscar(20)
print("Buscar(20) ->", achou, "; cursor:", lista.acessarAtual().getValor())

print("\nBusca inexistente(999)")
achou = lista.buscar(999)
print("Buscar(999) ->", achou, "; cursor:", lista.acessarAtual())
print_lista(lista, 5)

# 5) Operações relativas ao cursor (não zeram o cursor pelo desenho atual)
print("\nTeste inserirAntesDoAtual(13) com cursor em 15")
lista.buscar(15)  # seleciona 15
lista.inserirAntesDoAtual(Elemento(13))
print("Cursor após inserirAntesDoAtual (espera-se que aponte para 15 ainda):", lista.acessarAtual().getValor())
print_lista(lista, 5)

print("\nTeste inserirApósAtual(16) com cursor em 15")
lista.buscar(15)  # seleciona 15
lista.inserirApósAtual(Elemento(16))
print("Cursor após inserirApósAtual (espera-se que aponte para 15 ainda):", lista.acessarAtual().getValor())
print_lista(lista, 5)

# 6) excluirAtual após selecionar
print("\nTeste excluirAtual() removendo 15")
lista.buscar(15)
lista.excluirAtual()
# Exclusao do 15
print("Cursor após excluirAtual (esperado None):", lista.acessarAtual())
print_lista(lista, 5)

# 7) Exclusões por extremidade
print("\nTeste excluirPrim()")
lista.excluirPrim()
# primeiro elemento(5) foi removido
print("Cursor após excluirPrim (esperado None):", lista.acessarAtual())
print_lista(lista, 10)

print("\nTeste excluirUlt()")
lista.excluirUlt()
print("Cursor após excluirUlt (esperado None):", lista.acessarAtual())
print_lista(lista, 10)

# 8) Esvaziar lista completamente
print("\nTeste esvaziar com excluirPrim()")
while not lista.vazia():
    lista.excluirPrim()
print("Vazia?:", lista.vazia())

# 9) Erros esperados em vazia
print("\nErros esperados em lista vazia")
try:
    lista.excluirUlt()
except Exception as e:
    print("ExcluirUlt() ->", repr(e))
try:
    lista.inserirNaPosicao(1, Elemento(99))
except Exception as e:
    print("InserirNaPosicao(1, 99) ->", repr(e))
try:
    lista.inserirNaPosicao(-1, Elemento(100))
except Exception as e:
    print("InserirNaPosicao(-1, 100) ->", repr(e))

# 10) Caso unitário: 1 elemento e remover atual
print("\nTeste caso unitário 1 item na lista + excluirAtual")
listaUnitaria = ListaDuplamenteEncadeada()
listaUnitaria.inserirComoPrimeiro(Elemento(42))
listaUnitaria.buscar(42)
listaUnitaria.excluirAtual()
print_lista(listaUnitaria, 42)   # deve exibir []
print("Lista vazia?:", listaUnitaria.vazia())

print("\n ------ FIM DOS TESTES -------- ")