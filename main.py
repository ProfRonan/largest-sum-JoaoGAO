"""Module with functions."""


def largest_sum(numbers: list[int]) -> tuple[int, int]:
    """Encontra e retorna os dois números que somados dão o maior valor."""
    primeiro = 0  # o primeiro número da soma
    segundo = 0  # o segundo número da soma
    if len(numbers) < 2:
        return None
    
    numbers = sorted(numbers)
    primeiro= numbers[-2]
    segundo= numbers[-1]
    return primeiro, segundo
