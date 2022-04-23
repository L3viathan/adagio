from time import monotonic, sleep as _sleep
from collections import deque


class sleep:
    def __init__(self, n):
        self.n = n
        self.start = monotonic()

    def __await__(self):
        while monotonic() - self.start < self.n:
            _sleep(0.1)
            yield


class Group:
    def __init__(self):
        self.jobs = deque()

    def schedule(self, job):
        self.jobs.append(job)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            raise exc_val
        while self.jobs:
            job = self.jobs.popleft()
            try:
                job.send(None)
            except StopIteration:
                pass
            else:
                self.jobs.append(job)


def a_wait(awaitable):
    with Group() as g:
        g.schedule(awaitable)
