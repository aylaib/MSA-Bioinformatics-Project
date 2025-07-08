#!/usr/bin/env python3

import sys
import random
import time

# Fonction pour générer une séquence aléatoire d'acides aminés de longueur donnée
def generate_sequence(length):
    amino_acids = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']
    return ''.join(random.choices(amino_acids, k=length))

# Fonction pour aligner deux séquences d'acides aminés
def align_sequences():
    # Demander à l'utilisateur d'entrer la taille des deux séquences
    seq1_length = int(input("Entrez la taille de la première séquence : "))
    seq2_length = int(input("Entrez la taille de la deuxième séquence : "))

    # Générer les séquences aléatoires d'acides aminés
    seq1 = generate_sequence(seq1_length)
    seq2 = generate_sequence(seq2_length)

    # Afficher les séquences générées
    print("Séquence 1 :", seq1)
    print("Séquence 2 :", seq2)

    m = len(seq1)  # Seq1 sera la séquence verticale à gauche
    n = len(seq2)  # Seq2 sera la séquence horizontale en haut
    init_mat = []  # Matrice initialisée

    # Système de notation pour correspondance, non-correspondance et trou
    blosum62 = {
        ('A', 'A'): 4, ('A', 'R'): -1, ('A', 'N'): -2, ('A', 'D'): -2, ('A', 'C'): 0,
        ('A', 'Q'): -1, ('A', 'E'): -1, ('A', 'G'): 0, ('A', 'H'): -2, ('A', 'I'): -1,
        ('A', 'L'): -1, ('A', 'K'): -1, ('A', 'M'): -1, ('A', 'F'): -2, ('A', 'P'): -1,
        ('A', 'S'): 1, ('A', 'T'): 0, ('A', 'W'): -3, ('A', 'Y'): -2, ('A', 'V'): 0,
        ('R', 'R'): 5, ('R', 'N'): 0, ('R', 'D'): -2, ('R', 'C'): -3, ('R', 'Q'): 1,
        ('R', 'E'): 0, ('R', 'G'): -2, ('R', 'H'): 0, ('R', 'I'): -3, ('R', 'L'): -2,
        ('R', 'K'): 2, ('R', 'M'): -1, ('R', 'F'): -3, ('R', 'P'): -2, ('R', 'S'): -1,
        ('R', 'T'): -1, ('R', 'W'): -3, ('R', 'Y'): -2, ('R', 'V'): -3,
        ('N', 'N'): 6, ('N', 'D'): 1, ('N', 'C'): -3, ('N', 'Q'): 0, ('N', 'E'): 0,
        ('N', 'G'): 0, ('N', 'H'): 1, ('N', 'I'): -3, ('N', 'L'): -3, ('N', 'K'): 0,
        ('N', 'M'): -2, ('N', 'F'): -3, ('N', 'P'): -2, ('N', 'S'): 1, ('N', 'T'): 0,
        ('N', 'W'): -4, ('N', 'Y'): -2, ('N', 'V'): -3,
        ('D', 'D'): 6, ('D', 'C'): -3, ('D', 'Q'): 0, ('D', 'E'): 2, ('D', 'G'): -1,
        ('D', 'H'): 1, ('D', 'I'): -3, ('D', 'L'): -4, ('D', 'K'): -1, ('D', 'M'): -3,
        ('D', 'F'): -3, ('D', 'P'): -1, ('D', 'S'): 0, ('D', 'T'): -1, ('D', 'W'): -4,
        ('D', 'Y'): -3 , ('D', 'V'): -3,
        ('C', 'C'): 9, ('C', 'Q'): -3, ('C', 'E'): -4, ('C', 'G'): -3, ('C', 'H'): -3, ('C', 'I'): -1, ('C', 'L'): -1, ('C', 'K'): -3, ('C', 'M'): -1,
        ('C', 'F'): -2, ('C', 'P'): -3, ('C', 'S'): -1, ('C', 'T'): -1, ('C', 'W'): -2,
        ('C', 'Y'): -2, ('C', 'V'): -1,
        ('Q', 'Q'): 5, ('Q', 'E'): 2, ('Q', 'G'): -2, ('Q', 'H'): 0, ('Q', 'I'): -3,
        ('Q', 'L'): -2, ('Q', 'K'): 1, ('Q', 'M'): 0, ('Q', 'F'): -3, ('Q', 'P'): -1,
        ('Q', 'S'): 0, ('Q', 'T'): -1, ('Q', 'W'): -2, ('Q', 'Y'): -1, ('Q', 'V'): -2,
        ('E', 'E'): 5, ('E', 'G'): -2, ('E', 'H'): 0, ('E', 'I'): -3, ('E', 'L'): -3,
        ('E', 'K'): 1, ('E', 'M'): -2, ('E', 'F'): -3, ('E', 'P'): -1, ('E', 'S'): 0,
        ('E', 'T'): -1, ('E', 'W'): -3, ('E', 'Y'): -2, ('E', 'V'): -2,
        ('G', 'G'): 6, ('G', 'H'): -2, ('G', 'I'): -4, ('G', 'L'): -4, ('G', 'K'): -2,
        ('G', 'M'): -3, ('G', 'F'): -3, ('G', 'P'): -2, ('G', 'S'): 0,
        ('G', 'T'): -2, ('G', 'W'): -2, ('G', 'Y'): -3, ('G', 'V'): -3,
        ('H', 'H'): 8, ('H', 'I'): -3, ('H', 'L'): -3, ('H', 'K'): -1,
        ('H', 'M'): -2, ('H', 'F'): -1, ('H', 'P'): -2, ('H', 'S'): -1,
        ('H', 'T'): -2, ('H', 'W'): -2, ('H', 'Y'): 2, ('H', 'V'): -3,
        ('I', 'I'): 4, ('I', 'L'): 2, ('I', 'K'): -3, ('I', 'M'): 1,
        ('I', 'F'): 0, ('I', 'P'): -3, ('I', 'S'): -2, ('I', 'T'): -1,
        ('I', 'W'): -3, ('I', 'Y'): -1, ('I', 'V'): 3,
        ('L', 'L'): 4, ('L', 'K'): -2, ('L', 'M'): 2, ('L', 'F'): 0,
        ('L', 'P'): -3, ('L', 'S'): -2, ('L', 'T'): -1, ('L', 'W'): -2,
        ('L', 'Y'): -1, ('L', 'V'): 1,
        ('K', 'K'): 5, ('K', 'M'): -1, ('K', 'F'): -3, ('K', 'P'): -1,
        ('K', 'S'): 0, ('K', 'T'): -1, ('K', 'W'): -3, ('K', 'Y'): -2,
        ('K', 'V'): -2,
        ('M', 'M'): 5, ('M', 'F'): 0, ('M', 'P'): -2, ('M', 'S'): -1,
        ('M', 'T'): -1, ('M', 'W'): -1, ('M', 'Y'): -1, ('M', 'V'): 1,
        ('F', 'F'): 6, ('F', 'P'): -4, ('F', 'S'): -2, ('F', 'T'): -2,
        ('F', 'W'): 1, ('F', 'Y'): 3, ('F', 'V'): -1,
        ('P', 'P'): 7, ('P', 'S'): -1, ('P', 'T'): -1, ('P', 'W'): -4,
        ('P', 'Y'): -3 , ('P', 'V'): -2,
        ('S', 'S'): 4, ('S', 'T'): 1, ('S', 'W'): -3, ('S', 'Y'): -2,
        ('S', 'V'): -2,
        ('T', 'T'): 5, ('T', 'W'): -2, ('T', 'Y'): -2, ('T', 'V'): 0,
        ('W', 'W'): 11, ('W', 'Y'): 2, ('W', 'V'): -3,
        ('Y', 'Y'): 7, ('Y', 'V'): -1,
        ('V', 'V'): 4}

    # Initialisation des scores de correspondance, de non-correspondance et de trou
    match = 1
    mismatch = -1
    gap = -2

    # Initialisation de la matrice à 0
    init_mat = [[0] * (n + 1) for _ in range(m + 1)]

    # Remplissage de la première ligne et de la première colonne de la matrice
    for i in range(1, m + 1):
        init_mat[i][0] = gap * i

    for j in range(1, n + 1):
        init_mat[0][j] = gap * j

    # Remplissage de la matrice
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            match_score = blosum62.get((seq1[i - 1], seq2[j - 1]), mismatch)
            init_mat[i][j] = max(init_mat[i - 1][j - 1] + match_score,
                                 init_mat[i - 1][j] + gap,
                                 init_mat[i][j - 1] + gap)

    # Temps de départ
    start_time = time.time()

    # Initialisation des séquences alignées
    seq1_align = ""
    seq2_align = ""

    # Initialisation des indices de la matrice
    i = m
    j = n

    # Backtracking
    while i > 0 or j > 0:
        if i > 0 and j > 0 and init_mat[i][j] == init_mat[i - 1][j - 1] + blosum62.get((seq1[i - 1], seq2[j - 1]), mismatch):
            seq1_align = seq1[i - 1] + seq1_align
            seq2_align = seq2[j - 1] + seq2_align
            i -= 1
            j -= 1
        elif i > 0 and init_mat[i][j] == init_mat[i - 1][j] + gap:
            seq1_align = seq1[i - 1] + seq1_align
            seq2_align = '-' + seq2_align
            i -= 1
        else:
            seq1_align = '-' + seq1_align
            seq2_align = seq2[j - 1] + seq2_align
            j -= 1

    # Calcul du score d'alignement
    alignment_score = sum(blosum62.get((seq1_align[k], seq2_align[k]), mismatch) for k in range(len(seq1_align)))

    # Temps d'exécution
    execution_time = time.time() - start_time

    # Affichage des résultats de l'alignement
    print("Séquence 1 alignée:", seq1_align)
    print("Séquence 2 alignée:", seq2_align)
    print("Score d'alignement:", alignment_score)
    print("Temps d'exécution:", execution_time, "secondes")

    # Retourner les valeurs nécessaires dans un tuple
    return seq1_length, seq2_length, seq1_length + seq2_length, execution_time, alignment_score

# Liste pour stocker les résultats des alignements
results = []

# Boucle pour permettre à l'utilisateur de continuer ou de quitter
while True:
    choice = input("Voulez-vous faire un alignement? (o pour continuer, n pour quitter) : ")
    if choice.lower() == 'o':
        result = align_sequences()
        results.append(result)
    elif choice.lower() == 'n':
        print("Programme terminé.")
        break
    else:
        print("Entrée invalide. Veuillez entrer 'o' pour continuer ou 'n' pour quitter.")

# Affichage du tableau récapitulatif des résultats
print("\nTableau récapitulatif des résultats :")
print("{:<12} {:<12} {:<16} {:<20} {:<16}".format("Taille seq 1", "Taille seq 2", "Taille globale", "Temps d'exécution", "Score d'alignement"))
for result in results:
    seq1_len, seq2_len, global_len, exec_time, alignment_score = result
    print("{:<12} {:<12} {:<16} {:<20.6f} {:<16}".format(seq1_len, seq2_len, global_len, exec_time, alignment_score))

# Affichage du tableau final des résultats dans le format spécifié
print("\nSequence 1   Sequence 2   Taille globale   Temps d'exécution   Score d'alignement")
for result in results:
    seq1_len, seq2_len, global_len, exec_time, alignment_score = result
    print("{:<12} {:<12} {:<16} {:<20.6f} {:<16}".format(seq1_len, seq2_len, global_len, exec_time, alignment_score))
