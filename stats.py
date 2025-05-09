def count_words(text):
    """
    Compte le nombre de mots dans une chaîne de texte.

    :param text: Le texte à analyser.
    :return: Le nombre total de mots dans le texte.
    """
    words = text.split()  # Diviser le texte en mots
    return len(words)


def count_characters(text):
    """
    Compte les occurrences de chaque caractère alphabétique dans une chaîne de texte.

    :param text: Le texte à analyser.
    :return: Un dictionnaire des caractères et de leurs fréquences.
    """
    char_counts = {}
    for char in text.lower():  # Convertir tous les caractères en minuscules
        if char.isalpha():  # Vérifier si le caractère est une lettre
            if char not in char_counts:
                char_counts[char] = 0
            char_counts[char] += 1  # Incrémenter le compteur pour le caractère
    return char_counts


def sort_character_counts(char_counts):
    """
    Trie les fréquences des caractères par ordre décroissant.

    :param char_counts: Un dictionnaire des fréquences des caractères.
    :return: Une liste de dictionnaires triés avec les caractères et leurs fréquences.
    """
    # Créer une liste de dictionnaires à partir du dictionnaire des fréquences
    char_list = []
    for char, count in char_counts.items():
        char_list.append({"char": char, "num": count})
    
    # Trier la liste des dictionnaires par fréquence (num) en ordre décroissant
    for i in range(len(char_list)):
        for j in range(i + 1, len(char_list)):
            if char_list[i]["num"] < char_list[j]["num"]:
                # Échanger les éléments si nécessaire
                char_list[i], char_list[j] = char_list[j], char_list[i]

    return char_list
