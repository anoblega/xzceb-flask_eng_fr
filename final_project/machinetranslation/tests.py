import unittest

from machinetranslation import translator


class TestMachineTranslation(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(translator.englishToFrench(null), null)



if __name__=='__main__':
    unittest.main()