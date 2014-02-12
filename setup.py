from distutils.core import setup

setup(
    name='nasbkp',
    version='0.1',
    packages=['nasbkp', 'nasbkp.tests', 'nasbkp.common', 'nasbkp.storage'],
    url='',
    license='ISC',
    author='Alexandre Vaissière',
    author_email='avaiss@fmiw.org',
    description='Automated backup for zfs volume'
)
