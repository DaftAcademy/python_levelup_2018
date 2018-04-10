# Praca domowa nr 5

Na rozwiązania czekamy do wtorku 10.04.2018 23:59:59 CEST.

Rozwiązania prosimy przesyłać tylko za pośrednictwem formularza: https://goo.gl/forms/8ik0T9z3FeI8exzI2 

Prosimy o zadawanie pytań poprzez issue na GitHubie.

## Zadania

1.  Rozwiązać podpunkty: 1, 2, 4, 5 pracy domowej z poprzednich zajęć wykorzystując bazę PostgreSQL na Heroku oraz SQLAlchemy.
    Interesuje nas tylko endpoint `/cities` i powiązanie z krajami.
    Pozostałe tabele możecie pomminąć w waszej bazie (Heroku nakłada limit na liczbę wierszy w darmowej bazie). Wasza baza powinna zawierać wszystkie maista i kraje wraz z powiązaniami między nimi, które są obecne w bazie sakila używanej na zajęciach.
    Aplikacja powinna działać z wieloma workerami.
    Ta aplikacja nie powinna zaburzać rozwiązania poprzedniego zadania (najlepiej stwórzcie osobną aplikację)

2.  Rozwiązać zadanie ze ścieżką `/couter` z zajęć nr 1 wykorzystując Heroku PostgreSQL, SQLAlchemy i synchronizację na bazie.
    
    Dokumentacja dla zapytania `SELECT FOR UPDATE`: 
    * https://www.postgresql.org/docs/current/static/sql-select.html (sekcja: *The Locking Clause*)
    * http://docs.sqlalchemy.org/en/latest/orm/query.html#sqlalchemy.orm.query.Query.with_for_update
