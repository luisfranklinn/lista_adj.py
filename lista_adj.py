#Na primeira linha do arquivo você define a quantidade de vértices e se é direcionado(D) ou não(N)
#Nas linhas abaixo, você insere no indice 0 o vértice 1 e no indice 1 o vértice 2


class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.grafo = [[] for i in range(self.vertices)]

    def loadLista(self):
        for i in range(len(lista)):
            linha = lista[i].split()
            if i == 0:
                Ori = linha[1]
            else:
                if Ori == "D":
                    self.grafo[int(linha[0]) - 1].append(int(linha[1]))
                else:
                    self.grafo[int(linha[0]) - 1].append(int(linha[1]))
                    self.grafo[int(linha[1]) - 1].append(int(linha[0]))
        arquivo.close()

    def imprime_lista(self):
        for i in range(self.vertices):
            print(f"Vértice {i+1}:", end="  ")
            for j in self.grafo[i]:
                print(f"{j}  -", end="  ")
            print("")



nome = input("Nome do arquivo: ")
arquivo = open(nome, "r")
lista = arquivo.readlines()
for i in range(len(lista)):
    linha = lista[i].split()
    if i == 0:
        g = Grafo(int(linha[0]))


g.loadLista()
g.imprime_lista()
