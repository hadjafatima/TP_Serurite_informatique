import unicodedata
from collections import Counter
cle_secrete="secret"
texte="Tant qu’il existera, par le fait des lois et des mœurs, une damnation sociale créant artificiellement, en pleine civilisation, des enfers, et compliquant d’une fatalité humaine la destinée qui est divine ; tant que les trois problèmes du siècle, la dégradation de l’homme par le prolétariat, la déchéance de la femme par la faim, l’atrophie de l’enfant par la nuit, ne seront pas résolus ; tant que, dans de certaines régions, l’asphyxie sociale sera possible ; en d’autres termes, et à un point de vue plus étendu encore, tant qu’il y aura sur la terre ignorance et misère, des livres de la nature de celui-ci pourront ne pas être inutiles."
alphabet_m="abcdefghijklmnopqrstuvwxyz"
alphabet_M="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
frequence_francais={'a':7.11,'b':0.9, 'c':3.18,'d':3.67, 'e':12.10, 'f':1.11, 'g':1.23,'h':1.11,'i':6.59, 'j':0.34, 'k':0.29, 'l':4.96, 'm':2.62, 'n':6.39, 'o':5.02, 'p':2.49, 'q':0.65, 'r':6.07, 's':6.51, 't':5.92, 'u':4.49, 'v':1.11,'w':0.17, 'x':0.38, 'y':0.46, 'z':0.15 }

#Question 1

def chiffrement_cesar(decalage, chaine):
    resultat=[]
    for c in chaine:
        if c in alphabet_M:
            j=alphabet_M.index(c)                          #Pour récupérer l'indice du caractere courant dans l'alphabet
            resultat.append(alphabet_M[(j+decalage)%26])   #On ajoute le caractere correspondant lorsqu'on applique le décalage
        elif c in alphabet_m:
            j=alphabet_m.index(c)
            resultat.append(alphabet_m[(j+decalage)%26])
        else:     
            resultat.append(c)     #On ajoute juste les autres caracteres hors majuscule et minuscule
    return "".join(resultat)

def dechiffrement_cesar(decalage, chaine):
    return chiffrement_cesar(-decalage,chaine)  


def chiffrement_vigenere(chaine,cle):
    resultat=[]
    k=0                                                         #Pour parcourir la clé
    for i in range(len(chaine)):
        decalage=alphabet_m.index(cle[k%len(cle)].lower())      #Trouve le décalage à appliquer en fonction de la lettre courante de la clé
        if chaine[i] in alphabet_m:
            j=(decalage+ord(chaine[i])-ord('a'))%26             #Calcule la nouvelle position de la lettre en ajoutant le décalage
            resultat.append(alphabet_m[j]) 
            k+=1

        elif chaine[i] in alphabet_M:
            j=(decalage+ord(chaine[i])-ord('A'))%26
            resultat.append(alphabet_M[j])
            k+=1

        else:
            resultat.append(chaine[i])          
    return "".join(resultat)

def dechiffrement_vigenere(chaine,cle):
    resultat=[]
    m=0
    for i in range(len(chaine)):
        if chaine[i] in alphabet_m:
           j=alphabet_m.index(chaine[i])                    #Récupére l'indice de la lettre courante du chiffré
           k=alphabet_m.index(cle[(m%len(cle))].lower())    #Récupére l'indice de la lettre courante de la clé
           resultat.append(alphabet_m[j-k])                #Fais la soustraction des deux pour retrouver la lettre d'origine
           m+=1
        elif chaine[i] in alphabet_M:
            j=alphabet_M.index( chaine[i])
            k=alphabet_m.index(cle[(m%len(cle))].lower())
            resultat.append(alphabet_M[j-k])
            m+=1
        else:
            resultat.append(chaine[i])
                    
    return "".join(resultat)

#Question 2
def analyse_frequentielle(chaine):
    compteur={}                            #Dictionnaire avec le nb d'apparitions de chaque lettre dans la chaine
    somme=0
    r={l:0 for l in alphabet_m}           #On crée un dictionnaire avec les lettres de l'alphbet en les initialisant à 0
    chaine=chaine.replace("œ", "oe").replace("æ","ae").replace("Œ","OE").replace("Æ","AE")
    for c in chaine: 
        c=c.lower()
        c=unicodedata.normalize("NFD",c)   #Decompose un caractere avec accent en caractere et accent pour povoir récupérer l'un ou l'autre 
        c=c[0]                             #prend juste le caractere de base
        if c.isalpha():
            if c not in compteur:          
                compteur[c]=1
            else:
                compteur[c]+=1
        
    for element in compteur.values():
        somme+=element
    for key, value in compteur.items():
        el=value*100/somme          #Pour chaque élément, on calcule la fréquence d'apparition
        r[key]=el
    return r

def indice_coincidence(chaine):
    compteur={}
    s=0
    N=0
    chaine=chaine.replace("œ", "oe").replace("æ","ae").replace("Œ","OE").replace("Æ","AE")
    for c in chaine: 
        c=c.lower()
        c=unicodedata.normalize("NFD",c)      
        c=c[0]  
        if c.isalpha():
            N+=1
            if c in compteur:
                compteur[c]+=1
            else:
                compteur[c]=1
    for el in compteur.values():
        s+=el*(el-1)
    resultat=s/(N*(N-1))       #calcule l'indice de coincidence
    return resultat

def cryptanalyse_cesar(chaine):
    erreur_min=float("inf")
    meilleur_decalage=0
    for decalage in range(26):
        texte=dechiffrement_cesar(decalage,chaine)
        frequence=analyse_frequentielle(texte)
        erreur=0
        for lettre in alphabet_m:
            erreur+=abs(frequence[lettre]-frequence_francais[lettre])  #On calcule l'écart entre les fréquences obtenues et celles en français
        if  erreur<erreur_min:
            erreur_min= erreur                                          #On garde l'erreur minimale
            meilleur_decalage=decalage
    print("Clé trouvée=",meilleur_decalage)
    return dechiffrement_cesar(meilleur_decalage,chaine)
    
#Question 3

#retourne la liste des diviseurs d'un nombre hormis 1
def diviseur(nb):
    diviseurs=[i for i in range(2,nb+1) if nb%i==0]        
    return diviseurs

#Retourne la liste des 5 diviseurs avec le plus grand nombre d'occurences
def apparition_diviseur(d, top_n=5):
   dico=Counter()                          #Crée un objet de type counter permettant de compter les occurences
   for liste in d:
        for el in liste:
            dico[el]+=1
   return [diviseur for diviseur, _ in dico.most_common(top_n)]     #renvoie les 5 diviseurs avec le plus d'occurence
  

#Ne garder que les lettres non accentuées
def nettoyer_chaine(chaine):
    return "".join(c for c in chaine if c in alphabet_m or c in alphabet_M)

def Kasiski(chaine,longueur_sequence):
    sequence=[]
    distance=[]
    diviseurs=[]
    chaine=nettoyer_chaine(chaine)
    for i in range(len(chaine)-longueur_sequence+1):
        sequence.append(chaine[i:i+longueur_sequence])        #Divise le chiffré en des sequences de longueur_sequence
    for j in range(len(sequence)):
        for k in range(j+1,len(sequence)):
            if sequence[j]==sequence[k]:
                distance.append((k-j))
    diviseurs=[diviseur(val) for val in distance]
    return apparition_diviseur(diviseurs)                   #renvoie les 5 diviseurs avec le plus d'apparition

def trouver_cle(texte_chiffre):
    chaine=nettoyer_chaine(texte_chiffre)
    candidats=Kasiski(texte_chiffre,5) 
    liste_cle=[]
    for el in candidats:
        cle="" 
        erreur_totale=0
        for j in range(el):
            groupe="".join(chaine[i] for i in range(j,len(chaine),el))  #Construit le groupe de lettre qui ont été chiffrées avec la même lettre
            erreur_min=float("inf")
            meilleur_decalage=0

            #Comparer pour chacun des décalages la frequence d'apparition des lettres à celle théorique du français
            for decalage in range(26):
                groupe_dechiffre=dechiffrement_cesar(decalage,groupe)
                frequences=analyse_frequentielle(groupe_dechiffre)
                erreur=0
                for lettre in alphabet_m:
                    erreur+=abs(frequences[lettre]-frequence_francais[lettre])
                if  erreur<erreur_min:
                    erreur_min= erreur
                    meilleur_decalage=decalage
            cle+=alphabet_m[meilleur_decalage]
            erreur_totale+=erreur_min
        liste_cle.append((el,cle,erreur_totale/el))
    liste_cle.sort(key=lambda x:x[2])                          #Trie la liste en utilisant l'erreur moyenne de chaque clé
    return liste_cle


decalage=17
chiffre=chiffrement_cesar(decalage,texte)
print("\nChiffrement de Cesar: ",chiffre)
print("\nDechiffrement de Cesar: ", dechiffrement_cesar(decalage,chiffre),"\n")

chaine_chiffre=chiffrement_vigenere(texte,cle_secrete)
print("Chiffrement de Vigenere: \n",chaine_chiffre, "\n")
dechiffre=dechiffrement_vigenere(chaine_chiffre, cle_secrete)
print("Dechiffrement de Vigenere: \n",dechiffre,"\n")

print("Analyse fréquentielle: ",analyse_frequentielle(chiffre),"\n")
print("Indice de coincidence: ",indice_coincidence(chiffre),"\n")

print("Le texte déchiffré avec Cesar est: \n",cryptanalyse_cesar(chiffre),"\n")


resultats=trouver_cle(chaine_chiffre)
meilleure_cle=resultats[0][1]     #On récupère la clé ayant la plus faible erreur
print("Clé retenue: ", meilleure_cle, "\n")
print("Texte déchiffré avec Vigenere: \n", dechiffrement_vigenere(chaine_chiffre,meilleure_cle))





