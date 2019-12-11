import mbuild as mb
from os.path import dirname, join

def _get_library_dir():
    """ Returns the absolute path to the test compound library. """
    compound_library = join(dirname(__file__), "test_cpds")
    return compound_library

def load_solvent():
    file_path = join(_get_library_dir(), "test_solvent.mol2")
    compound = mb.load(file_path)
    return compound

def load_lipid():
    file_path = join(_get_library_dir(), "test_lipid.mol2")
    compound = mb.load(file_path)
    return compound
