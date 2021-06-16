import unittest

from Rewards import reward_function


class Test(unittest.TestCase):

    def test_tracks(self):
        """
        Test that numbers between 0 and 5 are all even.
        """
        params = {'track_width': 10, 'distance_from_center': 0}
        for i in range(20):
            params['distance_from_center'] = i/2
            result = reward_function(params)
            print("{} input, {} result.".format(params, result))
            self.assertGreater(result, 0, "it's not greater")


if __name__ == '__main__':
    unittest.main()
