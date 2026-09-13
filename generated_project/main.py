def _parse_number(s: str) -> float:
    s = s.strip()
    try:
        return float(s)
    except ValueError:
        # Basic handling for comma as decimal separator (e.g., "2,5")
        if s.count(',') == 1 and '.' not in s:
            try:
                return float(s.replace(',', '.'))
            except ValueError:
                pass
        raise


def main() -> None:
    try:
        first = input()
        second = input()
    except EOFError:
        # Not enough input provided; exit quietly
        return

    try:
        a = _parse_number(first)
        b = _parse_number(second)
    except ValueError:
        # Invalid input; exit quietly without extra text
        return

    print(a + b)


if __name__ == "__main__":
    main()
