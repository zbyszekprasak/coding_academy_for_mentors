# Write a function:
#
#     def solution(A)
#
# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
#
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
#
# Given A = [1, 2, 3], the function should return 4.
#
# Given A = [−1, −3], the function should return 1.
#
# Write an efficient algorithm for the following assumptions:
#
#         N is an integer within the range [1..100,000];
#         each element of array A is an integer within the range [−1,000,000..1,000,000].
#


def solution(a):
    a = sorted(a)
    i = 1
    for e in a:
        if e < 1:
            continue
        elif e == i:
            i += 1
        elif e > i:
            break
    return i


def main():
    for a in [[1, 3, 6, 4, 1, 2],
              [1, 2, 3],
              [-1, -3]]:
        print(f"Array {a} does not contain {solution(a)}")


if __name__ == "__main__":
    main()
