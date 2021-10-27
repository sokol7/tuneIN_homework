import unittest
from tunein_homework import merge_response


class Test_001(unittest.TestCase):
    def test_endpoint(self):
        """
        Verify that app return False if the status code of the response not equal 200
        """
        url = "https://api.fns.tunein.com/v312321/json”"
        res = merge_response(url)
        self.assertEqual(res, False)