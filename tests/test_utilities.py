import unittest
import json
import tempfile
from src.utilities import load_json_file

class TestUtilities(unittest.TestCase):

    def test_valid_json(self):
        jsons = json.dumps({
            'n': 3,
            'flights': [],
            'src': 0,
            'dst': 2,
            'k': 1
        })
        temp = tempfile.NamedTemporaryFile(delete=False, suffix='.json')
        temp.write(jsons.encode('utf-8'))
        temp.close()

        n, flights, src, dst, k = load_json_file(temp.name)

        self.assertEqual(n, 3)
        self.assertEqual(flights, [])
        self.assertEqual(src, 0)
        self.assertEqual(dst, 2)
        self.assertEqual(k, 1)

    def test_missing_key(self):
        temp = tempfile.NamedTemporaryFile(delete=False, suffix='.json')
        temp.write(json.dumps({'n': 3}).encode())
        temp.close()

        with self.assertRaises(KeyError):
            load_json_file(temp.name)
