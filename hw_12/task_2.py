def stop_words(words: list):
    def decarator(func: callable):
        def wrapper(name: str) -> str:
            result = func(name)
            for word in words:
                result = result.replace(word, '*')
            return result
        return wrapper
    return decarator

@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan("Steve") == "Steve drinks * in his brand new *!"