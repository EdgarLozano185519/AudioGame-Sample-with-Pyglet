from setuptools import setup, find_packages
from libloader import __author__, __author_email__, __doc__, __version__

setup(
 name = 'libloader',
 version = __version__,
 author = __author__,
 author_email = __author_email__,
 description = __doc__,
 packages = find_packages(),
 zip_safe = False,
 classifiers = [
  'Development Status :: 3 - Alpha',
  'Intended Audience :: Developers',
  'Programming Language :: Python',
  'Topic :: Software Development :: Libraries',
 ],
)
