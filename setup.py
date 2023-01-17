from setuptools import setup, find_packages

setup(
    name='Assignment',
    extras_required=dict(tests=['pytest']),
    packages=find_packages(where='Source_data'),
    package_dir={"": "Source_data"}
)
