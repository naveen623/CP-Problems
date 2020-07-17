
import os,sys
sys.path.append(os.getcwd())
from isrotation import isrotation
import pytest


@pytest.mark.parametrize("a, b, result",[
	(3412, 1234, True), (12345, 54321, False),
	(1234, 1234, True), (12345, 4321, False),
	(3142, 1234, False), (10010, 10100, False),
	(431256789, 123456789, False), (101111, 11110, False),
])
def test_isrotation(a, b, result):    
    assert isrotation(a, b) == result
