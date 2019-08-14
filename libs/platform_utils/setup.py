from setuptools import setup, find_packages
import io

__version__ = 0.40

install_requires = []
import platform
if platform.system() == 'Windows':
	install_requires += ['winpaths', 'pypiwin32']


setup(
	name = 'platform_utils',
	version = __version__,
	description = """Cross-platform utilities for accomplishing some tasks that the stdlib isn't equipped to provide""",
	long_description = io.open('README.rst', encoding='UTF8').read(),
	install_requires = install_requires,
	packages = find_packages(),
	zip_safe = False,
	classifiers = [
		'Development Status :: 4 - Beta',
		'Intended Audience :: Developers',
		'Programming Language :: Python',
		'License :: OSI Approved :: MIT License',
		'Topic :: Software Development :: Libraries'
	],
)
