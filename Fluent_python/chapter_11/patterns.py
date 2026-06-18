from vector2d_v3 import Vector2d


def keyword_pattern_demo(v: Vector2d) -> None:
    match v:
        case Vector2d(x=0, y=0):
            print(f"{v!r} is null")
        case Vector2d(x=0):
            print(f"{v!r} is vertical")
        case Vector2d(y=0):
            print(f"{v!r} is horizontal")

        case  Vector2d(x=x, y=y) if (x == y):
            print(f"{v!r} is diagonal")
        case _:
            print(f"{v!r} is awesome") 

def positional_pattern_demo(v: Vector2d) -> None:
    match v:
        case Vector2d(x=0, y=0):
            print(f"{v!r} is null")
        case Vector2d(x=0):
            print(f"{v!r} is vertical")
        case Vector2d(y=0):
            print(f"{v!r} is horizontal")

        case  Vector2d(x=x, y=y) if (x == y):
            print(f"{v!r} is diagonal")
        case _:
            print(f"{v!r} is awesome") 

            
def main():
    vectors = (
        Vector2d(1, 1),
        Vector2d(0, 1),
        Vector2d(1, 0),
        Vector2d(1, 2),
        Vector2d(0, 0),
    )                  

    print('KEYWORD PATTERS:')
    for vector in vectors:
        keyword_pattern_demo(vector)

    print('POSITIONAL PATTERNS:')
    for vector in vectors:
        positional_pattern_demo(vector)

if __name__ == '__main__':
    main()         

               
