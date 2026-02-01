# Structure des Mini CTF - Shellmates 2k26

## Organisation par catégorie

### 📁 Crypto
- **crypto-basics/** : Challenges de cryptographie basique
  - `challenge/` : Énoncés et fichiers du challenge
  - `solution/` : Writeup et solve scripts

### 📁 Forensics  
- **forensics-memory/** : Challenges d'analyse de mémoire
  - `challenge/` : Énoncés et fichiers du challenge
  - `solution/` : Writeup et solve scripts

### 📁 Web
- **web-login-system/** : Challenge de contournement de login
  - `challenge/` : Application Flask et fichiers du challenge
  - `solution/` : Writeup et solve scripts

- **web-login-bypass-v1/** : Challenge alternatif de bypass de login
  - `challenge/` : Code source du challenge
  - `solution/` : Writeup et writeup

### 📁 Autres catégories
- **misc/** : À remplir
- **pwn/** : À remplir
- **reverse/** : À remplir

## Convention de nommage

- Chaque challenge a un dossier dans sa catégorie
- Chaque challenge contient deux sous-dossiers:
  - `challenge/` : Fichiers visibles par les participants
  - `solution/` : Solutions et writeups (non visibles pendant le CTF)

## Note importante

Le dossier `all_challenges/` du répertoire parent est **ignoré par git** et ne sera pas synchronisé au repo du club. Les modifications se font uniquement dans `mp-mini-ctf-2k26/`.
