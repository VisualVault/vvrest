import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='vvrest',
    version='1.0.0',
    author='Jared Runyon',
    author_email='jared.runyon@visualvault.com',
    maintainer='Jared Runyon',
    maintainer_email='jared.runyon@visualvault.com',
    description='A Python REST client library for accessing VisualVault.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/VisualVault/vvrest',
    packages=setuptools.find_packages(exclude=['tests']),
    install_requires=['requests'],
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
