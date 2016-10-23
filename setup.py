from setuptools import setup, find_packages
from setuptools.command.install import install as _install

import sys
class InstallHook(_install):
	def run(self):
		self.preInstall()
		_install.run(self)
	def preInstall(self):
		if sys.version_info[0] >= 3 or sys.version_info <= (2,5):
			raise Exception("This module only supports Python 2.6 or 2.7")

setup(
	cmdclass = {"install": InstallHook},
	name = "Skeleton_Python",
	version = "0.0.1",
	description = "",
	author = "",
	author_email = "",
	url = "",
	
	package_dir = {"":"src"},
	packages = find_packages("src"),
	zip_safe = False,
	test_suite = "test",
	
	install_requires = [
		"foo",
	],
	classifiers = [
		# http://pypi.python.org/pypi?%3Aaction=list_classifiers
		"Development Status :: 5 - Production/Stable",
		"Programming Language :: Python :: 2.6",
		"Programming Language :: Python :: 2.7",
		"Operating System :: OS Independent",
	],
)
