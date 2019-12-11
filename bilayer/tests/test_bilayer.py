"""
Unit and regression test for the bilayer package.
"""

# Import package, test suite, and other packages as needed
import pytest
import sys
import numpy as np
import mbuild as mb
import bilayer
from .utils import load_lipid
from .utils import load_solvent

def test_bilayer_imported():
    """ Sample test, will always pass so long as import statement worked. """
    assert "bilayer" in sys.modules

def test_import():
    """ Test that mBuild recipe import works. """
    assert "Bilayer" in vars(mb.recipes).keys()

def test_build():
    """ Test building a bilayer with an alcohol and water solvent. """

    # Load in lipid and solvent mbuild compounds
    lipid = load_lipid()
    lipids = [(lipid, 1.0)]
    ref_atoms = [47]
    solvent = load_solvent()

    # Specify some options
    area_per_lipid = 0.2
    solvent_per_lipid = 10
    solvent_density = 1.0
    solvent_mass = 18.02
    tilt = 5 * np.pi / 180.0

    bilayer = mb.recipes.Bilayer(lipids, ref_atoms, solvent=solvent,
                              solvent_density=solvent_density,
                              solvent_mass=solvent_mass,
                              solvent_per_lipid=solvent_per_lipid,
                              area_per_lipid = area_per_lipid,
                              tilt=tilt)

    assert len(bilayer.children) == 2
    assert bilayer.n_particles == 16200
    assert bilayer[2019].name == 'H'
