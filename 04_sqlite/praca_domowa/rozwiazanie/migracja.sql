BEGIN TRANSACTION;

ALTER TABLE film ADD COLUMN category_id SMALLINT REFERENCES category(category_id);

UPDATE film SET category_id = (
    SELECT category_id
    FROM film_category
    WHERE film_category.film_id = film.film_id
);

DROP TABLE film_category;

COMMIT;
