# src/elements/waits.py
from functools import wraps


def with_timeout(func):
    @wraps(func)
    def wrapper(self, *args, timeout: int | None = None, **kwargs):
        t = self._effective_timeout(timeout)
        return func(self, *args, timeout=t, **kwargs)
    return wrapper
