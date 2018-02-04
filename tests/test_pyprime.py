import unittest
from nprime.pyprime import pyprime


class TestPyPrime(unittest.TestCase):
    """ test for pyprime """

    def setUp(self):
        """ Set up of the tests """
        pass

    def test_is_zero_not_prime(self):
        """Is zero correctly determined not to be prime?"""
        self.assertFalse(pyprime(0))

    def test_is_one_not_prime(self):
        """Is four correctly determined not to be prime?"""
        self.assertFalse(pyprime(1), msg='Four is not prime!')

    def test_negative_number_not_prime(self):
        """Is a negative number correctly determined not to be prime?"""
        for index in range(-1, -10, -1):
            self.assertFalse(pyprime(index), msg='{} should not be determined to be prime'.format(index))

    def test_float_return_error_message(self):
        """ An error message is raised for a float """
        self.assertRaises(TypeError, pyprime, 3.8)

    def test_bool_return_error_message(self):
        """ An error message is raised for a bool """
        self.assertRaises(TypeError, pyprime, True)

    def test_string_return_error_message(self):
        """ An error message is raised for a String"""
        self.assertRaises(TypeError, pyprime, "three")

    def tearDown(self):
        """ tear down of the tests """
        pass


if __name__ == '__main__':
    unittest.main()
