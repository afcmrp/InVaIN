from setuptools import setup, find_packages

packages=find_packages(exclude=['contrib', 'docs', 'tests*'])

setup(
  name = 'InVaIN',
  version = '0.1',
  description = 'A util to pull stock data',
  author = 'Alan Arechiga',
  author_email = 'alan@macler.us',
  license = 'MIT',
  url = 'https://github.com/hailfire113/InVaINe', # use the URL to the github repo
  download_url = 'https://github.com/hailfire113/InVaIN/archive/0.1.tar.gz', # I'll explain this in a second
  keywords = ['testing', 'stocks', 'data'], # arbitrary keywords
  classifiers=[
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    # Pick your license as you wish (should match "license" above)
     'License :: OSI Approved :: MIT License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
   ],
   packages=find_packages(exclude=['contrib', 'docs', 'tests']),
   install_requires=['requests','json'],
)