from distutils.core import setup

add_keywords = dict(
    entry_points = {
        'console_scripts': ['definition = definition.definition:main'],
    },
)

fhan = open('requirements.txt', 'rU')
requires = [line.strip() for line in fhan.readlines()]
fhan.close()
try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    fhan = open('README.txt')
    long_description = fhan.read()
    fhan.close()

setup(
        name='definition',
        description='Definition fetcher from 5 online dictionaries',
        version='0.0.4',
        packages=['definition'],
        license='GPLv3+',
        author='Shubham Chaudhary',
        author_email='me@shubhamchaudhary.in',
        url='https://github.com/shubhamchaudhary/definition',
        long_description=long_description,
        install_requires=requires,
        **add_keywords
)

