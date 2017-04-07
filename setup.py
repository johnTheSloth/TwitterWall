from setuptools import setup, find_packages


with open('README') as f:
    long_description = ''.join(f.readlines())


setup(
    name='john_the_sloth_twitterwall',
    version='0.2',
    description='Twitterwall console application.',
    long_description=long_description,
    author='Jan Grossmann',
    author_email='muj@email.cz',
    keywords='holiday,dates',
    license='Public Domain',
    url='http://naucse.python.cz/2017/pyknihovny-brno/intro/distribution/',
    packages=find_packages(),
    classifiers=[
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries',
        ],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'twitterwall = twitterwall.ukol1:main',
        ]
    },
    install_requires=['requests', 'click>=6'],
    package_data={
        'twitterwall' : ['templates/*.html'],
    },
)
