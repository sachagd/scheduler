Pour utiliser le code il faut deux fichiers dans le même dossier que l'exécutable: 
    - auteurs.csv
    - producteurs.csv

Les noms sont importants et ça doit être des .csv (convertir si jamais)

Les fichiers doivent être de la forme suivante : 
    - la première ligne : Nom, Souhait_1, Souhait_2....
    - chaque ligne après : le nom d'un auteur/producteur puis sa liste de souhaits
    - la première colonne : le nom des auteurs/producteurs

Le nombre de souhaits n'est pas limité, laissez des cases vides pour ceux qui en ont moins

Dans le fichier auteurs (resp. producteurs) le noms des producteurs (resp. auteurs) donnés en souhaits doivent apparaitre dans la première colonne du fichier producteurs (resp. auteurs) sinon l'exécution provoquera une erreur.
En gros, ne faites pas de typo dans les listes de souhaits.

Le nombre de créneaux voulu est à spécifier dans le fichier ncreneau.txt