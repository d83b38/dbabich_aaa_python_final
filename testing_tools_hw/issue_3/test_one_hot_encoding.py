import unittest
from one_hot_encoder import fit_transform


class TestOneHotEncoder(unittest.TestCase):
    """ test OHE """
    def test_fit_transform(self):
        """ main logic test """
        test_list = ['cold', 'cold', 'warm', 'cold', 'hot']
        actual = fit_transform(test_list)
        expected = [('cold', [0, 0, 1]),
                    ('cold', [0, 0, 1]),
                    ('warm', [0, 1, 0]),
                    ('cold', [0, 0, 1]),
                    ('hot', [1, 0, 0])]
        self.assertEqual(expected, actual)

    def test_not_in(self):
        """ test wrong calcaulation  """
        test_list = ['a', 'b', 'c', 'a', 'b']
        not_expected = ('b', [1, 0, 0])
        actual = fit_transform(test_list)
        self.assertNotIn(not_expected, actual)

    def test_error_empty(self):
        """ check empty throws TypeError """
        with self.assertRaises(TypeError) as ctx:
            fit_transform()
        self.assertIsInstance(ctx.exception, TypeError)

    def test_single_string(self):
        """ test single string """
        test_string = 'single'
        actual = fit_transform(test_string)
        expected = [('single', [1])]
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
