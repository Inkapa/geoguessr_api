
def test(a: int, b = False, **kwargs):
    print(kwargs)


test(1, cheese=True)
