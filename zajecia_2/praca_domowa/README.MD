# Praca domowa 2

Na odpowiedzi czekamy do 20.03.2018 23:59:59 czasu polskiego.

## Zadanie

Twój znajomy jest fanatykiem wędkarsktwa. Zlecił Ci przygotowanie portalu na
którym wędkarze mogą dzielić się  swoimi zdobyczami.

Wykonaj endpointy według poniższych wymagań:

1. `/login`  
    * POST  
    Za pomocą mechanizmu BasicAuth pozwala na zalogowanie użytkownika. 
    Poprawne podanie loginu i hasła sprawia, że dany użytkownik będzie miał 
    dostęp do wszystkich pozostałych endpointów w aplikacji.
    Podpowiedź: :cookie:.
    Stwórz następującego użytkownika:
        * login: `Akwarysta69`
        * pass: `J3si07r`.

    Uwaga: Celowo pomijamy rejestrowanie nowego użytkownika.

2. `/logout`  
    * POST  
    Wyloguje aktualnego użytkownika z aplikacji uniemożliwiając mu dostęp do
    żadnego endpointu poza `/` i `/login`.

3. `/hello`  
    * GET  
    Po zalogowaniu użytkownik powinien zostać przekierowany na ten endpoint.
    Template niech zawiera element o `"id=greeting"`. 
    Format powitania: `Hello, {user}!` 

4. `/fishes?format=JSON`
    * GET
    Wylistuje nazwy wszystkich ryb w kolejności alfabetycznej     identyfikatorów.
    Zwracany format: JSON
    ```json
    {
        "id_1": {
            "who": "Znajomy",
            "where": {
                "lat": 0.001,
                "long" 0.002
            },
            "mass": 34.56,
            "length": 23.67,
            "kind": "szczupak"
        },
        "id_2": {
            "who": "Kolega kolegi",
            "where": {
                "lat": 34.001,
                "long" 52.002
            },
            "mass": 300.12,
            "length": 234.56,
            "kind": "sum olimpijczyk"
        }
    }
    ```

    * POST  
    Dodanie nowej rybki.
    Format: JSON
    ```json
    {
        "who": "Znajomy",
        "where": {
            "lat": 0.001,
            "long" 0.002
        },
        "mass": 34.56,
        "length": 23.67,
        "kind": "szczupak"
    }
    ```

5. `/fishes/<id>?format=json`
    * GET
    Zwraca JSON'a danej rybki.
    
    * DELETE
    Usuwa rybkę
    
    * PUT
    Podmienia rybkę
    
    * PATCH
    Modyfikuje według podanych wartości, przykład:
    Przymując rybkę o takich danych początkowych:
    ```json
    {
        "who": "Znajomy",
        "where": {
            "lat": 0.001,
            "long" 0.002
        },
        "mass": 34.56,
        "length": 23.67,
        "kind": "szczupak"
    }
    ```
    Po zawołaniu `PATCHA'a` z takimi danymi:
    ```json
    {
        "who": "Nieznajomy"
    }
    ```
    Wynikowa rybka powinna wyglądać następująco:
    ```json
    {
        "who": "Nieznajomy",
        "where": {
            "lat": 0.001,
            "long" 0.002
        },
        "mass": 34.56,
        "length": 23.67,
        "kind": "szczupak"
    }
    ```

## Komentarz
* Na potrzeby tego zadania wystarczy trzymanie danych w wewnętrznych 
  strukturach danych w pamięci.
* Wystarczy 1 worker na heroku. Na zajęciach 4 będziemy się zajmować 
  aplikacjami wieloworkerowymi.
* Aplikacja będzie sprawdzana pomiędzy 21.03.2018 07:00 UTC a 22.03 18:00 UTC
  i w tym oknie czasowym powinna być dostępna.
* W opisie kilku endpointów zamieściliśmy informację o query stringu: 
  `?format=JSON` - nasz  automat będzie brał pod uwagę content zwrócony tylko 
  w JSON. 