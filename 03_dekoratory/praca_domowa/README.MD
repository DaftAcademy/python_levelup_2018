# Praca domowa 3


Odpowiedź podaj **wyłącznie** przez: https://goo.gl/forms/0ORFf46sjdDoyPW23 

Na odpowiedzi czekamy do 27.03.2018 23:59:59 czasu polskiego.
 
## Zadanie 1.
Napisz dekorator `@add_tag`, który opakowuje funkcje zwracające tekst, otaczając wynik podanym stringiem zamkniętym w klamry (jak w html), w formie `<TAG>wynik</TAG>`.
Przykład:
```python
@add_tag('h1')
def write_something():
    return 'something'

result = write_something()
assert result == '<h1>something</h1>'
```

## Zadanie 2.
Napisz walidator JSON'ów `@validate_json`. Ma on sprawdzać, czy przekazany json zawiera tylko i wyłącznie wymienione w argumentach dekoratora elementy. W przypadku innej zawartości niech rzuca `ValueError`.

```python
@validate_json('first_name', 'last_name')
def process_json(json_data):
    return len(json_data)

result = process_json('{"first_name": "James", "last_name": "Bond"}')
assert result == 44

process_json('{"first_name": "James", "age": 45}')
> ValueError

process_json('{"first_name": "James", "last_name": "Bond", "age": 45}')
> ValueError
```

## Zadanie 3.
Napisz dekorator `@log_this` który będzie logować wywołania funkcji.
Do dekoratora przekazujemy:
* `logger` na którym będziemy logować.
  Załadamy, że `logger` ma ustawiony poziom na logowania na `DEBUG`
* `level` poziom logowania z jakim będzie wywołany `logger`.
* `format` format w jakim będziemy logować wywołania.

`@log_this` ma drukować w (w odpowiednim formacie) kolejności:
* poziom logowania* nazwę funkcji
* argumenty wywołania
* wynik funkcji


Poniżej przykład

Zakładając taki kod:
```python
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

@log_this(logger, level=logging.INFO, format='%s: %s -> %s')
def my_func(a, b, c=None, d=False):
    return 'Wow!'
```

Po takim wywołaniu:
```
my_func(1, 2, d=True)
```

Zawoła na loggerze:
```
logger.info('%s: %s -> %s', 'my_func', ('1', '2', 'd=True'), 'Wow!')
```

> Do rozwiązania zadania przyda się wiedza stąd: https://docs.python.org/3.6/library/logging.html.
