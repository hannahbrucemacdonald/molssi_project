"""
Unit and regression test for the molssi_project package.
"""

# Import package, test suite, and other packages as needed
import molssi_project
import pytest
import sys

def test_molssi_project_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "molssi_project" in sys.modules
