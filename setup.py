from setuptools import find_packages
from setuptools import setup

version = '0.1'

setup(
    name='bobtemplates.leftxs',
    version=version,
    description="mr.bob templates ",
    long_description=open("README.rst").read() + "\n" +
                     open("CHANGES.rst").read(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",
    ],
    keywords='',
    author='Sven Strack',
    author_email='sven@so36.net',
    url='https://github.com/svx/bobtemplates.leftxs',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['bobtemplates'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'mr.bob',
    ],
    entry_points={},
)
