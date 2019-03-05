
import sys
def incr(x):
    print sys.version_info
    return x + 1

def test_incr():
    assert incr(3) == 4
