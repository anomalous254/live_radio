from setuptools import setup, find_packages

setup(
    name='live_radio',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        'pyradios',
    ],
    author='Peter Nyando',
    author_email='nyandopeter2@gmail.com', 
    description='Get live radio station streams by country',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/anomalous254/live_radio',
    license='MIT', 
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License', 
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6', 
)
