"""Utilities to test whether an integer is a palindrome number."""

def is_palindrome_number(value: int) -> bool:
    """Return True if ``value`` reads the same forwards and backwards.

    The implementation avoids converting the number to a string, which keeps
    space usage to O(1) while running in O(log10(n)) time with respect to the
    number's magnitude.
    """
    if value < 0 or (value % 10 == 0 and value != 0):
        return False

    reversed_half = 0
    while value > reversed_half:
        reversed_half = reversed_half * 10 + value % 10
        value //= 10

    return value == reversed_half or value == reversed_half // 10


if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        raise SystemExit(f"Usage: {sys.argv[0]} <integer>")

    try:
        number = int(sys.argv[1])
    except ValueError as exc:
        raise SystemExit("The provided argument must be an integer.") from exc

    print(is_palindrome_number(number))
