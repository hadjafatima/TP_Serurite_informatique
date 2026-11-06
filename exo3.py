import zipfile

alphabet="abcdefghijklmnopqrstuvwxyz"
archive=zipfile.ZipFile("archive.zip")
    

#Fonction qui génère récursivement tous les mots de passe de longueur n    
def generer(mdp,n):
    if len(mdp)==n:
        try:
            archive.read("cat.jpg",pwd=mdp.encode())   #On tente d'ouvrir le fichier avec le mot de passe courant 
        except(RuntimeError, Exception):         #Lève une exception si ce n'est pas le bon
            return False   
        else:
            print("Mot de passe trouvé:",mdp)
            return True
    else:
        for c in alphabet:     
            new_mdp=mdp+c             #On ajoute chaque lettre au fur et à mesur
            if generer(new_mdp,n):
                return True
        #Aucune lettre n'a permis de trouver le mot de passe à ce niveau
        return False       

#On essaie toutes les longueurs de mot de passe possibles
for j in range(1,27):
    if generer("",j):
        break                   #On arrête la boucle si le mot de passe a été trouvé

archive.close()
