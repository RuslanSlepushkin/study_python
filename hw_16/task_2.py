from typing import List


class Boss:
    def __init__(self, id_: int, name: str, company: str) -> None:
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []


    def _add_workers(self, worker: object) -> None:
        if not isinstance(worker, Worker):
            raise TypeError("worker must be an instance of the Worker class")
        self._workers.append(worker)


    @property
    def workers(self) -> List:
        return self._workers


    @workers.setter
    def workers(self, workers: List) -> None:
        raise AttributeError("Unable to install workers through a class Boss")


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss) -> None:
        self.id = id_
        self.name = name
        self.company = company
        self._boss = None
        self.boss = boss


    @property
    def boss(self) -> Boss:
            return self._boss


    @boss.setter
    def boss(self, boss: Boss) -> None:
        if not isinstance(boss, Boss):
            raise TypeError("boss must be an instance of the Boss class")
        self._boss = boss
        self._boss._add_workers(self)


bill = Boss(1, "Bill Gates", "Microsoft")
jeffrey = Boss(1, "Jeffrey Bezos", "Amazon")

worker_1, worker_2 = (Worker(1, "Bill", "Microsoft", bill), Worker(2, "Frank", "Microsoft", bill))
worker_3, worker_4 = (Worker(1, "John", "Amazon", jeffrey), Worker(2, "Peter", "Amazon", jeffrey))

for worker in bill.workers:
    print(f"{worker.name} with id №{worker.id} work at {worker.company} for the {bill.name}.")

for worker in jeffrey.workers:
    print(f"{worker.name} with id №{worker.id} work at {worker.company} for the {jeffrey.name}.")