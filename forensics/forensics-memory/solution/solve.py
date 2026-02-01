#!/usr/bin/env python3
"""
Solveur pour le challenge Memory Fragments.
Extrait et réordonne les fragments de message du dump mémoire pour récupérer le flag.
"""
from pathlib import Path
import re
from datetime import datetime

def extract_messages(dump_bytes):
    """Extrait tous les messages du dump avec leur timestamp."""
    # Pattern pour trouver les messages
    # Format: [HH:MM:SS] username: message
    pattern = rb'\[(\d{2}:\d{2}:\d{2})\] ([^:]+): (.+)\n'
    
    messages = []
    for match in re.finditer(pattern, dump_bytes):
        time_str = match.group(1).decode()
        username = match.group(2).decode()
        message = match.group(3).decode()
        
        # Convertir le timestamp en datetime pour trier
        time = datetime.strptime(time_str, "%H:%M:%S")
        messages.append((time, username, message))
    
    return messages

def find_flag_fragments(messages):
    """Trouve et ordonne les fragments du flag."""
    # Trier les messages par timestamp
    messages.sort(key=lambda x: x[0])
    
    # Chercher les messages contenant des parties du flag
    flag_fragments = []
    
    for _, _, msg in messages:
        # Chercher le début du flag
        if 'shellmates{' in msg:
            flag_fragments.append('shellmates{')
        # Chercher la fin du flag
        elif '0ry}' in msg:
            flag_fragments.append('0ry}')
        # Chercher les morceaux du milieu
        else:
            for fragment in ['fr4g', 'm3nt', 's_0f', '_m3m']:
                if fragment in msg:
                    flag_fragments.append(fragment)
    
    return flag_fragments

def main():
    # Lire le dump
    dump_file = Path(__file__).parent / "memory.dmp"
    dump = dump_file.read_bytes()
    
    # Extraire les messages
    messages = extract_messages(dump)
    print(f"Messages trouvés : {len(messages)}")
    
    # Trouver les fragments du flag
    fragments = find_flag_fragments(messages)
    
    # Afficher les fragments dans l'ordre
    print("\nFragments trouvés (dans l'ordre chronologique) :")
    for i, frag in enumerate(fragments, 1):
        print(f"{i}. {frag}")
    
    # Reconstituer le flag (si tous les fragments sont présents)
    if fragments:
        print("\nFlag reconstitué :")
        print("".join(fragments))

if __name__ == "__main__":
    main()