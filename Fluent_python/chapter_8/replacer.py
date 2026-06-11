'''   
zip_replace : replaces multiple calls to `str.replace`

'''
from collections.abc import Iterable

FromTo = tuple[str, str]

def zip_replace(text: str, changes: Iterable[FromTo]) -> str: 
    for from_, to in changes:
        text = text.replace(from_, to)
    return text


def demo() -> None:
    import doctest
    failed, count = doctest.testmod()
    print(f'{count-failed} of {count} doctests OK')
    l33t = [(p[0], p[1]) for p in 'a4 e3 i1 o0'.split()]
    text = 'mad skilled noob powned leet'
    print(zip_replace(text, l33t))

if __name__ == '__main__':
    demo()

    
    changes = [
        ('(', '('),
        (')', ')'),
        (' ', ' '),

    ] 

    expr = '(+ 2 (* 3 7 ))'
    zip_replace(expr, changes)


