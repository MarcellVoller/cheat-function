from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='cheat-function',
    url='https://github.com/MarcellVoller/cheat-function',
    author='Marcell Völler',
    author_email='marcellvoeller@yahoo.com',
    # Needed to actually package something
    packages=['cheat-function'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='A simple cheat function for PIPS',
    # long_description=open('README.md').read(),
)
