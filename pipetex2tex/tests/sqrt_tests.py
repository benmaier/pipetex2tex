import unittest

import numpy as np

from pipetex2tex.sqrt import get_sqrt_2

class SqrtTest(unittest.TestCase):

    def test_sqrt(self):

        a = get_sqrt_2()
        b = np.sqrt(2)

        assert(np.isclose(a,b))

if __name__ == "__main__":

    T = SqrtTest()
    T.test_sqrt()
