"""Головний модуль програми."""

from python_lab.lib import multiply_numbers


def main():
    """Головна точка входу в програму."""
    result = multiply_numbers(4.0, 5.5)
    print(f"Результат множення: {result}")


if __name__ == "__main__":
    main()