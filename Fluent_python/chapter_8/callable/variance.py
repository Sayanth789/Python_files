from collections.abc import Callable

def update(
        probe: Callable[[], float],
        display: Callable[[float], None]
) -> None:
    temperature = probe()

    # Can add more code here 
    display(temperature)

def probe_ok() -> int:
    return 42 

def display_wrong(temperature: int) -> None:
    print(hex(temperature))


update(probe_ok, display_wrong) # type error 

def display_ok(temperaure: complex) -> None:
    print(temperaure)

update(probe_ok, display_ok)    
