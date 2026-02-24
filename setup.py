#/usr/bin/env python
import io
import re
from setuptools import setup


with io.open('./xero/__init__.py', encoding='utf8') as version_file:
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file.read(), re.M)
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")


with io.open('README.md', encoding='utf8') as readme:
    long_description = readme.read()


setup(
    name='pyxero',
    version=version,
    description='Python API for accessing the REST API of the Xero accounting tool.',
    long_description=long_description,
    author='Russell Keith-Magee',
    author_email='russell@keith-magee.com',
    url='http://github.com/freakboy3742/pyxero',
    packages=['xero', ],
    install_requires=[
        'requests>=2.20.0',
        'requests-oauthlib>=1.0.0',
        'python-dateutil>=2.8.0',
        'PyJWT>=2.0', # This is required as part of oauthlib but doesn't seem to get included sometimes.
        'cryptography>=3.0', # As above, but fixes issue with missing module imports not picked up for some reason.
    ],
    license='New BSD',
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Financial and Insurance Industry',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Topic :: Office/Business :: Financial :: Accounting',
    ],
    test_suite="tests",
)
