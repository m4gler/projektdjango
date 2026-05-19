# Projekt 2026-05-18
##### Grupa: do uzupelnienia, klasa: do uzupelnienia
### Paczkomaty - aplikacja do zarzadzania przesylkami
* Imie i nazwisko: do uzupelnienia
* Imie i nazwisko: do uzupelnienia

## Opis

Aplikacja Django do zarzadzania paczkomatami. Umozliwia:

- przegladanie paczkomatow, kurierow i przesylek,
- wyszukiwanie i filtrowanie przesylek,
- nadawanie przesylek,
- przypisywanie przesylek kurierom,
- umieszczanie przesylek w paczkomatach z kontrola wolnych skrytek.

## Etapy projektu

- Z0: utworzono strukture projektu oraz README.
- Z1: historyjki uzytkownika sa w katalogu `historyjki/`.
- Z2: wzorce projektowe opisano w katalogu `wzorce/`.
- Z3: aplikacja ma minimum 3 ekrany: pulpit, lista przesylek, nadanie przesylki, paczkomaty.
- Z4: widoki HTML znajduja sie w `paczkomaty/templates/paczkomaty/`.
- Z5: odczyt i zapis danych odbywa sie przez Django ORM, a bledy sa obslugiwane w formularzach i warstwie serwisowej.

## Uruchomienie

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed
python manage.py runserver
```

Po starcie aplikacja bedzie dostepna pod adresem `http://127.0.0.1:8000/`.

## Wzorce projektowe

- Kreacyjny: Factory Method, opis w `wzorce/kreacyjny-factory-method/README.md`.
- Strukturalny: Facade, opis w `wzorce/strukturalny-facade/README.md`.
