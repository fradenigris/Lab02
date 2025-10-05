def carica_da_file(file_path):
    """Carica i libri dal file"""
    # TODO
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            biblioteca = list()

            file.readline()
            for riga in file:
                campi = riga.rstrip('\n').split(',')
                biblioteca.append({
                'titolo' : campi[0],
                'autore' : campi[1],
                'anno' : int(campi[2]),
                'pagine' : int(campi[3]),
                'sezione' : int(campi[4]),
                })

        return biblioteca

    except FileNotFoundError:
        return None

def aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path):
    """Aggiunge un libro nella biblioteca"""
    # TODO
    with open(file_path, 'r', encoding='utf-8') as file:
        for i, riga in enumerate(file, start = 0):
            if i == 0:
                max_sezioni = int(riga.strip())
            break

    titoli = list()
    for item in biblioteca:
        titoli.append(item['titolo'].lower())

    try:
        if titolo.lower() not in titoli and sezione <= max_sezioni and sezione > 0:
            biblioteca.append({
            'titolo': titolo,
            'autore': autore,
            'anno': anno,
            'pagine': pagine,
            'sezione': sezione
            })

            with open(file_path, 'a', encoding='utf-8', newline = '') as file:
                file.write(f"{titolo},{autore},{anno},{pagine},{sezione}\n")

            print(f"Il libro aggiunto alla biblioteca è '{titolo}', di {autore}!")

            return biblioteca

        else:
            return None

    except FileNotFoundError:
        return None



def cerca_libro(biblioteca, titolo):
    """Cerca un libro nella biblioteca dato il titolo"""
    # TODO

    titoli = list()
    for item in biblioteca:
        titoli.append(item['titolo'].lower())

    if titolo.lower() not in titoli:
        return None
    else:
        for item in biblioteca:
            if item['titolo'].lower() == titolo.lower():
                print(f"{item['titolo']}, {item['autore']}, {item['anno']}, {item['pagine']}, {item['sezione']}")

                return item['titolo']

def elenco_libri_sezione_per_titolo(biblioteca, sezione):
    """Ordina i titoli di una data sezione della biblioteca in ordine alfabetico"""
    # TODO
    titoli = list()

    if (sezione <= 0 or sezione > 5):
        print('Numero di sezione non esistente.')
        return None
    else:
        for item in biblioteca:
            if sezione == item['sezione']:
                titoli.append(item['titolo'])

    titoli.sort()

    return titoli

def main():
    biblioteca = []
    file_path = "biblioteca.csv"

    while True:
        print("\n--- MENU BIBLIOTECA ---")
        print("1. Carica biblioteca da file")
        print("2. Aggiungi un nuovo libro")
        print("3. Cerca un libro per titolo")
        print("4. Ordina titoli di una sezione")
        print("5. Esci")

        scelta = input("Scegli un'opzione >> ").strip()

        if scelta == "1":
            while True:
                file_path = input("Inserisci il path del file da caricare: ").strip()
                biblioteca = carica_da_file(file_path)
                if biblioteca is not None:
                    break

        elif scelta == "2":
            if not biblioteca:
                print("Prima carica la biblioteca da file.")
                continue

            titolo = input("Titolo del libro: ").strip()
            autore = input("Autore: ").strip()
            try:
                anno = int(input("Anno di pubblicazione: ").strip())
                pagine = int(input("Numero di pagine: ").strip())
                sezione = int(input("Sezione: ").strip())
            except ValueError:
                print("Errore: inserire valori numerici validi per anno, pagine e sezione.")
                continue

            libro = aggiungi_libro(biblioteca, titolo, autore, anno, pagine, sezione, file_path)
            if libro:
                print(f"Libro aggiunto con successo!")
            else:
                print("Non è stato possibile aggiungere il libro.")

        elif scelta == "3":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            titolo = input("Inserisci il titolo del libro da cercare: ").strip()
            risultato = cerca_libro(biblioteca, titolo)
            if risultato:
                print(f"Libro trovato: {risultato}")
            else:
                print("Libro non trovato.")

        elif scelta == "4":
            if not biblioteca:
                print("La biblioteca è vuota.")
                continue

            try:
                sezione = int(input("Inserisci numero della sezione da ordinare: ").strip())
            except ValueError:
                print("Errore: inserire un valore numerico valido.")
                continue

            titoli = elenco_libri_sezione_per_titolo(biblioteca, sezione)
            if titoli is not None:
                print(f'\nSezione {sezione} ordinata:')
                print("\n".join([f"- {titolo}" for titolo in titoli]))

        elif scelta == "5":
            print("Uscita dal programma...")
            break
        else:
            print("Opzione non valida. Riprova.")


if __name__ == "__main__":
    main()

