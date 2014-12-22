from setuptools import setup

setup(
    name = 'colourcat',
    version = '0.1',
    description = 'Dump files with syntax-highlighting to console, and other console utilities.',
    url = 'https://github.com/lincheney/colourcat',
    author = 'Cheney Lin',
    author_email = 'lincheney@gmail.com',
#    packages = ['colourcat'],
    scripts = ['bin/colourcat'],
    install_requires = ['pygments', 'python-magic'],
)
