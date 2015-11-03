from setuptools import setup, find_packages

setup(
    name='analysis',
    version='0.0.1',
    author='Sandy Ryza, Juliet Hougland',
    author_email='sryza@cloudera.com, juliet@cloudera.com',
    packages=find_packages(),
    description='Churn model using PySpark',
    long_description='Source code to accompany "Data Science for Telcom" tutorial at Hadoop World Singapore 2015',
    install_requires=[
        'scipy==0.16.0',
        'numpy==1.9.2'
    ],
)
