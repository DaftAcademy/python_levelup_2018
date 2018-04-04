import logging
from functools import wraps
from itertools import chain
from json import loads
from typing import Callable, Any


def add_tag(tag):
    """Add a specified tag for the function that returns strings"""
    def decorator(func: Callable[[Any], str]):
        @wraps(func)
        def wrapper(*args, **kwargs):
            return f'<{tag}>{func(*args, **kwargs)}</{tag}>'
        return wrapper
    return decorator


def validate_json(*required_keys):
    """Validates first json"""
    def decorator(func: Callable[[Any], Any]):
        @wraps(func)
        def wrapper(input_json, *args, **kwargs):
            input_dict = loads(input_json)
            # if not all(key in input_dict for key in required_keys):
            if input_dict.keys() != set(required_keys):
                raise ValueError
            return func(input_json, *args, **kwargs)
        return wrapper
    return decorator


def log_this(logger: logging.Logger, level, fmt):
    """Logs execution"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            rv = func(*args, **kwargs)
            logger.log(fmt, func.__name__,
                       tuple(chain((str(a) for a in args),
                                   (f'{k}={v}' for k, v in kwargs.items()))),
                       str(rv))
            return rv
        return wrapper
    return decorator