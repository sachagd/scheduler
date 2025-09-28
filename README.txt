Pour utiliser le code il faut trois fichiers dans le même dossier que l'exécutable: 
    - auteurs.csv
    - producteurs.csv
    - contraintes.csv

Les noms sont importants et ça doit être des .csv (convertir si jamais)

Les fichiers auteurs.csv et producteurs.csv doivent être de la forme suivante : 
    - la première ligne : Nom, Souhait_1, Souhait_2....
    - chaque ligne après : le nom d'un auteur/producteur puis sa liste de souhaits
    - la première colonne : le nom des auteurs/producteurs

Le nombre de souhaits n'est pas limité, laissez des cases vides pour ceux qui en ont moins

Dans le fichier auteurs (resp. producteurs) le noms des producteurs (resp. auteurs) donnés en souhaits doivent apparaitre dans la première colonne du fichier producteurs (resp. auteurs) sinon l'exécution provoquera une erreur.
En gros, ne faites pas de typo dans les listes de souhaits.

Le nombre de créneaux voulu est à spécifier dans le fichier ncreneau.txt

Même s'il n'y a pas de contraintes il faut un fichier contraintes.csv donc laissez le vide.
Sinon le fichier contraintes.csv doit être de la forme suivante : 
    - la première ligne : Nom, Contraintes
    - chaque ligne après : le nom d'un auteur/producteur puis des éléments du type "a-b" avec a et b des numéros de créneaux. Ce qui veut dire untel sera là du créneau a au b tout deux inclus.
    - la première colonne : le nom des auteurs/producteurs