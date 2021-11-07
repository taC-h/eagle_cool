from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='eagle_cool',
    packages=['eagle_cool'],

    version='0.1.0',

    license='MIT',

    install_requires=['requests'],

    author='taC-h',
    author_email='tac.handstandingcat@gmail.com',

    url='https://github.com/taC-h/eagle_cool',

    description='eagle.cool api library for Python',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='eagle_cool eagle-cool eagle',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)