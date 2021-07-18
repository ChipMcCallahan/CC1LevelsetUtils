from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='CCUtils',
    url='https://github.com/ChipMcCallahan/CCUtils',
    author='Chip McCallahan',
    author_email='thisischipmccallahan@gmail.com',
    # Needed to actually package something
    packages=['ccutils'],
    # Needed for dependencies
    install_requires=['struct', 'io'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='GNU General Public License v3.0',
    description='General utils for working with CC1 and CC2 files',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)
