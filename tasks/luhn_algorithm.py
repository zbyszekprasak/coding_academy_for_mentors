# Card number validity can be checked using Luhn algorithm.
# https://en.wikipedia.org/wiki/Luhn_algorithm
#
# Your task is to implement this algorithm.
#
# Write function to validate credit card numbers:
#   def solution(card_number):
#
# Variable card_number will be provided as string (no spaces inside).
# Function should return True for valid card number, and False for invalid.
#
# Sample data:
# Valid card numbers
# 4111111111111111
# 5500000000000004
#
# Invalid card numbers
# 4198786787558765
# 9875787643456354


def solution(card_number):
    card_digits = [int(digit) for digit in card_number]
    for i in range(-2, -len(card_digits) - 1, -2):
        card_digits[i] = card_digits[i] * 2 % 9
    return sum(card_digits) % 10 == 0


def main():
    for card_number in ["4111111111111111",
                        "5500000000000004",
                        "4198786787558765",
                        "9875787643456354"]:
        print(f"Card number {card_number} is {'valid' if solution(card_number) else 'invalid'}")


if __name__ == "__main__":
    main()
