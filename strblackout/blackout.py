def blackout(s: str, left: int = 0, right: int = 0, replacement: str = "*") -> str:
    n: int = len(s)

    if left + right >= n:
        return replacement * n

    return "".join([
        s[0:left] if left <= 0 else (left * replacement),
        s[left:(n - right)],
        s[(n - right):n] if right <= 0 else (right * replacement),
    ])
