import random

def generate_random_name_list():
    # Erstellt eine Liste von 1-100
    namen_liste = [f"User {i}" for i in range(1, 101)]
    # Liste der Namen mischen
    random.shuffle(namen_liste)
    return namen_liste

def get_random_name(namen_liste):
    # Hier Fragen ob er Name will
    while True:
        choice = input("Möchtest du einen Namen?: ").strip().lower()
        if choice == "ja":
            # Einen Namen aus der Liste ziehen und anzeigen
            if namen_liste:
                name = namen_liste.pop(0)
                print(f"Hier ist dein erstellter Name: {name}")
            else:
                print("Es sind keine Namen mehr übrig.")
        elif choice == "nein":
            print("Ich weiß bescheid")
            break
        else:
            print("Antworte mit Ja oder Nein")

def main():
    # Liste mit Namen erstellen
    namen_liste = generate_random_name_list()
    # Ein Namen anzeigen lassen
    get_random_name(namen_liste)

if __name__ == "__main__":
    main()

