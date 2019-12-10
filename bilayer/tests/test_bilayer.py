"""
Unit and regression test for the bilayer package.
"""

# Import package, test suite, and other packages as needed
import bilayer
import pytest
import sys
import mbuild as mb

def test_bilayer_imported():
    """ Sample test, will always pass so long as import statement worked """
    assert "bilayer" in sys.modules

def test_import():
    """ Test that mBuild recipe import works """
    assert "Bilayer" in vars(mb.recipes).keys()
