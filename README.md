# Mini CTF Shellmates 2026

Mini Capture The Flag challenges créés pour le concours du club **Shellmates** en 2026.

## 📋 Description

Ce projet regroupe une collection de défis de sécurité informatique conçus pour les compétitions et événements pédagogiques du club Shellmates. Les challenges couvrent plusieurs catégories et niveaux de difficulté, du débutant à l'intermédiaire.

## 📁 Structure des défis

### 🔐 Cryptographie (`crypto/`)
- **crypto-basics** - Exploitation d'une vulnérabilité de clé réutilisée en OTP
  - Challenge : cipher1.hex et cipher2.hex
  - Difficulté : Very Easy
  - Flag : `shellmates{reusedkeyattack}`

### 🔍 Forensique (`forensics/`)
- **forensics-memory** - Analyse de dump mémoire et reconstruction de messages
  - Challenge : memory.dmp
  - Difficulté : Easy
  - Flag : `shellmates{fr4gm3nts_0f_m3m0ry}`

### 🌐 Web (`web/`)
- **web-login-system** - Injection SQL dans un système d'authentification
  - Application Flask avec interface web
  - Déploiement Docker disponible
  - Difficulté : Easy
  - Flag : `shellmates{r4nd0mW3bFl4g2026}`

- **web-login-bypass-v1** - Variante du challenge de bypass de login
  - Code source et dockerfile inclus
  - Alternative pédagogique

### 📦 Autres catégories
- **misc/** - À remplir
- **pwn/** - À remplir
- **reverse/** - À remplir

## 🚀 Démarrage rapide

### Installation locale

#### Cryptographie
```bash
cd crypto/crypto-basics/challenge
python generator.py  # Générer les fichiers de challenge
```

#### Forensique
```bash
cd forensics/forensics-memory/challenge
python generator.py  # Générer le dump mémoire
```

#### Web
```bash
cd web/web-login-system/challenge
python init_db.py     # Initialiser la base de données
python app.py         # Lancer l'application Flask
# ou avec Docker
docker build -t fans-club .
docker run -p 5000:5000 fans-club
```

## 📚 Documentation

- **PRESENTATION.md** - Descriptions détaillées de chaque challenge
- **STRUCTURE.md** - Organisation du projet et conventions de nommage
- **solution/** - Dossiers contenant les writeups et scripts de résolution

## 🏆 À propos

Ces mini CTF ont été créés comme exercice pédagogique pour les membres du club Shellmates. Ils visent à :
- Introduire les concepts de sécurité informatique
- Fournir une expérience pratique dans différents domaines (crypto, forensique, web)
- Créer une compétition engageante et éducative
- Préparer les participants aux défis avancés

## 📝 Notes

Chaque challenge contient :
- **challenge/** - Fichiers visibles par les participants
- **solution/** - Writeup complet et scripts de résolution
- **challenge.yaml** - Métadonnées du challenge (nom, difficulté, description)

## 🔗 Liens

- Club Shellmates : https://github.com/Shellmates
- Repo officiel du club : https://github.com/Shellmates/mp-mini-ctf-2k26

---

**Créé par** : Amine  
**Date** : 2026  
**Licence** : À définir
