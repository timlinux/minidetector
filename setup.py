from distutils.core import setup

setup(
    name='minidetector',
    version='0.1dev',
    packages=['minidetector',],
    package_data={'minidetector': ['search_strings.txt']},
    license='New BSD License',
    long_description=open('README').read(),
)
