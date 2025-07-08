import matplotlib.pyplot as plt

# Données pour l'approche progressive
progressive_times = {
    50: [0.005997, 0.007995, 0.009996, 0.013001, 0.015674, 0.020004, 0.022006, 0.023264],
    100: [0.006001, 0.008819, 0.010009, 0.013003, 0.017540, 0.018006, 0.023532, 0.027161],
    150: [0.005999, 0.009017, 0.011643, 0.016126, 0.018538, 0.014998, 0.020193, 0.029035],
    200: [0.007002, 0.011000, 0.015999, 0.020056, 0.021024, 0.026688, 0.033043, 0.038176],
    300: [0.007563, 0.011316, 0.020013, 0.021534, 0.026227, 0.033032, 0.062521, 0.040670]
}

# Données pour la méthode SAGA (itérative)
saga_times = {
    50: [0.302025, 0.186595, 0.227634, 0.368311, 0.266054, 0.274393, 0.300085, 0.357844],
    100: [0.241544, 0.326585, 0.293261, 0.340454, 0.403734, 0.387194, 0.409754, 0.463689],
    150: [0.285552, 0.321794, 0.418824, 0.422699, 0.442606, 0.494291, 0.509848, 0.548218],
    200: [0.330859, 0.406071, 0.424856, 0.498104, 0.509691, 0.617193, 0.810479, 0.933210],
    300: [0.436182, 0.511508, 0.631581, 0.652109, 0.736005, 0.769468, 0.804323, 0.913221]
}

def calculate_average(times_dict):
    average_times = {}
    for key, values in times_dict.items():
        average_times[key] = sum(values) / len(values)
    return average_times

# Calcul des moyennes
average_progressive_times = calculate_average(progressive_times)
average_saga_times = calculate_average(saga_times)

# Affichage des résultats
print("Moyenne des temps d'exécution pour l'approche progressive:")
for key, value in average_progressive_times.items():
    print(f"Taille de séquence {key}: {value:.6f} s")

print("\nMoyenne des temps d'exécution pour la méthode SAGA:")
for key, value in average_saga_times.items():
    print(f"Taille de séquence {key}: {value:.6f} s")

# Tracé des graphes
x_values = list(average_progressive_times.keys())
y_progressive = list(average_progressive_times.values())
y_saga = list(average_saga_times.values())

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_progressive, marker='o', linestyle='-', color='b', label='Approche Progressive')
plt.plot(x_values, y_saga, marker='s', linestyle='--', color='r', label='Méthode SAGA')

plt.xlabel('Taille de séquence')
plt.ylabel('Moyenne des temps d\'exécution (s)')
plt.title('Comparaison des temps d\'exécution moyens')
plt.legend()
plt.grid(True)
plt.show()
