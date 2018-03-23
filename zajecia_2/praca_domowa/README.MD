# Praca domowa 2

Odpowiedź podaj **wyłącznie** przez: https://goo.gl/forms/l51AAbUGAlDVMJAc2

Na odpowiedzi czekamy do 27.03.2018 23:59:59 czasu polskiego.

## Zadanie

Twój znajomy jest fanatykiem wędkarsktwa. Zlecił Ci przygotowanie portalu na
którym wędkarze mogą dzielić się  swoimi zdobyczami.

Wykonaj endpointy według poniższych wymagań:

### `/`
* **GET**
  Zwracamy dowolną treść. Ważne aby serwer odpowiadał na tej ścieżce.

### `/login` 
* **POST** 
  > Jeżeli macie ochotę, możecie dodać obsługę  metody **GET** ułatwi Wam to testowanie aplikacji z poziomu przeglądarki. Sprawdzarka nie weźmie jej pod uwagę.

  Za pomocą mechanizmu BasicAuth pozwala na zalogowanie użytkownika. Poprawne podanie loginu i hasła sprawia, że dany użytkownik będzie miał dostęp do wszystkich pozostałych endpointów w aplikacji. Podpowiedź: :cookie: (a jeszcze lepiej mechanizm `flask.session` - swoją  drogą oparty na :cookie:)
  Stwórz następującego użytkownika:
  * login: `Akwarysta69`
  * pass: `J3si07r`.

  Uwaga: Celowo pomijamy rejestrowanie nowego użytkownika

  Jeżeli użytkownik jest już zalogowany, przekieruj na `/hello`.


### `/logout` 
  Do tego endpointu mają dostęp tylko zalogowani użytkownicy. Jeżeli użytkownik nie jest zalogowany, przekieruj na `/login`.
  
* **POST** 
  Wyloguje aktualnego użytkownika z aplikacji uniemożliwiając mu dostęp do żadnego endpointu poza `/` i `/login`.

  > Jeżeli macie ochotę, możecie dodać obsługę  metody **GET** ułatwi Wam to testowanie aplikacji z poziomu przeglądarki. Sprawdzarka nie weźmie jej pod uwagę.
  
  > *Pamiętaj, aby po wylogowaniu **nie** przekierowywać na `/login`, zamiast tego przekieruj na `/`.*


### `/hello` 
  Do tego endpointu mają dostęp tylko zalogowani użytkownicy. Jeżeli użytkownik nie jest zalogowany, przekieruj na `/login`.
  
* **GET**
  Po zalogowaniu użytkownik powinien zostać przekierowany na ten endpoint.
  Template niech zawiera element o `"id=greeting"`.
  Format powitania: `Hello, {user}!`

### `/fishes`
  Do tego endpointu mają dostęp tylko zalogowani użytkownicy. Jeżeli użytkownik nie jest zalogowany, przekieruj na `/login`.
  
* **GET**
  Wylistuje dane wszystkich ryb z ich identyfikatorami. Identyfikatory oczywiście takie jakie im przypisaliście podczas ich tworzenia w metodzie **POST**.
  > **Testować będziemy z *query string* (*qs*): `?format=json`. Oczekujemy w odpowiedzi danych w postaci JSON**.

  > Jeżeli macie ochotę, możecie zwrócić ładniej sformatowy template w przypadku braku *qs*.
      
  ```json
  {
      "id_1": {
          "who": "Znajomy",
          "where": {
              "lat": 0.001,
              "long": 0.002
          },
          "mass": 34.56,
          "length": 23.67,
          "kind": "szczupak"
      },
      "id_2": {
          "who": "Kolega kolegi",
          "where": {
              "lat": 34.001,
              "long": 52.002
          },
          "mass": 300.12,
          "length": 234.56,
          "kind": "sum olimpijczyk"
      }
  }
  ```
       
* **POST** 
  Doda nową rybkę.
  Format: JSON
  > Pomyślne dodanie nowej rybki zakończone powinno być przekierowaniem użytkownika na ładniej sformatowany template na której będzie mógł obejrzeć swoją zdobycz: `GET /fishes/<id>?format=json`. 

  ```json
  {
      "who": "Znajomy",
      "where": {
          "lat": 0.001,
          "long": 0.002
      },
      "mass": 34.56,
      "length": 23.67,
      "kind": "szczupak"
  }
  ```

### `/fishes/<id>`
  Do tego endpointu mają dostęp tylko zalogowani użytkownicy. Jeżeli użytkownik nie jest zalogowany, przekieruj na `/login`.
  
* **GET**
  Zwraca info danej rybki.
  > **Testować będziemy z *query string* (*qs*): `?format=json`. Oczekujemy w odpowiedzi danych w postaci JSON**.
  
  > Jeżeli macie ochotę, możecie zwrócić ładniej sformatowy template w przypadku braku *qs*.

* **DELETE**
  Usuwa rybkę

* **PUT**
  Podmienia rybkę.

* **PATCH**
  Modyfikuje według podanych wartości, przykład:
  Przymując rybkę o takich danych początkowych:
  ```json
  {
      "who": "Znajomy",
      "where": {
          "lat": 0.001,
          "long": 0.002
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
          "long": 0.002
      },
      "mass": 34.56,
      "length": 23.67,
      "kind": "szczupak"
  }
  ```
  > Zakładamy, że chcemy podmienić wartości kluczy najwyższego poziomu, czyli bazując na powyższym przypadku klucze: `"who", "where", "mass", "length", "kind"`. Jeżeli chcemy zmienić wartość `"lat"`, podobiektu `"where"` podajmy cały podobiekt `"where"`.
   

## Komentarz
* Na potrzeby tego zadania wystarczy trzymanie danych w wewnętrznych strukturach danych w pamięci.
* Wystarczy 1 worker na heroku. Na zajęciach 4 będziemy się zajmować aplikacjami wieloworkerowymi. 
  Dla przypomnienia, poniżej podajemy sposób w jaki można skonfigurować  `gunicorn'a` na heroku w trybie jednoworkerowym.
  ```shell
  heroku config:set WEB_CONCURRENCY=1
  ```

* Aplikacja będzie sprawdzana pomiędzy 28.03.2018 07:00 UTC a 30.03 18:00 UTC i w tym oknie czasowym powinna być dostępna.
* W opisie kilku endpointów zamieściliśmy informację o query stringu który będziemy dołączać do zapytań: `?format=json` - nasz automat będzie brał pod uwagę content zwrócony tylko w JSON.
* Więcej info tutaj: [Zadanie domowe 2 - pytania](https://github.com/daftcode/python_levelup_2018/issues/2)
