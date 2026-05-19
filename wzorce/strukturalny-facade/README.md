# Facade

## Wybrany wzorzec

Wzorzec strukturalny Facade.

## Uzasadnienie wyboru wzorca

Widoki potrzebuja kilku operacji na danych: pobrania statystyk, listy przesylek, listy paczkomatow, nadania przesylki i umieszczenia jej w paczkomacie. Bez fasady widoki musialyby znac szczegoly zapytan ORM, transakcji, walidacji i obslugi bledow.

## Problem projektowy

Interfejs HTTP powinien pozostac prosty. Zmiany w sposobie zapisu przesylek, sprawdzania skrytek lub generowania numerow nie powinny wymuszac przebudowy kazdego widoku. Fasada daje jeden punkt wejscia do operacji aplikacyjnych.

## Sposob wykorzystania w aplikacji

Klasa `ParcelManagementFacade` w pliku `paczkomaty/services.py` udostepnia metody `dashboard()`, `list_parcels()`, `list_lockers()`, `send_parcel()` oraz `put_in_locker()`. Widoki w `paczkomaty/views.py` wywoluja fasade zamiast bezposrednio wykonywac cala logike ORM i walidacji.

## Pliki

- Implementacja: `paczkomaty/services.py`
- Diagram klas: `wzorce/strukturalny-facade/diagram.svg`
