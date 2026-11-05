# TP1 – Introduction à la sécurité informatique

TP réalisé en binôme en **L3 Informatique** (Université de Limoges). Tous les programmes sont écrits en **Python**.

## Objectif

Mettre en pratique des attaques classiques sur des mots de passe et des chiffrements simples :
cryptanalyse de César et de Vigenère, attaque par dictionnaire, force brute sur une archive zip et sur un code PIN.

## Contenu du dépôt

```
SI/
├── rapport_tp1.pdf      # Rapport détaillé du TP
├── archive.zip          # Archive protégée par mot de passe (exercice 3)
└── TP1/
    ├── exo1.py          # Exercice 1 : César et Vigenère
    ├── exo2.py          # Exercice 2 : mot de passe faible (MD5)
    ├── exo3.py          # Exercice 3 : archive zip protégée
    ├── exo4.py          # Exercice 4 : authentification (PIN)
    └── exemple_client.py  # Exemple de client socket
```

## Exercices

### Exercice 1 : Cryptanalyse de César et de Vigenère
- Chiffrement et déchiffrement de César et de Vigenère
- Analyse fréquentielle et calcul de l'indice de coïncidence
- Cryptanalyse de César par comparaison avec les fréquences des lettres du français
- Cryptanalyse de Vigenère : test de Kasiski pour estimer la longueur de la clé,
  puis recherche de la clé lettre par lettre

### Exercice 2 : Mot de passe faible
Attaque par dictionnaire sur un haché MD5 (bibliothèque `hashlib`).

### Exercice 3 : Archive zip protégée
Force brute récursive pour retrouver le mot de passe de `archive.zip` (bibliothèque `zipfile`).

### Exercice 4 : Authentification
Force brute des 10 000 codes PIN possibles sur un service accessible par socket.

## Utilisation

```bash
python3 exo1.py
python3 exo2.py
python3 exo3.py
python3 exo4.py
```

## Remarque

Le fichier `rockyou.txt` (liste de mots de passe utilisée à l'exercice 2) n'est **pas inclus**
dans ce dépôt car il est trop volumineux (plus de 100 Mo). Il est disponible publiquement
sur internet. Pour tester l'exercice 2, télécharge-le et place-le dans le même dossier que `exo2.py`.

## Rapport

Le rapport complet (explications, méthodes et résultats) est disponible dans [`SI/rapport_tp1.pdf`](SI/rapport_tp1.pdf).

## Auteures

TP réalisé en binôme par :
- Hadja Fatima – L3 Informatique, Université de Limoges
- KPARA Hamoudalath – L3 Informatique, Université de Limoges
