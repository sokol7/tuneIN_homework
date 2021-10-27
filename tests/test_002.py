import unittest
from tunein_homework import merge_response


class Test_002(unittest.TestCase):
    def test_returned_object(self):
        """
        Verify that returned object is a dict
        """
        url = "https://api.fns.tunein.com/v1/json”"
        res = merge_response(url)
        self.assertEqual(isinstance(res, dict), True)
