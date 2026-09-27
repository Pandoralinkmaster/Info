# =====================================================================
# FORENSISCHE ANALYSE: Der 53-Bit-Präzisionsverlust bei Belphegor
# =====================================================================

# 1. Wir definieren die Belphegor-Zahl mit unbegrenzter Präzision (BigInt)
belphegor_exakt = 10**30 + 666 * 10**14 + 1

# 2. Wir definieren eine "gefälschte" Belphegor-Zahl (eine gerade Zahl!)
# Wir ziehen die 1 am Ende einfach ab.
belphegor_gerade = 10**30 + 666 * 10**14

print("--- DIE EXAKTE WIRKLICHKEIT (Unbegrenzte Präzision) ---")
print(f"Sind die exakte und die gerade Zahl identisch? -> {belphegor_exakt == belphegor_gerade}")
# Ergebnis: False (Wie es logisch sein sollte)

# 3. Jetzt simulieren wir den Hardware-Fehler!
# Wir zwingen das System, die Zahlen in 64-Bit-Gleitkomma-Register zu pressen (IEEE 754)
belphegor_float = float(belphegor_exakt)
belphegor_gerade_float = float(belphegor_gerade)

print("\n--- DIE HARDWARE-ILLUSION (64-Bit Double Precision) ---")
print(f"Sind sie nach der Typenkonvertierung identisch?  -> {belphegor_float == belphegor_gerade_float}")
# Ergebnis: True !!!

# 4. Wie groß ist der "blinde Fleck" wirklich?
# Wie viel müssen wir zu 10**30 addieren, damit der Float es überhaupt bemerkt?
basis = float(10**30)
differenz = 0
schritt = 10**13  # Wir starten mit Schritten von 10 Billionen!

while basis + differenz == basis:
    differenz += schritt

print("\n--- DER BLINDE FLECK ---")
print(f"Der Computer bemerkt eine Addition bei 10^30 erst ab dem Wert: {differenz}")