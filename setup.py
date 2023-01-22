from setuptools import setup, find_packages

setup(
    name='topsis-102003452',
    version='0.1',
    description='A topsis package',
    author='Kunwar Apoorvaditya',
    author_email='apoorvadityakunwar@gmail.com',
    url='https://github.com/kunwar-code/topsis',
    packages=find_packages(),
    install_requires=[
        'numpy',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
