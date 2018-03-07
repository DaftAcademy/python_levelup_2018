# Przygotowanie do pierwszych zajęć
W trakcie pierwszych zajęć będziemy tworzyć aplikację webową przy użyciu frameworku `Flask`, a następnie będziemy ją wrzucać na serwer `Heroku` przy użyciu systemu kontroli wersji `Git`.
Zachęcamy do przygotowania środowiska pracy jeszcze przed pierwszymi zajęciami zgodnie z poniższą instrukcją:

## 1. Stworzenie środowiska wirtualnego
Środowisko wirtuale tworzymy za pomocą komendy `python3 -m venv`, a następnie podajemy ścieżkę pod którą ma on zostać utworzony.
```
python3 -m venv /path/to/new/virtual/environment
```

Więcej o środowiskach wirtualnych: https://docs.python.org/3.6/library/venv.html

## 2. Instalacja Flaska w stworzonym środowisku wirtualnym
Przed instalacją zewnętrznych zależności należy aktywować virtualenv:

Windows:
```
\path\to\new\virtual\environment\Scripts\activate.bat
```

Linux:
```
source /path/to/new/virtual/environment/bin/activate
```

Następnie instalujemy Flaska za pomocą komendy
```
pip install Flask
```
Więcej o instalowaniu dodatkowych bibliotek w Pythonie: https://docs.python.org/3.6/installing/index.html

## 3. Instalacja gita
Przy instalacji Gita można skorzystać z bardzo dobrej instrukcji znajdującej się w tutorialu Django Girls: https://tutorial.djangogirls.org/en/deploy/#installing-git .
Więcej o gicie: https://git-scm.com/

## 4. Założenie konta na heroku
Załóż konto na https://signup.heroku.com/ . Jest to serwis ułatwiający wrzucanie aplikacji webowych na serwer.

## 5. Instalacja Heroku CLI
Zainstaluj narzędzie Heroku CLI zgodnie z instrukcją pod następującym linkiem: https://devcenter.heroku.com/articles/heroku-cli .
