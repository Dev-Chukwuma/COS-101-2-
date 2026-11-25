translations = {
    "hello": {
        "Igbo": "Ndewo",
        "Hausa": "Sannu",
        "Yoruba": "Pẹlẹ o",
        "Idoma": "À gbè hìì",
        "Tiv": "M sugh u"
    },
    "thank you": {
        "Igbo": "Daalụ",
        "Hausa": "Na gode",
        "Yoruba": "Ẹ ṣé",
        "Idoma": "Ainya / Ahinya",
        "Tiv": "M sugh 7"
    },
    "good morning": {
        "Igbo": "Ụtụtụ ọma",
        "Hausa": "Ina kwana",
        "Yoruba": "Ẹ káàárọ̀",
        "Idoma": "Nmaochi",
        "Tiv": "U nder"
    },
    "good night": {
        "Igbo": "Ka chi foo",
        "Hausa": "Barka da dare",
        "Yoruba": "Ó dàárọ̀",
        "Idoma": "Nmoo",
        "Tiv": "Yav dedo"
    },
    "water": {
        "Igbo": "Mmiri",
        "Hausa": "Ruwa",
        "Yoruba": "Omi",
        "Idoma": "Ènyí",
        "Tiv": "Mngerem"
    },
    "food": {
        "Igbo": "Nri",
        "Hausa": "Abinci",
        "Yoruba": "Oúnjẹ",
        "Idoma": "Odre",
        "Tiv": "Kwaghyan"
    },
    "house": {
        "Igbo": "Ụlọ",
        "Hausa": "Gida",
        "Yoruba": "Ilé",
        "Idoma": "Ole",
        "Tiv": "Ya"
    },
    "school": {
        "Igbo": "Ụlọ akwụkwọ",
        "Hausa": "Makaranta",
        "Yoruba": "Ilé ẹ̀kọ́",
        "Idoma": "Inokpa",
        "Tiv": "Ikyogh"
    },
    "book": {
        "Igbo": "Akwụkwọ",
        "Hausa": "Littafi",
        "Yoruba": "Ìwé",
        "Idoma": "Okpa",
        "Tiv": "Takerada"
    },
    "friend": {
        "Igbo": "Enyi",
        "Hausa": "Aboki",
        "Yoruba": "Ọ̀rẹ́",
        "Idoma": "Oya",
        "Tiv": "Huror"
    },
    "mother": {
        "Igbo": "Nne",
        "Hausa": "Uwa",
        "Yoruba": "Ìyá",
        "Idoma": "Ene",
        "Tiv": "Ngo"
    },
    "father": {
        "Igbo": "Nna",
        "Hausa": "Uba",
        "Yoruba": "Bàbá",
        "Idoma": "Ada",
        "Tiv": "Baba"
    },
    "child": {
        "Igbo": "Nwa",
        "Hausa": "Yaro",
        "Yoruba": "Ọmọ",
        "Idoma": "Oyi",
        "Tiv": "Wan"
    },
    "love": {
        "Igbo": "Ịhụnanya",
        "Hausa": "Ƙauna",
        "Yoruba": "Ìfẹ́",
        "Idoma": "Ihotu",
        "Tiv": "Dooshima"
    },
    "come": {
        "Igbo": "Bịa",
        "Hausa": "Zo",
        "Yoruba": "Wá",
        "Idoma": "Wā",
        "Tiv": "Va"
    },
    "go": {
        "Igbo": "Gaa",
        "Hausa": "Je",
        "Yoruba": "Lọ",
        "Idoma": "Nyɔ",
        "Tiv": "Za"
    },
    "sit": {
        "Igbo": "Nọdụ ala",
        "Hausa": "Zauna",
        "Yoruba": "Jókòó",
        "Idoma": "Chíchē",
        "Tiv": "Tema nya"
    },
    "eat": {
        "Igbo": "Rie",
        "Hausa": "Ci",
        "Yoruba": "Jẹun",
        "Idoma": "Lé",
        "Tiv": "Yan"
    },
    "drink": {
        "Igbo": "Ṅụọ",
        "Hausa": "Sha",
        "Yoruba": "Mu",
        "Idoma": "Gwá",
        "Tiv": "Ma"
    },
    "welcome": {
        "Igbo": "Nnọọ",
        "Hausa": "Barka da zuwa",
        "Yoruba": "Ẹ káàbọ̀",
        "Idoma": "Ainya owa",
        "Tiv": "M sugh u Za Van"
    }
}

def welcome_message():
    print("\n" + "=" * 45)
    print("       MULTILINGUAL TRANSLATION SYSTEM")
    print("=" * 45)
    print("Welcome! Translate English into Nigerian languages.")
    print("Available languages: 5")
    print("Available words and phrases: 20")
    print("=" * 45)


def select_language():

    languages = ["Igbo", "Hausa", "Yoruba", "Idoma", "Tiv"]

    while True:

        print("\nSELECT YOUR LANGUAGE")

        for number, language in enumerate(languages, start=1):
            print(f"{number}. {language}")

        choice = input("\nChoose a language (1-5): ").strip()

        if choice in ["1", "2", "3", "4", "5"]:
            selected_language = languages[int(choice) - 1]

            print(f"\nYou selected: {selected_language}")

            return selected_language

        else:
            print("Invalid selection! Please choose a number from 1 to 5.")
def display_words():

    print("\nAVAILABLE ENGLISH WORDS")

    for number, word in enumerate(translations.keys(), start=1):
        print(f"{number}. {word.title()}")


def translate_word(language):

    word = input("\nEnter an English word or phrase: ").strip().lower()

    if word in translations:

        result = translations[word][language]

        print("\n" + "-" * 40)
        print("TRANSLATION RESULT")
        print("-" * 40)
        print(f"English: {word.title()}")
        print(f"{language}: {result}")
        print("-" * 40)

    else:
        print("\nSorry! This word is not available.")
        print("Please choose a word from the available list.")

def translate_all(language):

    print("\n" + "=" * 45)
    print(f"       ALL TRANSLATIONS IN {language.upper()}")
    print("=" * 45)

    for number, (word, language_data) in enumerate(
        translations.items(), start=1
    ):
        print(f"{number}. {word.title()} = {language_data[language]}")

    print("=" * 45)


def main_menu(language):

    while True:

        print("\n" + "=" * 45)
        print("             MAIN MENU")
        print("=" * 45)
        print(f"Selected Language: {language}")
        print("1. Translate a word")
        print("2. View available English words")
        print("3. Translate all 20 words")
        print("4. Change language")
        print("5. Exit")
        print("=" * 45)

        choice = input("Select an option (1-5): ").strip()

        if choice == "1":

            translate_word(language)

        elif choice == "2":

            display_words()

        elif choice == "3":

            translate_all(language)

        elif choice == "4":

            language = select_language()

        elif choice == "5":

            print("\nThank you for using our translation system!")
            print("Goodbye!")
            break

        else:

            print("\nInvalid option! Please select between 1 and 5.")
