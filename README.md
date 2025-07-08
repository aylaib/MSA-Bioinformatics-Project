\# Implémentation et Comparaison d'Algorithmes d'Alignement Multiple de Séquences



Ce projet, réalisé dans le cadre du module Bio-Algorithmique (Master 1 Bio-Informatique, USTHB), explore l'implémentation et l'analyse de performance de différentes méthodes pour l'alignement multiple de séquences (MSA).



L'objectif principal est de comparer deux approches fondamentales : l'\*\*approche progressive\*\* (heuristique) et l'\*\*approche itérative\*\* basée sur un algorithme génétique (SAGA).



\## 📊 Analyse Comparative des Performances



Le script `Comp.py` analyse les données de temps d'exécution des deux principales méthodes et génère le graphique comparatif suivant, démontrant la différence de performance en termes de vitesse entre l'approche progressive et SAGA.



\*(Astuce : Exécutez `python Comp.py`, sauvegardez le graphique généré en tant que `comparison\_plot.png` dans ce dossier, et décommentez la ligne ci-dessous en la remplaçant par le bon nom de fichier.)\*



!\[Comparaison des temps d'exécution](./comparison\_plot.png)



\## 🤖 Algorithmes Implémentés



Ce dépôt contient une collection de scripts Python, chacun démontrant un algorithme ou un concept clé :



1\.  \*\*`Needelman.py` : Alignement par Paire (Needleman-Wunsch)\*\*

&nbsp;   - Implémente l'algorithme de programmation dynamique classique pour l'alignement global de deux séquences.

&nbsp;   - Utilise la matrice de similarité \*\*BLOSUM62\*\* et une pénalité de gap linéaire.

&nbsp;   - Génère des séquences protéiques aléatoires pour les tests.



2\.  \*\*`ProgressiveMultiple.py` : Alignement Multiple Progressif\*\*

&nbsp;   - Une implémentation d'une méthode heuristique rapide pour l'alignement multiple.

&nbsp;   - Aligne progressivement les séquences en se basant sur un profil qui est mis à jour à chaque étape.

&nbsp;   - Très efficace en temps de calcul, c'est une approche similaire à celle utilisée par des outils comme ClustalW.



3\.  \*\*`SAGA.py` : Alignement par Algorithme Génétique (SAGA)\*\*

&nbsp;   - Implémente une méthode itérative qui utilise les principes de l'évolution (sélection, croisement, mutation) pour trouver un alignement de haute qualité.

&nbsp;   - Vise à optimiser un score d'alignement sur plusieurs générations.

&nbsp;   - Bien que plus lent, cet algorithme peut potentiellement trouver de meilleurs alignements pour des cas complexes.



4\.  \*\*`Comp.py` : Script d'Analyse et de Visualisation\*\*

&nbsp;   - Ne réalise pas d'alignement.

&nbsp;   - Prend en entrée des données de performance (temps d'exécution) et utilise `matplotlib` pour visualiser la comparaison entre les méthodes.



\## 🚀 Comment l'Exécuter



Chaque script est autonome et peut être exécuté individuellement.



1\.  \*\*Clonez le dépôt :\*\*

&nbsp;   ```bash

&nbsp;   git clone https://github.com/VOTRE\_NOM\_UTILISATEUR/MSA-Bioinformatics-Project.git

&nbsp;   cd MSA-Bioinformatics-Project

&nbsp;   ```

2\.  \*\*Installez les dépendances :\*\*

&nbsp;   ```bash

&nbsp;   pip install -r requirements.txt

&nbsp;   ```

3\.  \*\*Exécutez le script de votre choix :\*\*

&nbsp;   - Pour l'alignement par paire :

&nbsp;     ```bash

&nbsp;     python Needelman.py

&nbsp;     ```

&nbsp;   - Pour l'alignement progressif :

&nbsp;     ```bash

&nbsp;     python ProgressiveMultiple.py

&nbsp;     ```

&nbsp;   - Pour l'alignement avec SAGA :

&nbsp;     ```bash

&nbsp;     python SAGA.py

&nbsp;     ```

&nbsp;   - Pour générer le graphique de comparaison :

&nbsp;     ```bash

&nbsp;     python Comp.py

&nbsp;     ```

Chaque script vous guidera en vous demandant les paramètres nécessaires (taille des séquences, nombre de séquences, etc.).



\## 📚 Documents de Référence

\- \*\*\[Rapport Complet du Projet](./rapport\_alignement\_multiple.pdf)\*\* : Ce document contient l'analyse théorique détaillée, la méthodologie, les résultats des tests et la conclusion du projet.

\- \*\*\[Énoncé du Projet](./enonce\_projet.pdf)\*\* : Le cahier des charges original du mini-projet.

