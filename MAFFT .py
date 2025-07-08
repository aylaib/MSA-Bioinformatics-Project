import random
import time

# Générer une séquence aléatoire de nucléotides de longueur donnée
def generate_sequence(length):
    nucleotides = ['A', 'T', 'C', 'G']
    return ''.join(random.choices(nucleotides, k=length))

# Fonction pour calculer le temps d'exécution
def calculate_execution_time(start_time):
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

# Fonction pour aligner deux séquences avec un alignement global simple
def align_sequences(seq1, seq2):
    len1, len2 = len(seq1), len(seq2)
    score_matrix = [[0] * (len2 + 1) for _ in range(len1 + 1)]
    gap_penalty = -1
    match_score = 1
    mismatch_penalty = -1

    # Initialisation de la première ligne et première colonne de la matrice de score
    for i in range(len1 + 1):
        score_matrix[i][0] = gap_penalty * i
    for j in range(len2 + 1):
        score_matrix[0][j] = gap_penalty * j

    # Remplissage de la matrice de score
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            match = score_matrix[i-1][j-1] + (match_score if seq1[i-1] == seq2[j-1] else mismatch_penalty)
            delete = score_matrix[i-1][j] + gap_penalty
            insert = score_matrix[i][j-1] + gap_penalty
            score_matrix[i][j] = max(match, delete, insert)

    # Traçage de l'alignement à partir de la matrice de score
    aligned_seq1 = ""
    aligned_seq2 = ""
    i, j = len1, len2
    while i > 0 and j > 0:
        score_current = score_matrix[i][j]
        score_diagonal = score_matrix[i-1][j-1]
        score_up = score_matrix[i][j-1]
        score_left = score_matrix[i-1][j]
        if score_current == score_diagonal + (match_score if seq1[i-1] == seq2[j-1] else mismatch_penalty):
            aligned_seq1 = seq1[i-1] + aligned_seq1
            aligned_seq2 = seq2[j-1] + aligned_seq2
            i -= 1
            j -= 1
        elif score_current == score_left + gap_penalty:
            aligned_seq1 = seq1[i-1] + aligned_seq1
            aligned_seq2 = '-' + aligned_seq2
            i -= 1
        elif score_current == score_up + gap_penalty:
            aligned_seq1 = '-' + aligned_seq1
            aligned_seq2 = seq2[j-1] + aligned_seq2
            j -= 1

    while i > 0:
        aligned_seq1 = seq1[i-1] + aligned_seq1
        aligned_seq2 = '-' + aligned_seq2
        i -= 1
    while j > 0:
        aligned_seq1 = '-' + aligned_seq1
        aligned_seq2 = seq2[j-1] + aligned_seq2
        j -= 1

    return aligned_seq1, aligned_seq2

# Fonction pour aligner une séquence avec un profil
def align_with_profile(seq, profile):
    return align_sequences(seq, profile)[1]

# Fonction pour construire un profil à partir d'alignements
def build_profile(aligned_sequences):
    profile = ""
    for bases in zip(*aligned_sequences):
        base_counts = {base: bases.count(base) for base in set(bases)}
        most_common_base = max(base_counts, key=base_counts.get)
        profile += most_common_base
    return profile

# Fonction d'alignement progressif
def progressive_alignment(sequences):
    start_time = time.time()
    aligned_sequences = [sequences[0]]
    for i in range(1, len(sequences)):
        seq_to_align = sequences[i]
        profile = build_profile(aligned_sequences)
        aligned_seq = align_with_profile(seq_to_align, profile)
        aligned_sequences.append(aligned_seq)
        print(f"\nAlignement progressif étape {i} :")
        print(f"Séquence {i + 1} alignée : {aligned_seq}")
        print(f"Profil {i + 1} : {profile}")
    execution_time = calculate_execution_time(start_time)
    print(f"\nTemps total d'exécution : {execution_time:.6f} secondes")
    return aligned_sequences

# Demander à l'utilisateur d'entrer le nombre de séquences et leur taille
num_sequences = int(input("Entrez le nombre de séquences : "))
seq_length = int(input("Entrez la taille de chaque séquence : "))

# Générer les séquences aléatoires de nucléotides
sequences = [generate_sequence(seq_length) for _ in range(num_sequences)]

# Afficher les séquences générées
print("\nSéquences générées :")
for i, seq in enumerate(sequences, start=1):
    print(f"Séquence {i} : {seq}")

# Effectuer l'alignement multiple progressif
aligned_sequences = progressive_alignment(sequences)
