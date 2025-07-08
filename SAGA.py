import random
import time

# Générer une séquence aléatoire de nucléotides de longueur donnée
def generate_sequence(length):
    nucleotides = ['A', 'T', 'C', 'G']
    return ''.join(random.choices(nucleotides, k=length))

# Fonction pour évaluer un alignement (score simplifié)
def evaluate_alignment(alignment):
    score = 0
    for i in range(len(alignment[0])):
        column = [seq[i] for seq in alignment]
        if len(set(column)) == 1:  # Tous les éléments de la colonne sont identiques
            score += 1
    return score

# Fonction pour aligner deux séquences en les complétant avec des gaps
def align_sequences(seq1, seq2):
    max_len = max(len(seq1), len(seq2))
    seq1 += '-' * (max_len - len(seq1))
    seq2 += '-' * (max_len - len(seq2))
    return seq1, seq2

# Fonction pour créer une population initiale d'alignements
def create_initial_population(sequences, population_size):
    population = []
    for _ in range(population_size):
        alignment = sequences[:]
        random.shuffle(alignment)
        population.append(alignment)
    return population

# Fonction pour effectuer une mutation sur un alignement
def mutate_alignment(alignment):
    idx = random.randint(0, len(alignment) - 1)
    seq = alignment[idx]
    if random.random() < 0.5:
        # Insertion d'un gap
        pos = random.randint(0, len(seq))
        alignment[idx] = seq[:pos] + '-' + seq[pos:]
    else:
        # Suppression d'un gap
        seq = seq.replace('-', '')
        alignment[idx] = seq
    # Ajuster toutes les séquences à la même longueur
    max_len = max(len(seq) for seq in alignment)
    for i in range(len(alignment)):
        alignment[i] += '-' * (max_len - len(alignment[i]))
    return alignment

# Fonction pour croiser deux alignements (croisement simple)
def crossover_alignment(parent1, parent2):
    if parent1 is None or parent2 is None:
        return None, None
    cross_point = random.randint(1, len(parent1[0]) - 1)
    child1 = [seq[:cross_point] + seq2[cross_point:] for seq, seq2 in zip(parent1, parent2)]
    child2 = [seq2[:cross_point] + seq[cross_point:] for seq, seq2 in zip(parent1, parent2)]
    # Ajuster toutes les séquences à la même longueur
    max_len = max(len(seq) for seq in child1 + child2)
    for i in range(len(child1)):
        child1[i] += '-' * (max_len - len(child1[i]))
        child2[i] += '-' * (max_len - len(child2[i]))
    return child1, child2

# Fonction pour la sélection des alignements (roulette wheel selection)
def select_alignment(population, scores):
    max_score = sum(scores)
    if max_score == 0:
        return random.choice(population)
    pick = random.uniform(0, max_score)
    current = 0
    for alignment, score in zip(population, scores):
        current += score
        if current > pick:
            return alignment
    return random.choice(population)

# Fonction principale pour l'algorithme SAGA
def saga_algorithm(sequences, population_size=10, generations=50):
    population = create_initial_population(sequences, population_size)
    best_alignment = None
    best_score = 0

    for generation in range(generations):
        scores = [evaluate_alignment(alignment) for alignment in population]
        next_generation = []

        while len(next_generation) < population_size:
            parent1 = select_alignment(population, scores)
            parent2 = select_alignment(population, scores)
            if parent1 is None or parent2 is None:
                continue
            child1, child2 = crossover_alignment(parent1, parent2)
            if child1 is not None and child2 is not None:
                next_generation.append(mutate_alignment(child1))
                next_generation.append(mutate_alignment(child2))

        population = next_generation[:population_size]

        for alignment in population:
            score = evaluate_alignment(alignment)
            if score > best_score:
                best_score = score
                best_alignment = alignment

        print(f"Génération {generation + 1}, meilleur score : {best_score}")

    return best_alignment, best_score

def run_alignment_generation(seq_length, num_sequences):
    while True:
        # Générer les séquences aléatoires de nucléotides
        sequences = [generate_sequence(seq_length) for _ in range(num_sequences)]

        # Afficher les séquences générées
        print("\nSéquences générées :")
        for i, seq in enumerate(sequences, start=1):
            print(f"Séquence {i} : {seq}")

        # Exécuter l'algorithme SAGA
        start_time = time.time()
        best_alignment, best_score = saga_algorithm(sequences)
        end_time = time.time()
        execution_time = end_time - start_time

        # Afficher les résultats
        print("\nMeilleur alignement trouvé :")
        for seq in best_alignment:
            print(seq)
        print(f"\nScore de l'alignement : {best_score}")
        print(f"\nTemps total d'exécution : {execution_time:.6f} secondes")

        # Demander à l'utilisateur s'il souhaite continuer
        choice = input("Voulez-vous continuer ? (o/n) ").lower()
        if choice != 'o':
            break

        # Demander à l'utilisateur d'entrer le nombre de séquences à nouveau
        num_sequences = int(input("Entrez le nombre de séquences : "))

# Demander à l'utilisateur d'abord d'entrer la taille de chaque séquence
seq_length = int(input("Entrez la taille de chaque séquence : "))

# Demander à l'utilisateur d'entrer le nombre de séquences
num_sequences = int(input("Entrez le nombre de séquences : "))

# Exécuter l'alignement avec les paramètres donnés
run_alignment_generation(seq_length, num_sequences)
