from stats import count_words, count_characters, sort_character_counts



def get_book_text(file_path):
    """
    Lit le contenu d'un fichier et retourne le texte en tant que chaîne.

    :param file_path: Le chemin du fichier à lire.
    :return: Le contenu du fichier sous forme de chaîne.
    """
    with open(file_path, "r") as f:
        return f.read()




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
    text = get_book_text(file_path)
    #print(text)

    # Compter les mots dans le texte
    num_words = count_words(text)
    print(f"{num_words} words found in the document")

    # Compter les fréquences des caractères
    #char_counts = count_characters(text)

    # Afficher le rapport
    #print_report(file_path, word_count, char_counts)


# Exécuter le programme
if __name__ == "__main__":
    main()