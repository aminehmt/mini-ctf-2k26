# Memory Fragments - Write-up

## Description du challenge

Le challenge fournit un dump mémoire (`memory.dmp`) qui contient des fragments d'une conversation en ligne. 
Le flag a été partagé morceau par morceau dans plusieurs messages, et ces messages sont mélangés dans le dump.

## Solution

1. D'abord, on peut utiliser `strings` pour voir le contenu lisible du dump :
```bash
strings memory.dmp
```

On voit des messages au format : `[HH:MM:SS] username: message`

2. Les messages contenant des parties du flag sont :
```
[14:30:00] hacker1337: Hey, j'ai trouvé quelque chose d'intéressant : shellmates{
[14:32:00] anonymous: Voici la suite : fr4g
[14:34:00] security_expert: Voici la suite : m3nt
[14:36:00] hacker1337: Voici la suite : s_0f
[14:38:00] anonymous: Voici la suite : _m3m
[14:40:00] security_expert: Et voilà la fin : 0ry}
```

3. En ordonnant les messages par timestamp et en concaténant les fragments, on obtient le flag :
```
shellmates{fr4gm3nts_0f_m3m0ry}
```

## Script de solution automatisée

Le script `solve.py` fourni :
1. Lit le dump mémoire
2. Extrait tous les messages avec leurs timestamps
3. Trie les messages chronologiquement
4. Identifie et concatène les fragments du flag

## Apprentissages

Ce challenge illustre :
- L'importance d'analyser les timestamps dans une investigation forensique
- Comment extraire des informations utiles d'un dump mémoire
- L'utilisation d'expressions régulières pour parser des logs
- La reconstruction d'informations fragmentées