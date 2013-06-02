from setuptools import setup

setup(
    name='Lost Property',
    version='1.0',
    long_description=__doc__,
    packages=['lostproperty'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask', 'Frozen-Flask']
)
