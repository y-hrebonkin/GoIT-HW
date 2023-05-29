from setuptools import setup, find_packages

setup(
    name='clean_folder',
    version='0.1',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'clean-folder = clean_folder.clean_folder.clean:main',
        ],
    },
)