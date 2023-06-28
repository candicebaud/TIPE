##data
NOMS_PAYS = ["France", "Espagne", "Allemagne", "UK", "Italie", "Pologne", "Belgique", "Grèce", "Reptchèque", "Portugal", "Hongrie", "Suède", "Autriche", "Suisse", "Danemark", "Finlande", "Slovaquie","Norvège","Irlande", "Pays-Bas", "Algérie", "Arabie Saoudite", "Israel", "Malte", "Maroc", "Tunisie", "Egypte", "Turquie", "Canada", "USA", "Argentine", "Roumanie", "Kazakhstan", "Russie", "Ukraine", "Chine", "Inde"]

AFFICHER = ["évolution du nombre total de morts", "évolution du nombre de contaminés"]
#données relatives aux pays (nombre hab)
#AFNMO où on a de la donnée:
algerie=[42230000, 20]
arabiesaoudite=[34813900, 21]
israel=[8655540, 22]
malte=[514564, 23]
maroc=[34660000, 24]
tunisie=[11180000,25]
egypte=[102334000, 26]
turquie=[84339100, 27]
AFNMO=[algerie, arabiesaoudite, israel, malte, maroc, tunisie, egypte, turquie]

#europe
france=[66352469,0]
espagne=[46439864, 1]
allemagne=[81174000, 2]
UK=[64767115, 3]
italie=[60795612,4]
pologne=[38005614, 5]
belgique=[11258434,6]
grece=[10812467, 7]
reptcheque=[10538275, 8]
portugal=[10374822, 9]
hongrie=[9849000, 10]
suede=[9747355, 11]
autriche=[8584926, 12]
suisse=[8236573, 13]
danemark=[5659715, 14]
finlande=[5471553, 15]
slovaquie=[5421349, 16]
norvege=[5165802, 17]
irlande=[4625885,18]
paysbas=[16900726, 19]
europe=[france, espagne, allemagne, UK, italie, pologne, belgique, grece, reptcheque, portugal, hongrie, suede, autriche, suisse, danemark, finlande, slovaquie, norvege, irlande, paysbas]

#autres pays importants
canada=[37590000,28]
USA=[328200000, 29]
argentine=[44490000, 30]
roumanie=[19410000,31]
kazakhstan=[18280000, 32]
russie=[144500000,33]
ukraine=[41980000,34]
chine=[1393000000, 35]
inde=[1353000000,36]
autres=[canada, USA, argentine, roumanie, kazakhstan, russie, ukraine, chine, inde]

monde=[france, espagne, allemagne, UK, italie, pologne, belgique, grece, reptcheque, portugal, hongrie, suede, autriche, suisse, danemark, finlande, slovaquie, norvege, irlande, paysbas,algerie, arabiesaoudite, israel, malte, maroc, tunisie, egypte, turquie,canada, USA, argentine, roumanie, kazakhstan, russie, ukraine, chine, inde]

import numpy as np
import matplotlib.pyplot as plt
import random as rd
from math import floor
from math import ceil

##liste avec les numéros des pays concernés
def listenum(H):
    listenum=[0]*(len(H))
    for i in range (len(H)):
        listenum[i]=H[i][1]
    return (listenum)

##creerseuildepart
def seuildep(T, sc, sd, S):
    for i in range (len(T)):
        if S[i]==0:
            if T[i]>=sc:
                S[i]=1
            else:
                S[i]=0
        else:
            if T[i]>sd:
                S[i]=1
            else:
                S[i]=0
    return S

##taux
def taux(C, L):
    T=[0]*(len(C))
    for i in range (len(C)):
            if (L[i][0]+L[i][1]+L[i][2])==0:
                T[i]=0
            else:
                T[i]=(L[i][1])/(L[i][0]+L[i][1]+L[i][2])
    return (T)

def tauxlocal(C, L, i):
    T=0
    if (L[i][0]+L[i][1]+L[i][2])==0:
        T=0
    else:
        T=(L[i][1])/(L[i][0]+L[i][1]+L[i][2])
    return (T)

##creertableau
def creertableau(n, a):
    N=[0]*n
    for i in range (n):
        N[i]=[0]*a
    return N

##SIRevol
#Lt=[St, It, Rt, Dt] #D les dead
#d le taux de létalité =! taux de mortalité
def SIRevol(Lt, beta, i, k): # Lt la liste au temps t, L1 la liste au temps t+1, beta param de l'épidémie
#modèle d'évolution de t à t+1
    gamma=0.2
    d=0.048
    N=(Lt[0]+Lt[1]+Lt[2]+Lt[3])
    if N==0:
        return ([0, 0, 0, 0])
    else:
        L1=[0,0,0,0]
        L1[0]= (-beta[i][k]*Lt[0]*Lt[1])/(N) +Lt[0] #St+1
        L1[1]= beta[i][k]*Lt[0]*Lt[1]/(N) - gamma*Lt[1] +Lt[1] -d*Lt[1] #It+1
        L1[2]= Lt[2]+ gamma*Lt[1] #Rt+1
        L1[3]= Lt[3]+d*Lt[1]
        Lt=L1 #Lt devient L1 pour pouvoir ensuite le faire à chaque temps
        return (Lt) #on renvoie la liste au temps t+1


##renvoyer une case
def case(Lt,n):
    return (Lt[n])

##creerLt pour le début seulement
def creerLt(C, H, i): #crée un Lt pour le pays en position i
    Lt=[0, 0, 0, 0]
    Lt[0]=H[i][0]-C[i]
    Lt[1]=C[i]
    return Lt

##creerL au depart
def creerL(C, H): #crée la liste des Lt-> cad on a L[0][0] qui donne le nombre de sains dans le pays 0
#L[0][1] le nombre de contaminés du pays 0
#L[0][2] le nombre de recovered du pays 1
    L=creertableau(len(C), len(C))
    for i in range (len(C)):
        L[i]=creerLt(C,H,i)
    return L

##verifS
def verifS(S):
    n=len(S)
    res=0
    for i in range (n):
        if S[i]==1:
            res=res+1
    if res==n:
        return False

##creerV V=voyageurs en prenant en compte les stratégies de confinement

def creerV(L, C, S, Pop):
    paspossible=[]
    for i in range (len(C)):
        if Pop[i]==0:
            paspossible.append(i) # on fait la liste des gens qui ne peuvent pas voyager car ils sont morts
    V=[0]*(len(C))
    for i in range (len(C)):
            V[i]=[0]*2
    if verifS(S)==False:
        for i in range (len(C)):
            V[i][0]=0
    else :
        for i in range (len(C)):
            if S[i]==0:
                V[i][1]= rd.randint(0,(len(C)-1))
                while S[V[i][1]]==1 :
                    V[i][1]=rd.randint(0, len(C)-1)
                    while V[i][1] in paspossible :
                        V[i][1]=rd.randint(0, len(C)-1)
                V[i][0]=rd.uniform(0, 0.0002)*(L[i][0]+L[i][1]+L[i][2])#on ne veut pas que plus de la moitié de la population se barre sinon pas cohérent
            else:
                V[i][0]=0
    return (V)
##creerD
def creerD(H, C, V, L): #on renvoie la liste des contaminés qui se déplacent et où ils se déplacent
    D=[0]*(len(C))
    T=taux(C, L)
    for i in range (len(C)):
        D[i]=[0]*2
    for i in range (len(C)):
        D[i][0]=(V[i][0]*T[i])
        D[i][1]=V[i][1]
    return (D)

##trouver les contaminés
def recherche(D, i):
    c=0 #res
    for k in range (len(D)):
        if D[k][1]==i:
            c=c+D[k][0]
    return c


##creer beta
def creertableaubeta(n,C):
    beta=creertableau(len(C), n+1)
    for i in range (len(C)):
        beta[i][0]=0.39
    return beta


##expansion avec confinement
def expansionconfined(C, H, n, sc, sd):# d le taux de gens qui meurent
    Pop=[0]*len(H)
    for i in range (len(H)):
        Pop[i]=H[i][0]
    L=creerL(C, H)
    beta=creertableaubeta(n, C)
    gamma=0.2
    d=0.048
    S=[0]*(len(C))
    T=taux(C,L)
    S=seuildep(T,sc, sd,S)
    V=creerV(L,C,S, Pop)
    D=creerD(H,C,V,L) #D le tableau des gens dangereux qui se déplacent et vers quel pays ils se déplacent
    evolcontamines=creertableau(len(C), n) #evolution des contaminés
    evolmorts=creertableau(len(C),n)
    listedeS=creertableau(len(C),n)
    for k in range (n):
        T=taux(C,L)
        S=seuildep(T,sc, sd ,S)
        V=creerV(L,C,S, Pop)
        D=creerD(H,C,V,L)
        for i in range (len(C)):
            L[i]=SIRevol(L[i], beta, i, k)
            C[i]=L[i][1] + recherche(D,i)-D[i][0] #on contamine
            Pop[i]=Pop[i]+recherche(V,i)-V[i][0]
            L[i]=[Pop[i]-C[i]-L[i][2],C[i],L[i][2],L[i][3]]
            evolcontamines[i][k]=C[i]
            evolmorts[i][k]=L[i][3]
            listedeS[i][k]=S[i]
            if listedeS[i][k]==1:
                beta[i][k+1]=0.22
            else:
                beta[i][k+1]=0.39

    return ([evolmorts, evolcontamines]) #on renvoie la liste des états de chaque pays

#à partir d'un moment, l'évolution du nombre de contaminés stagne -> pourtant si le pays est confiné, l'épidémie doit progresser avec SIRevol

##tracer des évolutions en fonction
def tracercontamines(C, H, n,sc, sd):
    evol=expansionconfined(C, H, n, sc, sd)[1]
    abscisse=[0]*n
    liste=listenum(H)
    for i in range (n):
        abscisse[i]=i
    for k in range (len(C)):
        plt.plot(abscisse,evol[k], label=str(NOMS_PAYS[liste[k]]))
        plt.legend()
        plt.title("Nombre de contaminés en fonction du temps")
        plt.xlabel("Temps en jours")
        plt.ylabel("Nombre de contaminés")
        plt.legend(fontsize=6, loc='best')
    return(plt.show())

def tracermorts(C, H, n,sc, sd):
    evol=expansionconfined(C, H, n,sc, sd)[0]
    abscisse=[0]*n
    liste=listenum(H)
    for i in range (n):
        abscisse[i]=i
    for k in range (len(C)):
        plt.plot(abscisse,evol[k], label=str(NOMS_PAYS[liste[k]]))
        plt.legend()
        plt.title("Nombre de morts en fonction du temps")
        plt.xlabel("Temps en jours")
        plt.ylabel("Nombre de morts")
        plt.legend(fontsize=6, loc='best')
    plt.show()


def tracermortsfrance(C, H, n,sc, sd):
    evol=expansionconfined(C, H, n,sc, sd)[0]
    abscisse=[0]*n
    liste=listenum(H)
    for i in range (n):
        abscisse[i]=i
    plt.plot(abscisse,evol[0], label=str(NOMS_PAYS[liste[0]]))
    plt.legend()
    plt.title("Nombre de morts en fonction du temps")
    plt.xlabel("Temps en jours")
    plt.ylabel("Nombre de morts")
    plt.legend(fontsize=6, loc='best')
    plt.show()

def tracercontaminesfrance(C, H, n,sc, sd):
    evol=expansionconfined(C, H, n,sc, sd)[1]
    abscisse=[0]*n
    liste=listenum(H)
    for i in range (n):
        abscisse[i]=i
    plt.plot(abscisse,evol[0], label=str(NOMS_PAYS[liste[0]]))
    plt.legend()
    plt.title("Nombre de contaminés en fonction du temps")
    plt.xlabel("Temps en jours")
    plt.ylabel("Nombre de contaminés")
    plt.legend(fontsize=6, loc='best')
    plt.show()

##application
#tracercontamines([116, 1486, 114,35, 1578, 0,1, 7, 3,0, 0,14, 14, 23, 4, 5, 0, 19, 1, 10, 3, 0, 9, 0, 0, 0,1, 0, 20,65,0, 2, 0,0,0,32616,0],monde, 365, 0.003, 0.0006)
#tracermorts([116, 1486, 114,35, 1578, 0,1, 7, 3,0, 0,14, 14, 23, 4, 5, 0, 19, 1, 10, 3, 0, 9, 0, 0, 0,1, 0, 20,65,0, 2, 0,0,0,32616,0],monde, 365, 0.003, 0.0006)
#tracercontamines([116, 1486, 114,35, 1578, 0,1, 7, 3,0, 0,14, 14, 23, 4, 5, 0, 19, 1, 10], europe, 365,0.003, 0.0006)
#tracermorts([116, 1486, 114,35, 1578, 0,1, 7, 3,0, 0,14, 14, 23, 4, 5, 0, 19, 1, 10], europe, 365, 0.003, 0.0006)
#tracercontamines([3, 0, 9, 0, 0, 0,1, 0], AFNMO, 365, 0.003, 0.0006)
#tracermorts([3, 0, 9, 0, 0, 0,1, 0], AFNMO, 365, 0.003, 0.0006)

#tracermortsfrance([116, 1486, 114,35, 1578, 0,1, 7, 3,0, 0,14, 14, 23, 4, 5, 0, 19, 1, 10, 3, 0, 9, 0, 0, 0,1, 0, 20,65,0, 2, 0,0,0,32616,0],monde, 365, 0.003, 0.0006)
#tracercontaminesfrance([116, 1486, 114,35, 1578, 0,1, 7, 3,0, 0,14, 14, 23, 4, 5, 0, 19, 1, 10, 3, 0, 9, 0, 0, 0,1, 0, 20,65,0, 2, 0,0,0,32616,0],monde, 365, 0.003, 0.0006)
