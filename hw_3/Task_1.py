sample_str = input("Write the word: ")
if len(sample_str) >= 2:
    new_item = sample_str[:2] + sample_str[-2:]
    print(new_item)
else:
    print('')