class numeriComplessi:
    ' Common base class for complex number\'s operation '

    def __init__(self, pReale, pImmaginaria):
        self.pReale = pReale
        self.pImmaginaria = pImmaginaria

    def displayComplessi(self):
        complesso = self.pReale + '+' + self.pImmaginaria





def inserisciNumero(x,cmx):
    nReale = raw_input('Parte Reale: ')
    nImm = raw_input('Parte Immaginaria: ')
    cmx[x]=numeriComplessi(nReale,nImm)
def mostraNumeri(x):
    for i in range(x):
        i.displayComplessi()
def printMenu():
    print '''
    1) Inserisci numero complesso
    2) Somma
    3) Sottrazione
    4) Moltiplicazione
    5) Divisione
    6) Visualizza numeri complessi
    7) Goodbye
    '''
print numeriComplessi.__name__
counter=0
complesso=[]
inserisciNumero(counter,complesso)
while True:
    printMenu()
    insert = raw_input('Scelta>> ')
    if insert == '1':
        counter += 1
        inserisciNumero(counter,complesso)
    elif insert == 2:
        mostraNumeri(counter,complesso)
    elif insert == 3:
        quit()