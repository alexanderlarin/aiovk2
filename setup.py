import codecs
import os
import re

from setuptools import setup, find_packages

with open('README.rst', 'r', encoding='utf8') as f:
    readme = f.read()

with open('requirements.txt') as f:
    requirements = list(map(lambda x: x.strip(), f.readlines()))

with codecs.open(os.path.join(os.path.abspath(os.path.dirname(
        __file__)), 'aiovk2', '__init__.py'), 'r', 'latin1') as fp:
    try:
        version = re.findall(r"^__version__ = '([^']+)'\r?$",
                             fp.read(), re.M)[0]
    except IndexError:
        raise RuntimeError('Unable to determine version.')

setup(
    name='aiovk2',
    version=version,

    author='Alexander Larin',
    author_email='ekzebox@gmail.com',

    url='https://github.com/alexanderlarin/aiovk2',
    description='vk.com API python wrapper for asyncio',
    long_description=readme,

    packages=find_packages(),
    install_requires=requirements,

    license='MIT License',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='vk.com api vk wrappper asyncio',
    test_suite="tests",
    python_requires='>=3.6'
)
