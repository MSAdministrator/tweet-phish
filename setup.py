from setuptools import setup, find_packages

def parse_requirements(requirement_file):
    with open(requirement_file) as f:
        return f.readlines()

version = dict()
with open("./tweetphish/utils/version.py") as fp:
    exec(fp.read(), version)


setup(
    name='tweet-phish',
    version=version['__version__'],
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='A Python package created using carcass',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=parse_requirements('./requirements.txt'),
    keywords=['carcass'],
    url='https://github.com/MSAdministrator/tweet-phish',
    author='MSAdministrator',
    author_email='rickardja@live.com',
    python_requires='>=3.6, <4',
    package_data={
        'tweetphish':  ['data/logging.yml', 'data/tweet.yml']
    },
    entry_points={
          'console_scripts': [
              'tweet-phish = tweetphish.__main__:main'
          ]
    }
)