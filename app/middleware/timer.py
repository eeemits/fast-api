import time
from fastapi import Request


async def timer_middleware(request: Request, call_next):
    """middleware to measure request processing time"""
    start = time.perf_counter()  # high resolution counter to measure elapse time
    response = await call_next(request)
    # setting a custom header to calculate processing time of request
    response.headers["X-Processing-Time"] = (
        f"{time.perf_counter() - start:.4f}s"  # An f-string (formatted string literal) is a modern and efficient Python string formatting mechanism introduced in Python 3.6. It allows you to embed Python expressions and variables directly within a string literal for clear, concise, and dynamic string creation.
    )
    return response
