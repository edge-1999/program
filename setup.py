from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license_ = f.read()

setup(
    name='AI',
    version='1999.9.29',
    description='siyuan.li',
    long_description=readme,
    author='siyuan',
    author_email='lijd1999@icloud.com',
    url='https://entirely.com/',
    license=license_,
    packages=find_packages(exclude=('./', 'docs'))
)
