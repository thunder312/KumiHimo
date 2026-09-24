#!/usr/bin/env python3
"""
Kumihimo-Modell: Kongo Gumi auf der runden Scheibe mit 32 Schlitzen.

Dasselbe Rechenmodell wie im Kumihimo-Planer (kumihimo-planer.html),
als Python-Referenz zum Nachrechnen und Weiterentwickeln.

Aufrufe:
  python kumihimo_modell.py muster Muster/4-farben-spirale.json
      -> Startaufbau, Flechtschritte (2 Runden) und Matrix eines gespeicherten Musters
  python kumihimo_modell.py zeichnung 16 "ABCDABCD/ABCDABCD/ABCDABCD/ABCDABCD"
      -> flechtbarer Aufbau zu einer Zeichnung (Zeilen von oben nach unten, '.' = egal)
  python kumihimo_modell.py katalog 16
      -> Anzahl verschiedener Zweifarben-Muster (Kontrolle: 16 Fäden -> 1162)

Modell in Kürze
  * Fäden liegen paarweise links und rechts neben den Markierungen
    (16 Fäden: Paare bei 32|1, 4|5, 8|9 ... 28|29; 8 Fäden: 32|1, 8|9, 16|17, 24|25).
  * Schritt: oben rechts -> unten rechts, unten links -> oben links,
    Scheibe gegen den Uhrzeigersinn drehen, bis das nächste Paar oben liegt.
  * Die beiden bewegten Fäden bilden je einen Stich auf der Kordel.
  * Die Reihenfolge, in der die Fäden wandern (die "Musterkette"), enthält jeden
    Faden genau einmal. Das Muster hängt nur von den Farben in dieser Kette ab.
  * Matrix-Sicht (Spalten = Stiche rundum, Zeile = halbe Runde): Das Muster
    wiederholt sich alle 4 Zeilen, und Zeile r+2 ist Zeile r um eine halbe Runde
    versetzt. Jeder Faden liefert genau diese zwei Stiche.
"""
import json
import sys
from collections import Counter

SLOTS = 32


def simulate(n, steps):
    """Simuliert `steps` Flechtschritte mit n Fäden (8 oder 16).

    Rückgabe: (start, moves, stitches)
      start[s]   = Startschlitz (0..31, 0 entspricht Schlitz 1) von Faden s
      moves      = Liste (von_oben, nach_unten, von_unten, nach_oben, faden_runter, faden_hoch)
      stitches   = Liste (schritt, schlitz, faden)
    """
    g_count = n // 2
    spacing = SLOTS // g_count
    groups = [[(g * spacing - 1) % SLOTS, g * spacing] for g in range(g_count)]
    occ, start = {}, {}
    for g, (ccw, cw) in enumerate(groups):
        occ[ccw], occ[cw] = 2 * g, 2 * g + 1
        start[2 * g], start[2 * g + 1] = ccw, cw
    moves, stitches = [], []
    for k in range(steps):
        t = k % g_count
        b = (t + g_count // 2) % g_count
        p, p1 = groups[t]
        q, q1 = groups[b]
        down, up = occ.pop(p1), occ.pop(q1)
        d_to, u_to = (q - 1) % SLOTS, (p - 1) % SLOTS
        occ[d_to], occ[u_to] = down, up
        groups[t], groups[b] = [u_to, p], [d_to, q]
        moves.append((p1, d_to, q1, u_to, down, up))
        stitches.append((k, u_to, up))
        stitches.append((k, d_to, down))
    return start, moves, stitches


def necklace(n):
    """Musterkette: Reihenfolge der Fäden auf der Kordel."""
    _, moves, _ = simulate(n, n)
    return [m[5] for m in moves]


def matrix_table(n):
    """T[r][c] = Faden in Zeile r (0..3, von unten) und Spalte c."""
    g_count = n // 2
    half, width = g_count // 2, SLOTS // g_count
    _, _, stitches = simulate(n, 8 * half)
    table = [[None] * g_count for _ in range(4)]
    for k, slot, s in stitches:
        r = k // half
        if 4 <= r < 8:
            table[r % 4][((30 - r - slot) % SLOTS) // width] = s
    return table


def label(slot):
    return slot + 1


def fit_drawing(n, rows):
    """Flechtbarer Aufbau zu einer Zeichnung (Zeilen oben->unten, Zeichen je Farbe, '.' egal).

    Rückgabe: (farbe_je_faden, abweichungen, gezeichnete_zellen)
    """
    table = matrix_table(n)
    votes = [Counter() for _ in range(n)]
    freq = Counter()
    R = len(rows)
    for i, row in enumerate(rows):
        for c, ch in enumerate(row):
            if ch == ".":
                continue
            s = table[(R - 1 - i) % 4][c]
            votes[s][ch] += 1
            freq[ch] += 1
    fallback = freq.most_common(1)[0][0] if freq else "A"
    colors = []
    for s in range(n):
        if votes[s]:
            colors.append(max(votes[s], key=lambda ch: (votes[s][ch], freq[ch])))
        else:
            colors.append(fallback)
    miss = sum(sum(v.values()) - v[colors[s]] for s, v in enumerate(votes))
    return colors, miss, sum(freq.values())


def count_two_color_patterns(n):
    """Zweifarbige Muster bis auf Drehen, Spiegeln und Farbtausch der Kette."""
    full = (1 << n) - 1

    def rot(v, r):
        return ((v << r) | (v >> (n - r))) & full

    def rev(v):
        return int(format(v, f"0{n}b")[::-1], 2)

    seen, count = set(), 0
    for v in range(1 << n):
        if v in seen:
            continue
        count += 1
        for w in (v, rev(v)):
            for r in range(n):
                x = rot(w, r)
                seen.add(x)
                seen.add(full ^ x)
    return count


def print_setup(n, color_of, name_of=str):
    start, moves, _ = simulate(n, n)
    print("Startaufbau (Schlitz links | rechts):")
    for g in range(n // 2):
        a, b = 2 * g, 2 * g + 1
        print(f"  {label(start[a]):2d} | {label(start[b]):2d}   {name_of(color_of[a])} / {name_of(color_of[b])}")
    print("\nFlechtschritte, erste zwei Runden (danach Scheibe gegen den Uhrzeigersinn drehen):")
    _, moves, _ = simulate(n, n)
    for k, (p1, d_to, q1, u_to, down, up) in enumerate(moves):
        print(f"  {k + 1:2d}: oben rechts {label(p1):2d} -> {label(d_to):2d} ({name_of(color_of[down])}),"
              f"  unten links {label(q1):2d} -> {label(u_to):2d} ({name_of(color_of[up])})")


def print_matrix(n, color_of, rows=8, sym=str):
    table = matrix_table(n)
    print(f"\nMatrix ({n // 2} Spalten, {rows} Zeilen, oben = später geflochten):")
    for i in range(rows):
        r = rows - 1 - i
        print("  " + " ".join(sym(color_of[table[r % 4][c]]) for c in range(n // 2)))


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return
    cmd = argv[1]
    if cmd == "muster":
        with open(argv[2], encoding="utf-8") as fh:
            rec = json.load(fh)
        n = int(rec["n"])
        neck_idx = [int(ch) for ch in str(rec["neck"])]
        names = rec.get("names") or [f"Farbe {i + 1}" for i in range(6)]
        chain = necklace(n)
        color_of = [0] * n
        for j, s in enumerate(chain):
            color_of[s] = neck_idx[j]
        print(f"{rec.get('name', 'Muster')} · {n} Fäden\n")
        print_setup(n, color_of, lambda c: names[c] if c < len(names) else f"Farbe {c + 1}")
        print_matrix(n, color_of, sym=lambda c: str(c))
        used = Counter(color_of)
        print("\nFäden je Farbe: " + ", ".join(f"{names[c]} {k}" for c, k in sorted(used.items())))
    elif cmd == "zeichnung":
        n = int(argv[2])
        rows = argv[3].split("/")
        colors, miss, total = fit_drawing(n, rows)
        print(f"{total - miss} von {total} Zellen passen ({miss} Abweichungen)\n")
        print_setup(n, colors)
        print_matrix(n, colors, rows=len(rows))
    elif cmd == "katalog":
        n = int(argv[2])
        print(f"{n} Fäden: {count_two_color_patterns(n)} verschiedene Zweifarben-Muster")
    else:
        print(__doc__)


if __name__ == "__main__":
    main(sys.argv)
