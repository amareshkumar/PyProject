try:
	from setuptools import setup
except importError:
		from distutils.core import setup

config  = {
	'description': 'Kumar Python Project',
	'author':	'Amaresh Kumar',
	'url': 'to be updated',
	'dwonload_url': 'to be updated',
	'author email': 'amaresh.kumar@live.in',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': ['bin/hello.py'],
	'name': 'pythonproject'
}

setup(**config)