from __future__ import annotations

def find_non_injective_pair(mapping: dict) -> tuple | None:
    """Return (x1, x2) where f(x1)==f(x2), or None."""
    seen = {}

    for key, value in mapping.items():
        if value in seen:
            return (seen[value], key)
        seen[value] = key

    return None


def find_non_surjective_element(mapping: dict, target: set):
    """Return one target element not in range, or None."""
    outputs = set(mapping.values())

    for element in target:
        if element not in outputs:
            return element

    return None


def my_floor(x: float) -> int:
    """Return floor(x) without math.floor."""
    return int(x)


def my_ceil(x: float) -> int:
    """Return ceil(x) without math.ceil."""
    truncated = int(x)

    if x == truncated:
        return truncated
    if x > 0:
        return truncated + 1
    return truncated