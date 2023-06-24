from threading import Thread


class Counter(Thread):
    COUNTER = 0
    ROUNDS = 100_000

    def run(self) -> None:
        for _ in range(self.ROUNDS):
            Counter.COUNTER += 1


counter_1 = Counter()
counter_2 = Counter()

counter_1.start()
counter_1.join()

print(Counter.COUNTER)

counter_2.start()
counter_2.join()

print(Counter.COUNTER)


# print(f"Counter result: {result}")
