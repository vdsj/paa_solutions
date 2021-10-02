class Hamiltonian:
    def __init__(self, start):
        self.start = start #inicia e finaliza vertice
        self.cycle = [] #lista para armazenar os caminhos do cycle4
        self.have_cycle = False #Marca se o grafo conhave cycle

    
    def find_cycle.(self):
        self.cycle.append(self.start) 
        self.backtrack(self.start)
        if not self.have_cycle:
            print("Sem caminhos")

    #continua a procurar mais cycles
    def backtrack(self, vertice):
        if (vertice == self.start and len(self.cycle) == nvert+1):
            self.have_cycle = True
            return

        #itera os vértices neighbors
        for i in range(len(vert)): #itera os vértices neighbors 
            if (matrizAdjc[vertice][i] == 1 and vert[i] == 0):
                neighbor = i
                vert[neighbor] = 1 #visita e adiciona vertice ao cycle
                self.cycle.append(neighbor)
                self.backtrack(neighbor) # chamada recursiva com o neighbor para encontrar cycle
                vert[neighbor] = 0 #Backtrack
                self.cycle.pop()
