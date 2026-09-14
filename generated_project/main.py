#!/usr/bin/env python3

def _to_float(text: str) -> float:
    if text is None:
        return 0.0
    s = text.strip()
    try:
        return float(s)
    except ValueError:
        # Try replacing comma decimal separator
        try:
            return float(s.replace(",", "."))
        except ValueError:
            return 0.0

def main():
    try:
        a = _to_float(input())
    except EOFError:
        a = 0.0
    try:
        b = _to_float(input())
    except EOFError:
        b = 0.0
    total = a + b
    print(total)

if __name__ == "__main__":
    main()
