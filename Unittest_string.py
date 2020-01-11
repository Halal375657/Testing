import unittest
from collections import defaultdict

def FilterDuplicates(str_var):
    # Return only duplicate characters.
    d = defaultdict(int)
    for ch in str_var:
        d[ch] += 1

    res_str = ''
    for ch in d:
        if d[ch] != 1:
            res_str += ch

    return res_str

def Rotate(s, k):
    # Return rotated string.
    n = len(s)
    rotated_str = ''
    for i in range(n-k, n):
        rotated_str += s[i]

    for i in range(n-k):
        rotated_str += s[i]

    return rotated_str

class TestStringMethods(unittest.TestCase):

    def test_upper(self):

        self.assertEqual('foo'.upper(), 'FOO')
        self.assertEqual('FoO'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('fOo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])

        with self.assertRaises(TypeError):
            s.split(2)

    def test_FilterDuplicates(self):
        s = 'teststringmethods'
        self.assertEqual(FilterDuplicates(s), "tes")

    def test_Rotate(self):
        s = 'string'
        self.assertEqual(Rotate(s, 2), 'ngstri')

if __name__=="__main__":
    unittest.main()
