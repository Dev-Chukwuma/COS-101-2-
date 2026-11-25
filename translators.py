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
