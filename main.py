def read_file(file_path):
    """
    Lit le contenu d'un fichier et retourne le texte en tant que chaîne.

    :param file_path: Le chemin du fichier à lire.
    :return: Le contenu du fichier sous forme de chaîne.
    """
    with open(file_path, "r") as f:
        return f.read()


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


def print_report(file_path, word_count, char_counts):
    """
    Affiche un rapport formaté des fréquences des mots et des caractères.
    
    :param file_path: Le chemin du fichier analysé.
    :param word_count: Le nombre total de mots dans le fichier.
    :param char_counts: Un dictionnaire des fréquences des caractères.
    """
    # Trier les fréquences des caractères
    sorted_char_counts = sort_character_counts(char_counts)

    # Imprimer le rapport
    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document\n")

    for item in sorted_char_counts:
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def main():
    """
    Point d'entrée principal du programme.
    """
    # Chemin du fichier à analyser
    file_path = "books/frankenstein.txt"

    # Lire le contenu du fichier
    text = read_file(file_path)

    # Compter les mots dans le texte
    word_count = count_words(text)

    # Compter les fréquences des caractères
    char_counts = count_characters(text)

    # Afficher le rapport
    print_report(file_path, word_count, char_counts)


# Exécuter le programme
if __name__ == "__main__":
    main()