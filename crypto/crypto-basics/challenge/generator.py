#!/usr/bin/env python3
"""
Générateur pour le challenge "Reused OTP Key".

Exécutez `python3 generator.py` pour écrire `cipher1.hex` et `cipher2.hex` dans ce répertoire.
Ce script utilise une clé déterministe (pour reproductibilité) et écrit les hex des ciphertexts.
"""
from pathlib import Path


def xor_bytes(a: bytes, b: bytes) -> bytes:
    return bytes(x ^ y for x, y in zip(a, b))


def main():
    out = Path(__file__).parent

    # clé déterministe (64 bytes) — suffisante pour nos messages
    key = bytes([i % 256 for i in range(64)])

    # message 1 = le flag
    flag = b"shellmates{reusedkeyattack}"

    # message 2 = un message connu (fourni dans l'énoncé)
    known = (
        b"Server: mini-ctf\n"
        b"Version: 1.0\n"
        b"Message: Hello, Shellmates!\n"
    )

    c1 = xor_bytes(flag, key[: len(flag)])
    c2 = xor_bytes(known, key[: len(known)])

    (out / "cipher1.hex").write_text(c1.hex())
    (out / "cipher2.hex").write_text(c2.hex())

    print("Wrote cipher1.hex and cipher2.hex")


if __name__ == "__main__":
    main()
