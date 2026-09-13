#!/usr/bin/env python3

def main() -> None:
    print("Hello from FORGE")

if __name__ == "__main__":
    try:
        main()
    except Exception:
        import sys
        sys.exit(1)
