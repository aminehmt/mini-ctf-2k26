# Writeup — web-login-bypass

## But
Trouver le flag en contournant la page de login.

## Vulnérabilité
Le serveur construit la requête SQL en concaténant directement les champs `username` et `password`.

## Exploit (façon simple)
Dans le champ `username`, utiliser une payload :
admin' --
et mettre n'importe quel password.

## Flag
shellmates{r4nd0mW3bFl4g2026}

## Mitigation
Utiliser des requêtes paramétrées (prepared statements).
