from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
	name='ckanext-mef_theme',
	version=version,
	description="CKAN extension for theme of MEF",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='Creainter SAC',
	author_email='comercial@creainter.com.pe',
	url='https://www.creainter.com.pe',
	license='',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.mef_theme'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points=\
	"""
        [ckan.plugins]
	# Add plugins here
    mef_theme=ckanext.mef_theme.plugin:MEFThemeCustomizations
	""",
)
