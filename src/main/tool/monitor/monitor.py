import functools
import logging
import time
import traceback

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def monitor_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            logging.info(
                f"Function/Method: {func.__name__} executed successfully in {end_time - start_time:.4f}s with result: {result}")
            return result
        except Exception as e:
            logging.error(f"Function/Method: {func.__name__} failed. Error: {e}\nTraceback: {traceback.format_exc()}")
            raise

    return wrapper
