from unittest import TestCase, main
from tasks import count_bits, binary_gap, cyclic_rotation, missing_integer, luhn_algorithm


class Test(TestCase):
    def test_count_bits(self):
        self.assertEqual(3, count_bits.solution(3, 7))
        self.assertEqual(8, count_bits.solution(123, 456))
        self.assertEqual(1, count_bits.solution(1024, 8))
        self.assertEqual(8, count_bits.solution(999, 888))
        self.assertEqual(18, count_bits.solution(99999, 88888))
        self.assertEqual(0, count_bits.solution(0, 1))

    def test_binary_gap(self):
        self.assertEqual(5, binary_gap.solution(1041))
        self.assertEqual(0, binary_gap.solution(32))
        self.assertEqual(0, binary_gap.solution(1024))
        self.assertEqual(9, binary_gap.solution(1025))
        self.assertEqual(4, binary_gap.solution(999999))

    def test_cyclic_rotation(self):
        self.assertListEqual([9, 7, 6, 3, 8], cyclic_rotation.solution([3, 8, 9, 7, 6], 3))
        self.assertListEqual([0, 0, 0], cyclic_rotation.solution([0, 0, 0], 1))
        self.assertListEqual([6, 7, 8, 9, 1, 2, 3, 4, 5], cyclic_rotation.solution([1, 2, 3, 4, 5, 6, 7, 8, 9], 4))

    def test_missing_integer(self):
        self.assertEqual(4, missing_integer.solution([1, 2, 3]))
        self.assertEqual(1, missing_integer.solution([-1, -3]))

    def test_luhn_algorithm(self):
        self.assertEqual(True, luhn_algorithm.solution('4111111111111111'))
        self.assertEqual(True, luhn_algorithm.solution('5500000000000004'))
        self.assertEqual(False, luhn_algorithm.solution('4198786787558765'))
        self.assertEqual(False, luhn_algorithm.solution('9875787643456354'))


if __name__ == '__main__':
    main()
