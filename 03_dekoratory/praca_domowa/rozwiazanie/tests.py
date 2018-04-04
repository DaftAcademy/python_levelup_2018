import logging
from unittest.mock import MagicMock

from pytest import raises, mark

from resolution import add_tag, validate_json, log_this


def test_add_tag():
    @add_tag('h1')
    def hello():
        return('hello')
    assert hello() == '<h1>hello</h1>'


@mark.parametrize('required_keys, test_keys, should_throw', [
    [
        ['first_name', 'second_name'],
        '{"first_name": "James", "second_name": "Bond"}',
        False,
    ],
    [
        ['first_name', 'second_name'], '{"first_name": "James"}',
        True,
    ],
    [
        ['first_name', 'second_name'],
        '{"first_name": "James", "second_name": "Bond", "agent_id": "007"}',
        True,
    ],
])
def test_validate_json(required_keys, test_keys, should_throw):
    
    @validate_json(*required_keys)
    def hello(json_input):
        pass

    if should_throw:
        with raises(ValueError):
            hello(test_keys)
    else:
        hello(test_keys)


def test_log_this():

    logger = MagicMock()

    @log_this(logger, level=logging.INFO, fmt='%s: %s -> %s')
    def my_func(a, b, c=None, d=False):
        return 'Wow!'

    my_func(1, 2, d=True)

    logger.log.assert_called()
    logger.log.assert_called_once()
    logger.log.assert_called_with('%s: %s -> %s', 'my_func',
                                  ('1', '2', 'd=True'), 'Wow!')
