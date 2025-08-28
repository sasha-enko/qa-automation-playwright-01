# src/elements/retry.py
import time
from functools import wraps



def retry_on_exception(default_retries: int = 1, delay: float = 0.5):
    """Decorator to retry a method if it raises an exception."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, retries=None, **kwargs):
            retries_ = retries if retries is not None else default_retries

            attempt = 0
            while attempt <= retries_:
                try:
                    print(
                        f"\n[DEV LOG]\t\
                        Attempt {attempt + 1} of {retries_ + 1} in total"
                    )

                    return func(*args, **kwargs)

                except Exception as e:
                    attempt += 1
                    if attempt > retries_:
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


# Initially the code was in and came from the base_page.py
#
# def refresh(self, wait_until: Literal["load", "domcontentloaded", "networkidle"] = "load", retries: int = None):
#     attempt = 0
#     while attempt <= retries:
#         try:
#             self.page.reload(wait_until=wait_until)
#             if self.unique_page_definer:
#                 self.page.wait_for_selector(self.unique_page_definer)
#             return
#         except Exception as e:
#             attempt += 1
#             if attempt > retries:
#                 raise RuntimeError(
#                     f"\n[DEV LOG]\t\
#                     Page {self.__class__.__name__} refresh failed after {retries} retries with exception: \n{e}"
#                 ) from e  # this line show that the original cause of the RuntimeError is the TimeoutError
#             print(
#                 f"\n[DEV LOG]\t\
#                 Warning: refresh attempt {attempt} of th page {self.__class__.__name__} is failed, retrying..."
#             )
