import unittest

from tunein_homework import merge_response


class Test_003(unittest.TestCase):
    def test_skip_fields(self):
        """
        Verify that fields which start with 'skip' text aren't present in the output
        """
        url = "https://api.fns.tunein.com/v1/json”"
        res = merge_response(url)
        are_present = False
        for i in res:
            if i.startswith("skip"):
                are_present = True
        self.assertEqual(are_present, False)
