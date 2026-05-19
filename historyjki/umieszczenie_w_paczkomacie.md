# Historyjka uzytkownika: umieszczenie przesylki w paczkomacie

## Jako

Pracownik obslugujacy przesylki.

## Chce

Oznaczyc przesylke jako umieszczona w paczkomacie.

## Aby

Odbiorca mogl odebrac przesylke z wybranego punktu.

## Kryteria akceptacji

- Lista przesylek pokazuje numer sledzenia, odbiorce, paczkomat, kuriera i status.
- Przy przesylce, ktora nie jest jeszcze w paczkomacie, dostepna jest akcja `Umiesc`.
- System sprawdza dostepnosc wolnej skrytki przed zmiana statusu.
- Po powodzeniu status przesylki zmienia sie na `W paczkomacie`.
- Jezeli brakuje wolnej skrytki, system pokazuje komunikat bledu i nie zapisuje zmiany.
