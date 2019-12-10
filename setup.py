from setuptools import setup


setup(
    # Self-descriptive entries which should always be present
    name='bilayer',
    author='Parashara Shamaprasad and Tim Moore',
    author_email='p.shama@vanderbilt.edu',
    license='MIT',
    version='0.0.0',
    description='A bilayer building plugin for mBuild.',
    zip_safe=False,
    entry_points={
        'mbuild.plugins':[
        "Bilayer = bilayer.bilayer:Bilayer"
        ]
        }
    )
