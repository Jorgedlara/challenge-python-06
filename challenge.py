def make_division_by(n):
    """This closure returns a function that returns the division
       of an x number by n 
    """
    def repeater (num):
        res = num / n
        return res 
    return repeater


def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))  # The expected output is 6

    division_by_5 = make_division_by(5)
    print(division_by_5(100))  # The expected output is 20

    division_by_18 = make_division_by(18)
    print(division_by_18(54))  # The expected output is 3

    unittest.main()


if __name__ == '__main__':
    import unittest

    class ClosureSuite(unittest.TestCase):

        def setUp (self):
            self.value_LCM = 90

        def test_closure_make_division_by(self):
            division_by_3 = make_division_by(3)
            self.assertEqual(30, division_by_3(self.value_LCM))
            
            division_by_5 = make_division_by(5)
            self.assertEqual(18, division_by_5(self.value_LCM))


            division_by_18 = make_division_by(18)
            self.assertEqual(5, division_by_18(self.value_LCM))

        def tearDown(self):
            del(self.value_LCM)

    
    run()

