# A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at
# both ends in the binary representation of N.
#
# For example, number 9 has binary representation 1001 and contains a binary gap of length 2.
# The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3.
# The number 20 has binary representation 10100 and contains one binary gap of length 1.
# The number 15 has binary representation 1111 and has no binary gaps.
# The number 32 has binary representation 100000 and has no binary gaps.
#
# Write a function:
#
#     def solution(N)
#
# that, given a positive integer N, returns the length of its longest binary gap. The function should return 0
# if N doesn't contain a binary gap.
#
# For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so
# its longest binary gap is of length 5.
# Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [1..2,147,483,647].


def solution(n: int):
    if n < 0:
        raise ValueError("Negative number encountered while non-negative expected.")

    binary_string = f"{n:b}"
    counting = False
    max_gap, index, length = 0, 0, len(binary_string)
    while index < length:
        digit = binary_string[index]
        if counting:
            if digit == "0":
                current_gap += 1
            else:
                if max_gap < current_gap:
                    max_gap = current_gap
                current_gap = 0
        else:
            if digit == "1":
                counting = True
                current_gap = 0
        index += 1
    return max_gap


def main():
    for number in [0, 1, 5, 9, 15, 17, 20, 32, 529, 1041, 2_147_483_647]:
        print(number, f"{number:b}", solution(number))

    try:
        solution(-1)
    except ValueError:
        print("Value error excepted.")


if __name__ == "__main__":
    main()
