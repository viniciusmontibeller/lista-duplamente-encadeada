# Elemento é item de uma lista que apresenta apenas um valor unico a ele
# Para fins apenas de pratica, Elemento nao possui atributos de dados, apenas
# o valor unico pelo qual é identificado

class Elemento():
    def __init__(self, valor):
        self.__valor = valor
        self.__anterior = None
        self.__proximo = None
        
    def getValor(self):
        return self.__valor
    
    def setValor(self, valor):
        self.__valor = valor
        
    def getAnterior(self):
        return self.__anterior
    
    def setAnterior(self, anterior):
        self.__anterior = anterior
        
    def getProximo(self):
        return self.__proximo
    
    def setProximo(self, proximo):
        self.__proximo = proximo
        
        
# A lista duplamente encadeada e estruturada de maneira ciclica, ou seja, possui um inicio,
# e o ultimo elemento da lista referencia o primeiro.
# Por se tratar de fins de pratica, a lista nao possui tamanho definido, assumindo o funcionamento ideal de crescer indefinidamente.
# Porem isso nao sera tratado nesse exemplo.
class ListaDuplamenteEncadeada():
    def __init__(self):
        self.__inicio = None
        self.__cursor = None
        
        # Sem uso de sinalização de fim, pois o proximo do ultimo e o primeiro
        # e o anterior do primeiro e o ultimo, ou seja estao encadeados como
        # o resto da lista
        
    # Cursor aponta para o elemento atual
    def acessarAtual(self):
        return self.__cursor

    # Caso o cursor nao tenha nenhuma referencia dispara exceção
    # Usuario deve levar em conta que se a lista estiver vazia deve usar inserirComoPrimeiro() ou inserirComoUltimo(),
    # pois a inserção esta relacionado ao atual
    # Cursor permanecera no selecionado até ter ser explicitamente mudado ou outro metodo for usado
    def inserirAntesDoAtual(self, novo: Elemento):
        if self.__cursor is None:
            raise ValueError("Não há nenhum item selecionado")         
        elAnterior = self.__cursor.getAnterior()
        novo.setAnterior(elAnterior)
        novo.setProximo(self.__cursor)
        elAnterior.setProximo(novo)
        self.__cursor.setAnterior(novo)
        
        if self.__cursor is self.__inicio:
            self.__inicio = novo

    # Caso o cursor nao tenha nenhuma referencia dispara exceção
    # Usuario deve levar em conta que se a lista estiver vazia deve usar inserirComoPrimeiro() ou inserirComoUltimo()
    # pois a inserção esta relacionado ao atual
    # Cursor permanecera no selecionado até ter ser explicitamente mudado ou outro metodo for usado
    def inserirApósAtual(self, novo: Elemento):
        if self.__cursor is None:
            raise ValueError("Não há nenhum item selecionado")
        elSeguinte = self.__cursor.getProximo()
        novo.setProximo(elSeguinte)
        novo.setAnterior(self.__cursor)
        elSeguinte.setAnterior(novo)
        self.__cursor.setProximo(novo)
        
    # Coloca o cursor no final da lista e insere o novo elemento após o atual(ultimo)
    # Com uma lista vazia, o elemento e inserido como primerio e ultimo simultaneamente, assim sendo o seu proximo e anterior.
    # Caso nao esteja vazia insere depois do atual, que nesse caso e o ultimo elemento ja que o cursor foi direcionado para o final
    # Apos inserir elemento cursor volta ser None, pois nenhum item foi selecionado
    def inserirComoUltimo(self, novo: Elemento):
        self.__irParaUltimo()
        if self.__cursor is None:
            self.__inicio = novo
            novo.setProximo(novo)
            novo.setAnterior(novo)
        else:
            self.inserirApósAtual(novo)
            
        self.__cursor = None

    # Cursor vai ate o primeiro elemento e insere antes do atual.
    # Com uma lista vazia, o elemento e inserido como primerio e ultimo simultaneamente, assim sendo o seu proximo e anterior.
    # Caso nao esteja vazia insere antes do atual, que nesse caso e o primeiro ja que o cursor foi transportado para o inicio
    # Apos inserir elemento cursor volta ser None, pois nenhum item foi selecionado
    def inserirComoPrimeiro(self, novo: Elemento):
        self.__irParaPrimeiro()
        if self.__cursor is None:
            self.__inicio = novo
            novo.setProximo(novo)
            novo.setAnterior(novo)
        else:
            self.inserirAntesDoAtual(novo)
            self.__inicio = novo
            
        self.__cursor = None

    # Direciona o cursor para inicio
    # Avança o cursor para a posicao k
    # Insere o elemento antes do elemento atual
    # Dessa forma o novo elemento é inserido na posicao k e o cursor ficara na posicao k+1
    # Caso for inserido na primeira posicao usa-se inserirComoPrimeiro()
    # Caso a lsita esteja vazia e o numero escolhido seja 0(primeiro item) insere como primeiro
    # No caso da lista estar vazia, mas se escolhe uma posicao diferente da primeira, retorna excecao
    # No caso de inserir um elemento na na posicao ultimo + 1, ou seja, querer inserir ao final da lista
    # adiciona após o ultimo elemento
    # Caso a posicao seja do ultimo elemento é inserido no lugar e o ultimo aumenta uma posicao
    # Como estamos validando k, podemos utilizar o metodo avançarKPosições()
    # Apos inserir elemento cursor volta ser None, pois nenhum item foi selecionado
    def inserirNaPosicao(self, k, novo: Elemento):
        if k < 0:
            raise ValueError("Não é permitido numeros negativos")
        
        if self.vazia():
            if k is 0:
                self.inserirComoPrimeiro(novo)
                return
            raise IndexError("Posição fora dos limites da lista")
        
        if k is 0:
            self.inserirComoPrimeiro(novo)
            return
        
        self.__irParaUltimo()
        ultima_posicao = self.posiçãoDe(self.__cursor.getValor())
        
        if k > (ultima_posicao + 1):
            self.__cursor = None
            raise IndexError("Posição fora dos limites da lista")
        
        if k is (ultima_posicao + 1):
            self.__irParaUltimo()
            self.inserirApósAtual(novo)
            self.__cursor = None
            return

        self.__irParaPrimeiro()
        self.__avançarKPosições(k)
        self.inserirAntesDoAtual(novo)
        self.__cursor = None
        

    # Apos linkar o proximo elemento e o anterior, cursor volta a ser none, ou seja, nao existe mais elemento atual.
    # Sem referencia o elemento e elimindo da memoria pelo coletor de lixo.
    # Se o cursor não estiver selecionando nenhum item retorna excecao
    # Caso a exclusao seja feita quando se tem apenas um item, atual igual ao proximo, retira referencia ao elemento.
    # Caso o atual elemento seja o primeiro, remove e redireciona o inicio para o proximo.
    def excluirAtual(self):
        if self.__cursor is None:
            raise ValueError("Não há nenhum item selecionado")
        
        proximo = self.__cursor.getProximo()
        anterior = self.__cursor.getAnterior()
        
        if self.__cursor is proximo:
            self.__inicio = None
            self.__cursor = None
            return
        
        anterior.setProximo(proximo)
        proximo.setAnterior(anterior)
        
        if self.__cursor is self.__inicio:
            self.__inicio = proximo
        
        self.__cursor = None
        
    # Cursor vai ate o primeiro elemento e o atual e excluido deixa de existir e o cursor volta a ser None
    # Caso a lista esteja vazia o cursor sera None e lancara excecao
    def excluirPrim(self):
        self.__irParaPrimeiro()
        if self.__cursor is None:
            raise ValueError("Lista vazia")
        self.excluirAtual()
        
    # Cursor vai ate o ultimo elemento e o atual e excluido deixa de existir e o cursor volta a ser None
    # Caso a lista esteja vazia o cursor sera None e lancara excecao
    def excluirUlt(self):
        self.__irParaUltimo()
        if self.__cursor is None:
            raise ValueError("Lista vazia")
        self.excluirAtual()
        
    # Cria-se um elemento fake para garantir o elemento na lista, reduzindo a checagem por laço
    # Coloca-se o cursor no inicio para procurar em toda a lista
    # Cada iteração caso a chave passada não bata com o valor do elemento, o cursor avança para o proximo elemento
    # O laço no pior dos casos vai até o elemento fake criado
    # Caso o resultado da busca seja o fake, não foi encontrado nenhum elemento. Exclui o fake da lista e elemento atual/cursor volta a ser None e rertorna falso a busca
    # Caso encontre elemento, desolca o cursor para o fake, que e o ultimo, exclui ele, e volta o cursor no item encontrado, retornando verdadeiro.
    # Considerado apenas casos sincronos, sem concorrencia ou interrupção.
    # Para os casos acima necessario envolver em try/finally para sempre limpar o elemento fake.
    def buscar( self, chave ):
        fake = Elemento(chave)
        self.inserirComoUltimo(fake)
        self.__irParaPrimeiro()
        while self.__cursor.getValor() is not chave:
            self.__cursor = self.__cursor.getProximo()
        if self.__cursor is fake:
            self.excluirAtual()
            self.__cursor = None
            return False
        atual = self.__cursor
        self.__irParaUltimo()
        self.excluirAtual()
        self.__cursor = atual
        return True
        
    # Operaçãoes de controle, sem acesso do ussuario.
    
    # Checa se o cursor esta em algum item da lista para avançar
    # Avança o numero de posições k
    # Note que a checagem do valor k deve ser feita em metodos que utilizem essa opreção
    def __avançarKPosições( self, k ):
        if self.__cursor is None:
            raise IndexError("Não há nehum item selecionado")
        for _ in range(k):
            self.__cursor = self.__cursor.getProximo()
    
    # Checa se o cursor esta em algum item da lista para retroceder
    # Retrocede o numero de posicoes k
    # Note que a checagem do valor k deve ser feita em metodos que utilizem essa opreção
    def __retrocederKPosições ( self, k ):
        if self.__cursor is None:
            raise IndexError("Não há nehum item selecionado")
        for _ in range(k):
            self.__cursor = self.__cursor.getAnterior()
            
    def __irParaPrimeiro(self):
        self.__cursor = self.__inicio
        
    def __irParaUltimo(self):
        if self.vazia():
            self.__cursor = None
        else:
            self.__cursor = self.__inicio.getAnterior()

    # Nao possui verificação de lista cheia

    def vazia(self):
        return self.__inicio is None
        
    # Similar a busca, mas contendo um contador da posicao atual e retornando ela caso encontre.
    # Retorna a posicao encontrada e exclui o fake e direciona o cursor para None
    def posiçãoDe(self, chave):
        posicaoAtual = 0
        fake = Elemento(chave)
        self.inserirComoUltimo(fake)
        self.__cursor = self.__inicio
        while self.__cursor.getValor() is not chave:
            posicaoAtual += 1
            self.__cursor = self.__cursor.getProximo()
        if self.__cursor is fake:
            self.excluirAtual()
            self.__cursor = None
            raise ValueError("Item com essa chave não encontrado na lista.")
        self.__irParaUltimo()
        self.excluirAtual()
        self.__cursor = None
        return posicaoAtual