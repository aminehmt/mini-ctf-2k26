# Mini CTFs Shellmates 2026 - Présentation Détaillée

## Cryptographie : Reused OTP Key - La Clé Réutilisée

Ce défi cryptographique explore la vulnérabilité fondamentale du One-Time Pad lorsque la même clé est réutilisée pour chiffrer plusieurs messages. Les participants reçoivent deux fichiers au format hexadécimal (cipher1.hex et cipher2.hex), chiffrés avec la même clé secrète. Le deuxième fichier correspond à un message connu fourni dans l'énoncé : un en-tête de serveur contenant "Server: mini-ctf\nVersion: 1.0\nMessage: Hello, Shellmates!\n".

La particularité de ce challenge réside dans son approche pédagogique de la cryptographie. En effet, le One-Time Pad est théoriquement inviolable lorsqu'il est correctement utilisé, mais devient vulnérable dès que la même clé est réutilisée. Cette erreur d'implémentation permet une attaque élégante basée sur les propriétés du XOR.

Processus de résolution :
1. Analyse des fichiers hexadécimaux fournis
2. Compréhension de la propriété : (M1 ⊕ K) ⊕ (M2 ⊕ K) = M1 ⊕ M2
3. Application du XOR entre les deux textes chiffrés
4. Utilisation du message connu pour retrouver le flag

Le challenge inclut :
- Fichiers de challenge : cipher1.hex, cipher2.hex
- Documentation claire dans challenge.yaml
- Script de génération (generator.py) pour les organisateurs
- Solution détaillée (solve.py) avec explications
- Writeup complet couvrant la théorie et la pratique

Niveau technique :
- Difficulté : Very Easy
- Prérequis : Bases en manipulation de bytes et opérations XOR
- Compétences développées : Cryptanalyse basique, manipulation de données hexadécimales

Flag : shellmates{reusedkeyattack}

Points d'apprentissage :
- Importance de l'unicité des clés en cryptographie
- Propriétés mathématiques du XOR
- Manipulation de données hexadécimales
- Concepts fondamentaux du One-Time Pad

## Web : Club des Fans Shellmates - Le Salon VIP

Une application web moderne qui simule un système d'authentification exclusif pour le club des fans de Shellmates. Ce défi met en scène une faille d'injection SQL classique dans un contexte ludique et engageant, où les participants doivent contourner le système d'authentification pour accéder à un salon VIP.

Infrastructure technique :
- Backend : Flask (Python)
- Base de données : SQLite
- Déploiement : Container Docker
- Interface : HTML/CSS stylisée avec thème cyberpunk

Architecture du challenge :
- app.py : Application Flask principale
- init_db.py : Initialisation de la base de données
- templates/ : Pages web stylisées (login.html, vip_lounge.html, etc.)
- Dockerfile : Configuration du conteneur
- requirements.txt : Dépendances Python

Mécanisme de vulnérabilité :
La page de login demande un code fan et un événement préféré, construisant une requête SQL vulnérable :
```sql
SELECT ... FROM shellmates_fans WHERE fan_code = '[INPUT]' AND favorite_event = '[INPUT]'
```

Indices intégrés :
- Messages d'erreur personnalisés réagissant aux tentatives d'injection
- Commentaires dans le code source suggérant l'utilisation de SQL
- Interface intuitive avec des indices visuels

Progression attendue :
1. Découverte de l'interface de login
2. Analyse des messages d'erreur révélateurs
3. Identification de la vulnérabilité SQL
4. Exploitation pour accéder au salon VIP
5. Récupération du flag

Éléments pédagogiques :
- Introduction aux injections SQL
- Sensibilisation à la sécurité des bases de données
- Importance des requêtes paramétrées
- Design d'interface utilisateur sécurisée

Flag : shellmates{r4nd0mW3bFl4g2026}

Installation locale :
```bash
python init_db.py && python app.py
# ou avec Docker
docker build -t fans-club . && docker run -p 5000:5000 fans-club
```

## Forensique : Memory Fragments - Les Messages Perdus

Ce défi forensique plonge les participants dans l'analyse d'un dump mémoire provenant d'un navigateur web qui s'est brusquement interrompu. L'histoire met en scène un agent qui a intercepté ce dump contenant des fragments d'une conversation sensible, où un flag a été partagé morceau par morceau à différents moments.

Le cœur du défi repose sur un dump mémoire soigneusement construit, où des messages de conversation suivent un format standard : [HH:MM:SS] username: message. Les fragments du flag sont dispersés chronologiquement parmi des messages de conversation ordinaires, créant un mélange réaliste de données à analyser. Le dump contient également du "bruit" binaire entre les messages, simulant un véritable environnement de récupération de données.

Les participants découvrent rapidement que les timestamps ne sont pas là par hasard. En effet, les fragments du flag ont été partagés dans un ordre précis, et les horodatages deviennent la clé pour reconstituer le message original. Cette approche enseigne l'importance des métadonnées temporelles dans l'analyse forensique, une compétence cruciale dans les investigations numériques réelles.

La progression naturelle du défi suit plusieurs étapes d'apprentissage :
1. La première utilisation de la commande 'strings' révèle des messages lisibles dans le dump binaire
2. L'observation des timestamps mène à la compréhension de leur importance
3. L'identification des fragments du flag nécessite une lecture attentive des messages
4. La reconstruction finale exige une organisation méthodique des données temporelles

Les messages contenant le flag suivent une structure narrative cohérente :
- [14:30:00] : Message initial avec "shellmates{"
- [14:32:00] : Premier fragment "fr4g"
- [14:34:00] : Deuxième fragment "m3nt"
- [14:36:00] : Troisième fragment "s_0f"
- [14:38:00] : Quatrième fragment "_m3m"
- [14:40:00] : Fragment final "0ry}"

Le challenge est accompagné d'outils essentiels :
- Un script generator.py qui crée le dump avec des paramètres contrôlés
- Une solution solve.py démontrant l'automatisation de l'analyse
- Une documentation détaillée expliquant les concepts forensiques
- Des indices stratégiquement placés dans la description du challenge

L'aspect pédagogique est renforcé par :
- L'utilisation de formats de données réels
- La simulation d'une situation d'investigation authentique
- L'introduction aux outils d'analyse forensique
- La démonstration de l'importance de la chronologie dans les investigations

Pour réussir, les participants doivent :
- Maîtriser les commandes basiques d'analyse de fichiers binaires
- Comprendre l'importance des métadonnées temporelles
- Développer une approche méthodique d'investigation
- Potentiellement créer leurs propres scripts d'analyse

Le flag final, shellmates{fr4gm3nts_0f_m3m0ry}, ne peut être obtenu qu'en reconstituant correctement l'ordre chronologique des fragments, renforçant ainsi l'importance de la précision dans l'analyse forensique.

Ce défi, bien que classé comme "Easy", offre une expérience complète d'investigation numérique, préparant les participants aux concepts plus avancés de l'analyse forensique tout en restant accessible aux débutants. Il démontre parfaitement comment des données apparemment fragmentées peuvent être reconstituées en utilisant les métadonnées disponibles et une approche systématique.