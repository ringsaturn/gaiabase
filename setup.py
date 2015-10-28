from distutils.core import setup

setup(
    name='gaiabase',
    version='0.1.0',
    author='Mingli Yuan',
    author_email='mingli.yuan@gmail.com',
    packages=['gaia'],
    package_dir={'gaia': 'gaia'},
    url='git+https://github.com/caiyunapp/gaiabase.git',
    license='LICENSE',
    description='The base library for gaia-based projects',
    long_description=open('README.md').read(),
    install_requires=[
        "PyYAML"
    ],
)