stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
total = dict()
sum_total = 0
for key_1, value_1 in stock.items():
    total[key_1] = value_1 * prices[key_1]
    sum_total += total[key_1]
print(total)
print(sum_total)