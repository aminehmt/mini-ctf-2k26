# Writeup — Reused OTP Key

Solution courte :

1. Lire `cipher1.hex` et `cipher2.hex` et convertir les hex en bytes.
2. Faire XOR entre `cipher1` et `cipher2` : cela donne `flag XOR known`.
3. Faire XOR entre le résultat et le message connu (fourni dans l'énoncé) : on obtient le flag.

Flag final :

```
shellmates{reusedkeyattack}
```

Explication :

Un one-time pad (OTP) est sûr uniquement si la clé est utilisée une seule fois. Si la même clé
est réutilisée pour chiffrer deux messages m1 et m2 en produisant c1 = m1 XOR k et c2 = m2 XOR k,
alors c1 XOR c2 = m1 XOR m2. Si m2 est connu, on récupère directement m1.
