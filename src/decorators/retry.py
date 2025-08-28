# src/elements/retry.py
import time
from functools import wraps



def retry_on_exception(retries: int = 1, delay: float = 0.5):
    """Decorator to retry a method if it raises an exception."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):

            attempt = 0
            while attempt <= retries:
                try:

                    return func(*args, **kwargs)

                except Exception as e:
                    attempt += 1
                    if attempt > retries:
                        print(
                            f"\n[DEV LOG]\t\
                            Original exception {type(e)} is:\n{e}"
                        )
                        raise
                    print(
                        f"\n[DEV LOG]\t\
                        Warning: attempt {attempt} failed, retrying..."
                    )
                    time.sleep(delay)

        return wrapper
    return decorator
