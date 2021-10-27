import unittest
import requests
import json
from tunein_homework import merge_response


class Test_004(unittest.TestCase):
    def test_returned_object(self):
        """
        Verify that lower priority overwrites higher priority
        """
        url = "https://api.fns.tunein.com/v1/json”"

        # Get response content
        r = requests.get(url)
        content = json.loads(r.text)

        # Find the values with the lowest priority which doesn't start with "skip"
        vals_with_lower_priority = {}
        priorities = []
        for i in content['ranked']:
            priorities.append(i['priority'])
        lowest_priority = sorted(priorities)[0]

        for i in content['ranked']:
            if i['priority'] == lowest_priority:
                vals_with_lower_priority = i['vals']
        for i in vals_with_lower_priority:
            if i.startswith("skip"):
                del vals_with_lower_priority[i]

        # Receive merged values
        res = merge_response(url)

        # Check whether values with lowest priority matched
        values_matched = True
        for i in vals_with_lower_priority:
            if vals_with_lower_priority[i] != res[i]:
                values_matched = False

        self.assertEqual(values_matched, True)
