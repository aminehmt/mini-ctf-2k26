#!/usr/bin/env python3
"""
Solveur pour le challenge "Reused OTP Key".

Lecture de `cipher1.hex` et `cipher2.hex`, application d'un XOR avec le message connu
pour récupérer le flag.

Exécuter: python3 solve.py
"""
from pathlib import Path


def hex_to_bytes(path: Path) -> bytes:
    return bytes.fromhex(path.read_text().strip())


def xor_bytes(a: bytes, b: bytes) -> bytes:
    return bytes(x ^ y for x, y in zip(a, b))


def main():
    p = Path(__file__).parent
    c1 = hex_to_bytes(p / "cipher1.hex")
    c2 = hex_to_bytes(p / "cipher2.hex")

    # message connu (doit correspondre à celui utilisé pour générer cipher2.hex)
    known = (
        b"Server: mini-ctf\n"
        b"Version: 1.0\n"
        b"Message: Hello, Shellmates!\n"
    )

    # c1 = flag XOR key
    # c2 = known XOR key
    # donc c1 XOR c2 = flag XOR known
    flag_xor_known = xor_bytes(c1, c2[: len(c1)])

    # récupérer flag
    flag = xor_bytes(flag_xor_known, known[: len(flag_xor_known)])

    print("Recovered flag:", flag.decode())


if __name__ == "__main__":
    main()
