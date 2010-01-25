from setuptools import setup, find_packages
import os

version = '1.0.1dev'

setup(name='silvatheme.standardissue',
      version=version,
      description="Standard Issue theme for Silva",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Framework :: Zope2",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='silvatheme standardissue',
      author='Infrae - Design by NodeThirtyThree',
      author_email='info@infrae.com',
      url='http://infrae.com/products/silva',
      license='BSD',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['silvatheme'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'megrok.chameleon',
          'silva.core.interfaces',
          'silva.core.layout',
          'zope.cachedescriptors',
          ],
      )
