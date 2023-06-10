"""
Esercizio Sudoku (tema d'esame t2013-01-31)

Soluzione:
    - Parto da una lista con dentro una matrice Base in cui i numeri sono tutti zero;
    - Calcolo i possibili numeri al posto del primo zero;
    - Aggiungo alla lista una copia della matrice per ognuno di essi, sostituendo lo zero;
    - Se non ci sono zeri e' completa, quindi la restituisco con yield;
    - Tolgo la matrice dalla lista e ricomincio il ciclo
"""

class Sudoku:
    """Schema Sudoku 4 x 4"""
    def __init__(self,S): #S deve essere matrice 4 x 4
        self.S = S
    def matrix(self):
        return [row.copy() for row in self.S] #restituisco una copia di S
    def possibili(self,i,j):
        Row = self.S[i]
        Col = [self.S[x][j] for x in range(4)]
        Qua = [self.S[x+(i//2)*2][y+(j//2)*2] \
            for x in range(2) for y in range(2)]
        return {1,2,3,4} - set(Col+Row+Qua) #trovo i numeri che potrebbero stare in S[i][j]
    def zero(self):
        for x in range(4):
            try: return [x,self.S[x].index(0)] #coordinate del primo zero in S
            except: pass
        return False #non ci sono zeri

def risolutore(lista):
    while len(lista)>0:
        A=lista[0] #A e' un oggetto di classe Sudoku
        zero = A.zero()
        if not zero:
            yield A.matrix() #matrice completa
        else:
            #sostituzione e aggiornamento della lista:
            [i,j] = zero
            m=(A.matrix())
            M = Sudoku(m)
            for x in A.possibili(i,j):
                m[i][j] = x
                lista.append(Sudoku(M.matrix()))
        lista.pop(0)

if __name__=="__main__":
    print ("\n")
    
    Base = Sudoku([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
    for soluzione in list(risolutore([Base])):
       print (soluzione)
    
    print ("\n")
