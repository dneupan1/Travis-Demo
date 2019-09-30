import pytest
import subprocess

def test_sort():
	p = subprocess.run(["python", "src\\QuickSort.py", "--array=3,2,1"])
	## this test is not complete
