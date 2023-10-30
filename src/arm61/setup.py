#!/usr/bin/env python3

import os
from glob import glob
from setuptools import setup

package_name = 'arm61'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        # Install marker file in the package index
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        # Include our package.xml file
        ('share/' + package_name, ['package.xml']),
        # Include all launch files.
        (os.path.join('share', package_name, 'launch'), glob(os.path.join('launch', '*.launch.py'))),
        # Include rviz config files
        (os.path.join('share', package_name, 'rviz'), glob(os.path.join('rviz', '*.rviz'))),
        # Include urdf files
        (os.path.join('share', package_name, 'urdf'), glob(os.path.join('urdf', '*.urdf'))),
        # Include stl files
        (os.path.join('share', package_name, 'urdf', 'lowPoly'), glob(os.path.join('urdf', 'lowPoly', '*.stl'))),
        (os.path.join('share', package_name, 'urdf', 'highPoly'), glob(os.path.join('urdf', 'highPoly', '*.stl'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ddaners',
    maintainer_email='ddaners@mawsonrovers.com',
    description='ARM61 urdf visualisation using RVIZ',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
