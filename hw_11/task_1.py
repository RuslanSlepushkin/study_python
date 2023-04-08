def count_local_variable() -> int:
    film = "The Shawshank Redemption"
    year = 1994
    director = "Frank Darabont"
    imdb_rating = 1
    count = len(locals())
    return count


print(count_local_variable())