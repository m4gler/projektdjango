# Factory Method

## Wybrany wzorzec

Wzorzec kreacyjny Factory Method.

## Uzasadnienie wyboru wzorca

Podczas nadawania przesylki aplikacja musi utworzyc poprawny obiekt `Parcel`: nadac mu unikalny numer sledzenia, przepisac dane z formularza oraz ustawic odpowiedni status poczatkowy. Te reguly nie powinny byc powielane w widokach.

## Problem projektowy

Widok formularza powinien odpowiadac za obsluge zadania HTTP, a nie za szczegoly tworzenia encji domenowej. Bez fabryki logika generowania numeru sledzenia i wyboru statusu bylaby rozproszona, co utrudniloby zmiane formatu numerow lub dodanie kolejnych typow przesylek.

## Sposob wykorzystania w aplikacji

Klasa `ParcelFactory` w pliku `paczkomaty/services.py` tworzy obiekt `Parcel` na podstawie `ParcelDraft`. Metoda `create()` generuje numer sledzenia i ustawia status `created` albo `assigned`, jezeli wybrano kuriera. Fabryka jest uzywana przez `ParcelManagementFacade.send_parcel()`, czyli w dzialajacym przeplywie nadawania przesylki.

## Pliki

- Implementacja: `paczkomaty/services.py`
- Diagram klas: `wzorce/kreacyjny-factory-method/diagram.svg`
