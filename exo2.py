import hashlib
fichier=open("rockyou.txt","r", encoding="latin-1")
trouve=False
for mdp in fichier:
    mdp=mdp.strip()   #enleve l'espace présent à chaque ligne
    hache=hashlib.md5(mdp.encode()).hexdigest()  #encode le mot de passe présent sur la ligne
    if hache=="5a74dd4eef347734c8a0a9a3188abd11":
        print("Le mot de passe associé à ce haché est:", mdp)
        trouve=True
        break
if not trouve:
    print("Le mot de passe ne se trouve pas dans ce fichier")
fichier.close()