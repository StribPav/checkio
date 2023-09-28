from typing import Iterable

def frequency_sort(items: list[str | int]) -> Iterable[str | int]:
    return sorted(items, key=lambda x: (-items.count(x), items.index(x)))
