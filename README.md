mbuild_bilayer
==============================
[//]: # (Badges)
[![Travis Build Status](https://travis-ci.org/uppittu11/mbuild_bilayer.svg?branch=master)](https://travis-ci.org/uppittu11/mbuild_bilayer)
[![codecov](https://codecov.io/gh/uppittu11/mbuild_bilayer/branch/master/graph/badge.svg)](https://codecov.io/gh/uppittu11/mbuild_bilayer/branch/master)

A bilayer building plugin for mBuild.

Usage:
`mbuild.recipes.Bilayer()`:

 Bilayer(lipids, ref_atoms, n_lipids_x=10, n_lipids_y=10, area_per_lipid=1.0, lipid_box=None, spacing_z=None, solvent=None, solvent_per_lipid=None, n_solvent=None, solvent_density=None, solvent_mass=None, tilt=0, random_seed=12345, mirror=True)
 
Arguments:

* lipids : list
 
     *List of tuples in format `(lipid, frac)` where frac is the fraction of that lipid in the bilayer (lipid is a Compound)*
     
* ref_atoms : int
 
     *Indices of the atom in lipids to form the interface, one for each lipid in lipids (i.e., this atom is shifted to the 'interface' level)*
     
* n_lipids_x : int
 
     *Number of lipids in the x-direction per layer.*
     
* n_lipids_y : int
 
     *Number of lipids in the y-direction per layer.*
     
* area_per_lipid : float
 
     *Area per lipid.*
     
* solvent : Compound
 
     *Compound to solvate the bilayer with. Typically, a pre-equilibrated box of solvent.*
     
* lipid_box : mb.Box, optional
 
     *A mb.Box containing the lipids where no solvent will be added.*
     
* spacing_z : float, optional
 
     *Amount of space to add between opposing monolayers.*
     
* solvent_per_lipid : int, optional, default=None
 
     *Number of solvent molecules per lipid*
     
* n_solvent : int, optional, default=None
 
     *Total number of solvent molecules.*
     
* tilt: float, optional, default=None
 
     *Tilt angle relative to the bilayer normal to prescribe to lipids. Units are radians.*
     
* random_seed : int, optional, default=12345
 
     *Seed for random number generator for filling in lipids.*
     
* mirror : bool, optional, default=True
 
     *Make top and bottom layers mirrors of each other.*

### Copyright

Copyright (c) 2019, Parashara Shamaprasad and Tim Moore


#### Acknowledgements
 
Project based on the 
[mBuild Recipe Cookiecutter](https://github.com/rmatsum836/mbuild-cookiecutter)
