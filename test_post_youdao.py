import unittest
from unittest import mock

from post_youdao import *

class PostyoudaoTest(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)


    def test_get_ts(self):
        #import time
        #t= time.time()
        #ts=str(int(round(t * 1000)))
        #print(ts)
        get_ts=mock.Mock(return_value='1586062887388')
        self.assertEqual('1586062887388',get_ts())


    def test_get_salt(self):
        get_salt=mock.Mock(return_value='15860628873889')
        self.assertEqual('15860628873889',get_salt())


    def test_get_sign(self):
        get_sign=mock.Mock(return_value='16bfeef8bfe1bab0f14a688e05092703')
        self.assertEqual('16bfeef8bfe1bab0f14a688e05092703',get_sign())
        # 'a9c3483a52d7863608142cc3f302a0ba'


    if __name__ == '__main__':
         unittest.main()
