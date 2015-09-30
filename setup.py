from setuptools import setup, find_packages
import os

version = '1.2.2'

tests_require = [
    'ftw.testbrowser',
    'ftw.testing',
    'plone.app.testing',
]

setup(
    name='ftw.colorbox',
    version=version,
    description="An image gallery for Plone using ColorBox",
    long_description='{0}\n{1}'.format(
        open("README.rst").read(),
        open(os.path.join("docs", "HISTORY.txt")).read()
    ),

    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],

    keywords='ftw colorbox',
    author='4teamwork AG',
    author_email='mailto:info@4teamwork.ch',
    url='https://github.com/4teamwork/ftw.colorbox',
    license='GPL2',

    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['ftw'],
    include_package_data=True,
    zip_safe=False,

    install_requires=[
        'ftw.upgrade',
        'setuptools',
    ],

    tests_require=tests_require,
    extras_require=dict(tests=tests_require),

    entry_points="""
    # -*- Entry points: -*-
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
