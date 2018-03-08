# Praca domowa 1

Głównym celem pierwszej pracy domowej jest opublikowanie w Internecie naszej aplikacji napisanej w Pythonie. Pozwoli to nam w dalszych etapach kursu na skupienie się na innych zagadnieniach związanych z web developmentem w Pythonie.

Podczas wykładu przekazaliśmy wskazówki jak zrobić deploy aplikacji na **Heroku.com**. Ten sposób uznamy więc za preferowany. Nic jednak nie stoi na przeszkodzie abyście wrzucili swoją aplikację gdzie indziej, np.: AWS, Google Cloud, własny hosting etc. Ocenimy tylko te prace które będą dostępne publicznie.
 
Poniższe wymagania opisują jakie ścieżki (ang. _paths_) powinna obsługiwać Twoja aplikacja.

Przykładowa aplikacja dostępna jest tutaj: https://homework-01.herokuapp.com

Odpowiedź podaj **wyłącznie** przez: https://goo.gl/forms/bmidcmQNUEIzrujA3


## Wymagania:

1. Stwórz ścieżkę `/` która zwracać będzie "Hello, World!". Tak po prostu :)

2. Stwórz ścieżkę `/now` która będzie zwracać dzisiejszą datę i godzinę:
    * Ważne jest prawidłowe sformatowanie wartości zwracanej przez funkcję endpointu.
    * Użyj formatu identycznego do tego: `2018-03-07 15:37:58.610113`. Godzinę podaj w UTC.

3. Stwórz ścieżkę `/user-agent` która zwróci informacje o user agencie użytkownika.
    * Wykorzystaj informacje o requeście podawane przez `flask`.
    * Format wymagany: `{device-type} / {os} / {browser}`, 
      np: `PC / Linux / Chrome 64.0.3282`
    * _Nie wymyślaj koła od nowa_ ;-)

4. Stwórz ścieżkę `/counter` która zliczać będzię odwiedziny tej ścieżki.
    * W tym zadaniu ważne jest aby znaleźć miejsce w którym będzie można zapisać ilość odwiedzin od ostatniego uruchomienia aplikacji na serwerze
    * na tym etapie kursu nie bawimy się w bazy danych
    * być może spostrzeżesz bardzo ciekawe zachowanie ;-)
