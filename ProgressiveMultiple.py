import random
import time

# Déclaration des variables globales pour stocker les informations
alignments_info = []

# Générer une séquence aléatoire de nucléotides de longueur donnée
def generate_sequence(length):
    nucleotides = ['A', 'T', 'C', 'G']
    return ''.join(random.choices(nucleotides, k=length))

# Demander à l'utilisateur d'entrer la taille des séquences
def get_sequence_length():
    seq_length = int(input("Entrez la taille de chaque séquence : "))
    return seq_length

# Demander à l'utilisateur d'entrer le nombre de séquences
def get_num_sequences():
    num_sequences = int(input("Entrez le nombre de séquences : "))
    return num_sequences

# Générer les séquences aléatoires de nucléotides
def generate_sequences(num_sequences, seq_length):
    sequences = [generate_sequence(seq_length) for _ in range(num_sequences)]
    return sequences

# Afficher les séquences générées
def display_sequences(sequences):
    print("Séquences générées :")
    for i, seq in enumerate(sequences, start=1):
        print(f"Séquence {i} : {seq}")

# Alignement simple de deux séquences
def align_sequences(seq1, seq2):
    aligned_seq1 = ""
    aligned_seq2 = ""
    for base1, base2 in zip(seq1, seq2):
        if base1 == base2:
            aligned_seq1 += base1
            aligned_seq2 += base2
        else:
            aligned_seq1 += "-"
            aligned_seq2 += "-"
    return aligned_seq1, aligned_seq2

# Alignement d'une séquence avec un profil
def align_with_profile(seq, profile):
    aligned_seq = ""
    for base, profile_base in zip(seq, profile):
        if base == profile_base or profile_base == '-':
            aligned_seq += base
        else:
            aligned_seq += "-"
    return aligned_seq

# Construction d'un profil à partir d'alignements
def build_profile(aligned_sequences):
    profile = ""
    for bases in zip(*aligned_sequences):
        base_counts = {}
        for base in bases:
            base_counts[base] = base_counts.get(base, 0) + 1
        most_common_base = max(base_counts, key=base_counts.get)
        profile += most_common_base
    return profile

# Construction d'une matrice de distances entre toutes les séquences
def build_distance_matrix(sequences):
    distance_matrix = []
    for i in range(len(sequences)):
        distances = []
        for j in range(len(sequences)):
            if i != j:
                distance = sum(a != b for a, b in zip(sequences[i], sequences[j]))
                distances.append(distance)
            else:
                distances.append(0)
        distance_matrix.append(distances)
    return distance_matrix

# Détermination de l'ordre des alignements en fonction des distances
def determine_alignment_order(distance_matrix):
    order = []
    remaining_sequences = set(range(len(distance_matrix)))
    while remaining_sequences:
        min_distance = float('inf')
        closest_pair = None
        for i in remaining_sequences:
            for j in remaining_sequences:
                if i != j and distance_matrix[i][j] < min_distance:
                    min_distance = distance_matrix[i][j]
                    closest_pair = (i, j)
        order.append(closest_pair)
        remaining_sequences -= set(closest_pair)
    return order

def progressive_alignment(sequences):
    aligned_sequences = [sequences[0]]
    profiles = [sequences[0]]  # Initialiser le premier profil avec la première séquence
    start_time = time.time()  # Commencer à mesurer le temps d'exécution
    for i in range(1, len(sequences)):
        seq_to_align = sequences[i]
        profile = build_profile(aligned_sequences)
        aligned_seq = align_with_profile(seq_to_align, profile)
        aligned_sequences.append(aligned_seq)
        profiles.append(profile)
        print("\nAlignement progressif étape", i, ":")
        print(f"Séquence {i + 1} alignée : {aligned_seq}")
        print(f"Profil {i + 1} : {profile}")

    end_time = time.time()  # Finir de mesurer le temps d'exécution
    execution_time = end_time - start_time  # Calculer le temps total d'exécution
    alignments_info.append((len(sequences[0]), len(sequences), execution_time))  # Stocker les informations de l'alignement
    print(f"Temps total d'exécution : {execution_time:.6f} secondes")  # Afficher le temps total d'exécution

# Boucle principale pour permettre à l'utilisateur de faire plusieurs alignements
while True:
    print("\nNouvel alignement :")
    seq_length = get_sequence_length()  # Demander la taille des séquences
    num_sequences = get_num_sequences()  # Demander le nombre de séquences
    sequences = generate_sequences(num_sequences, seq_length)
    display_sequences(sequences)
    progressive_alignment(sequences)
    choice = input("Voulez-vous faire un autre alignement? (o pour continuer, n pour quitter) : ")
    if choice.lower() != 'o':
        print("Programme terminé.")
        break

# Affichage du tableau d'informations
print("\nTableau d'informations :")
print(f"{'Taille séquence':<20}{'Nombre de séquences':<20}{'Temps dexécution':<20}")
for info in alignments_info:
    print(f"{info[0]:<20}{info[1]:<20}{info[2]:.6f} secondes")
