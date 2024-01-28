from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='cheat-function',
    url='https://github.com/MarcellVoller/cheat-function',
    author='Marcell Völler',
    author_email='marcellvoeller@yahoo.com',
    # The license can be anything you like
    license='MIT',
    description='A simple cheat function for PIPS',

    py_modules=["cheat"]
)
