#!/usr/bin/env python3
"""
Générateur pour le challenge Memory Fragments.
Crée un faux dump mémoire contenant des fragments de conversation avec le flag.
"""
import random
import struct
import time
from datetime import datetime, timedelta
from pathlib import Path

# Le flag complet
FLAG = "shellmates{fr4gm3nts_0f_m3m0ry}"

# Format de message : [timestamp] username: message
MESSAGE_TEMPLATE = "[{}] {}: {}\n"

def generate_conversation():
    """Génère une conversation avec le flag morcelé."""
    base_time = datetime(2025, 10, 31, 14, 30, 0)  # 31 Oct 2025 14:30:00
    messages = []
    
    # Découper le flag en morceaux
    fragments = [
        FLAG[:11],                    # shellmates{
        FLAG[11:15],                  # fr4g
        FLAG[15:19],                  # m3nt
        FLAG[19:23],                  # s_0f
        FLAG[23:27],                  # _m3m
        FLAG[27:],                    # 0ry}
    ]
    
    # Créer des messages avec les fragments
    usernames = ["hacker1337", "anonymous", "security_expert"]
    
    for i, fragment in enumerate(fragments):
        timestamp = base_time + timedelta(minutes=i*2)
        username = random.choice(usernames)
        
        # Ajouter du contexte autour des fragments
        if i == 0:
            msg = f"Hey, j'ai trouvé quelque chose d'intéressant : {fragment}"
        elif i == len(fragments)-1:
            msg = f"Et voilà la fin : {fragment}"
        else:
            msg = f"Voici la suite : {fragment}"
            
        messages.append((timestamp, username, msg))
    
    # Ajouter quelques messages de "bruit"
    noise_msgs = [
        "Vous avez vu le dernier CTF ?",
        "Je galère avec ce challenge...",
        "Quelqu'un peut m'aider ?",
        "C'est plus dur que prévu !",
        "Je vais faire une pause café",
    ]
    
    for _ in range(5):
        timestamp = base_time + timedelta(minutes=random.randint(0, 15))
        username = random.choice(usernames)
        msg = random.choice(noise_msgs)
        messages.append((timestamp, username, msg))
    
    # Mélanger les messages
    random.shuffle(messages)
    
    return messages

def create_memory_dump(messages):
    """Crée un faux dump mémoire avec les messages."""
    # Ajouter du "bruit" avant/après chaque message
    noise = bytes([random.randint(0, 255) for _ in range(64)])
    
    dump = bytearray()
    
    for timestamp, username, msg in messages:
        # Convertir le message en bytes
        message_bytes = MESSAGE_TEMPLATE.format(
            timestamp.strftime("%H:%M:%S"),
            username,
            msg
        ).encode('utf-8')
        
        # Ajouter bruit + message + bruit
        dump.extend(noise)
        dump.extend(message_bytes)
        dump.extend(noise)
    
    return bytes(dump)

def main():
    # Créer le dossier de sortie s'il n'existe pas
    out_dir = Path(__file__).parent
    out_dir.mkdir(exist_ok=True)
    
    # Générer la conversation
    messages = generate_conversation()
    
    # Créer le dump
    dump = create_memory_dump(messages)
    
    # Écrire le fichier
    dump_file = out_dir / "memory.dmp"
    dump_file.write_bytes(dump)
    
    print(f"Dump mémoire créé : {dump_file}")
    print(f"Taille : {len(dump)} bytes")

if __name__ == "__main__":
    main()