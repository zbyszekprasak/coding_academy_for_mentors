# Write a function:
#
#     def solution(A, B)
#
# that, given two non-negative integers A and B, returns the number of bits set to 1 in the binary representation
# of the number A * B.
#
# For example, given A = 3 and B = 7 the function should return 3, because the binary representation of
# A * B = 3 * 7 = 21 is 10101 and it contains three bits set to 1.
#
# Assume that:
# A and B are integers within the range [0..100,000,000].
# In your solution, focus on correctness. The performance of your solution will not be the focus of the assessment.


def solution(a, b):
    if a < 0:
        raise ValueError("Parameter 'a' is negative but only non-negative is expected.")
    elif b < 0:
        raise ValueError("Parameter 'b' is negative but only non-negative is expected.")

    return f"{a * b:b}".count("1")


def main():
    for a, b in [(3, 7), (0, 3), (1_234, 5_678), (1, 100_000_000)]:
        print(f"{a} * {b} = {a * b} contains {solution(a, b)} one bits.")

    try:
        solution(-1, 3)
    except ValueError:
        print("Value error excepted.")


if __name__ == "__main__":
    main()
