import re
conv = {'a':2,'b':2,'c':2,'d':3,'e':3, \
        'f':3,'g':4,'h':4,'i':4,'j':5, \
        'k':5,'l':5,'m':6,'n':6,'o':6, \
        'p':7,'q':7,'r':7,'s':7,'t':8, \
        'u':8,'v':8,'w':9,'x':9,'y':9,'z':9,' ':0}

str2num = lambda string : "".join([str(conv[c]) for c in string])

#print(str2num('dai diamanti non nasce niente dal letame nascono i fiori'))
#print(str2num('ma io sono fiero del mio sognare di questo eterno mio incespicare'))

def file_read(filename):
    'generatore che legge le righe del file'
    with open(filename, encoding = 'utf-8') as file:
        for line in file:
            try:
                yield re.match('[0-9a-z ]+',line).group(0)
            except:
                print("errore nella lettura del file " + filename)

def leggi_dizionario(filename):
    "funzione che crea dizionario nel formato {,,1:['a','b','c'],,,,}"
    dizionario={}
    for line in file_read(filename):
        num = str2num(line)#converte parola in numero
        if num in dizionario:
            dizionario[num].append(line)#aggiunge parola alla lista
        else:
            dizionario[num] = [line]#crea nuova lista con chiave num
    return dizionario

def prodotto(list1,list2):
    "prodotto cartesiano fra due liste di stringhe"
    return [l1 + ' ' + l2 for l1 in list1 for l2 in list2]


if __name__ == "__main__":
    
    dizionario = leggi_dizionario('italiano.txt')#crea dizionario
    for text in file_read("texts.txt"):
        text=text.split()#text->[1,325,643683]
        for i in range(len(text)):
            text[i] = dizionario[text[i]]#text->[[a,b,c],[dal],[niente]]
        while len(text) > 1:
            #finche' text non contiene una sola lista
            #sostituisco le prime due con il loro prodotto cartesiano
            text.insert(0,prodotto(text.pop(0),text.pop(0)))

        #stampa tutte le combinazioni di una frase:
        print("\n===============================================")
        for t in text[0]:
            print(t)
