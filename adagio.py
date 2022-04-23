from time import monotonic, sleep as _sleep
from collections import deque

jobs = deque()

class sleep:
    def __init__(self, n):
        self.n = n
        self.start = monotonic()

    def __await__(self):
        while monotonic() - self.start < self.n:
            _sleep(0.1)
            yield

def schedule(job):
    jobs.append((str(job), job))

def run(entrypoint, *args, **kwargs):
    schedule(entrypoint(*args, **kwargs))
    while jobs:
        # print("jobs:", jobs)
        job = jobs.popleft()
        try:
            job[1].send(None)
        except StopIteration:
            pass
        else:
            jobs.append(job)


def a_wait(awaitable):
    return run(lambda: awaitable)
