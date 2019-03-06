import unittest
from unittest import mock
from unittest.mock import MagicMock as Mock
from HW4 import GitZeHub
from unittest.mock import patch
m = Mock()

class TestGitHubMagic(unittest.TestCase):
    @patch('requests.get')
    def JSONTest(self, json):
        json_object = json.loads(json)
        m.json.return_value = json_obj
        json_results_list = []
        results = [Mock(), Mock(), Mock()]
        json_results_list.append(json.loads('[{"name" : "Classify-Triangles"}. {"name": "Hello-World"}, {"name": "HW2a567"}, {"name": "HW4"}]'))
        json_results_list.append(json.loads('[ { "commit" : "1" }, { "commit" : "10" }, { "commit" : "2" }, { "commit" : "29" },  { "commit" : "18" } ]'))
        m.json.side_effect = results

if __name__ == '__main__':
    print('Testing...')
    unittest.main(exit = False)
