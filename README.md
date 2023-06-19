# DS-P6-Classifiez-automatiquement-des-biens-de-consommation

Projet 6 Classifiez automatiquement des biens de consommation 

Ce projet consiste à développer un moteur de classification d'articles pour une marketplace e-commerce. L'objectif est d'automatiser l'attribution des catégories aux articles en se basant sur leurs images et descriptions.

# Objectifs
- Faciliter la mise en ligne de nouveaux articles par les vendeurs.
- Améliorer l'expérience utilisateur des acheteurs en facilitant la recherche de produits.
- Automatiser la classification des articles en différentes catégories avec un niveau de précision élevé.

# Itération 1 - Étude de faisabilité
Dans cette première itération, les tâches à réaliser sont les suivantes :

1 - Prétraitement des données textuelles et des images.
2 - Extraction de caractéristiques (features) des données.
3 - Réduction des données en 2 dimensions pour les visualiser sur un graphique.
4 - Analyse du graphique pour évaluer la possibilité de regrouper automatiquement des produits de même catégorie.
5 - Calcul de similarité entre les catégories réelles et les catégories issues d'une segmentation en clusters.

Contraintes pour l'extraction des features textuelles :

- Utilisation de deux approches "bag-of-words" : comptage simple de mots et Tf-idf.
- Utilisation d'approches de type word/sentence embedding avec Word2Vec, Glove, FastText, BERT, et USE (Universal Sentence Encoder).

Contraintes pour l'extraction des features d'images :

- Utilisation d'algorithmes de type SIFT, ORB, SURF.
- Utilisation d'algorithmes de type CNN Transfer Learning.

# Itération 2 - Classification Supervisée et Data Augmentation
Après avoir démontré la faisabilité de regrouper automatiquement des produits de même catégorie, nous passons à la deuxième itération. Les tâches pour cette itération sont les suivantes :

1 - Réalisation d'une classification supervisée à partir des images des articles.
2 - Mise en place de la data augmentation pour optimiser le modèle.

# Élargissement de la Gamme de Produits

Dans le cadre de l'élargissement de la gamme de produits, nous souhaitons tester la collecte de produits à base de "champagne" via une API disponible. Nous demandons la fourniture d'un fichier ".csv" contenant les 10 premiers produits extraits, avec les colonnes suivantes : foodId, label, category, foodContentsLabel, image.





