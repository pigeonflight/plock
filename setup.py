#------------------------------------------------------------------------------
# Pyroma says:
# Final rating: 10/10
# Your cheese is so fresh most people think it's a cream: Mascarpone
#------------------------------------------------------------------------------
from setuptools import find_packages
from setuptools import setup


VERSION = '0.2.8'


setup(
    author="Alex Clark",
    author_email="aclark@aclark.net",
    classifiers=[
        'Framework :: Plone :: 4.3',
        'Programming Language :: Python :: 2.7',
    ],
    description="A Plone installer for the pip-loving crowd",
    entry_points={
        # "EntryPoint must be in 'name=module:attrs [extras]' format"
        'console_scripts': [
            'plock=plock.install:install',
        ],
    },
    install_requires=[
        'configparser',
        'sh',
        'virtualenv==1.9.1',
        'yolk',
        'zc.buildout==1.7.1',
        'setuptools==1.4.2'
    ],
    keywords="buildout pip plone virtualenv zope",
    license='Whatever license Plone is',
    long_description=(
        open('README.rst').read() + '\n' +
        open('CHANGES.rst').read()
    ),
    name='plock',
    packages=find_packages(),
    test_suite='plock.tests',
    tests_require=[
        'mock',
        'nose',
    ],
    url='https://github.com/plock/plock',
    version=VERSION,
    zip_safe=False,
)
