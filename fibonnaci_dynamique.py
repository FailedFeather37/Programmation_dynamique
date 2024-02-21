from random import randint


def fibonacci(n):
    if n==1:
        return n
    elif n==0:
        return n
    else:
        return(fibonacci(n-1)+fibonacci(n-2))



def fibo_dynamique(n,l,a=0):
    if l[n]!=None:
        return n
    elif l[n]==None:
        l[n]=n
        return n
    else:
        return(fibonacci(n-1)+fibonacci(n-2))


class arbre():
    def __init__(self,valeur,gauche=None,droite=None):
        self.valeur=valeur
        self.gauche=gauche
        self.droite=droite

    def remplissage(self):
        global liste
        self.gauche=liste[0]
        self.droite=liste[1]


def liste_nombre():
    l=[]
    for i in range(10):
        l.append(randint(1,20))
    return l


if __name__=="__main__":
    #print(fibonacci(35))
    n=35
    l=[0,1]
    for i in range(n-1):
        l.append(None)
    nbr=fibo_dynamique(35,l)
    print(nbr)


    arbre1=arbre(5)
    liste=liste_nombre()
    for i in range(2):
        arbre1.remplissage()
        liste=liste[2:]
    #print(arbre1.gauche)

"""
f(0)=0
f(1)=1
"""