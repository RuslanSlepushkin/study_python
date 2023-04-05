def make_country(name, capital):
    dict_make_country = dict()
    dict_make_country[name] = capital
    print(dict_make_country)


name_inpt = input("Write the name country: ")
capital_inpt = input("Write the capital: ")
make_country(name_inpt, capital_inpt)