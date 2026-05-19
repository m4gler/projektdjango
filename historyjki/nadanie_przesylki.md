# Historyjka uzytkownika: nadanie przesylki

## Jako

Klient paczkomatu.

## Chce

Wprowadzic dane nadawcy, odbiorcy, wybrac paczkomat i opcjonalnie kuriera.

## Aby

Nadac przesylke i otrzymac numer sledzenia.

## Kryteria akceptacji

- Formularz zawiera pola: nadawca, odbiorca, telefon odbiorcy, paczkomat, kurier.
- System nie pozwala nadac przesylki do pelnego paczkomatu.
- Po poprawnym zapisie system tworzy przesylke w bazie danych przez Django ORM.
- Po nadaniu uzytkownik widzi komunikat z numerem sledzenia.
- Przesylka z wybranym kurierem otrzymuje status `Przypisana kurierowi`.
- Bledy walidacji sa pokazane przy formularzu.
