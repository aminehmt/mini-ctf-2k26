# Reused OTP Key (veryeasy, crypto)

Objectif : récupérer le flag chiffré avec un OTP réutilisé.

Fichiers fournis :
- `cipher1.hex` : ciphertext du flag (hex)
- `cipher2.hex` : ciphertext d'un message connu (hex)

Indices :
- Le message connu est :
```
Server: mini-ctf
Version: 1.0
Message: Hello, Shellmates!
```

Comment résoudre :
1. Calculer c1 XOR c2 = flag XOR known
2. XORer le résultat avec le message connu pour obtenir le flag

Usage (auteur) :
- `python3 generator.py` pour générer `cipher1.hex` / `cipher2.hex` (inclus pour validation)
- `python3 solve.py` pour récupérer le flag automatiquement
