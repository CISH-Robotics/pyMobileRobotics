from setuptools import find_packages
from setuptools import setup

setup(name='pyMobileRobotics',
      version='0.0.5',
      description='WorldSkills Mobile Robotics System',
      author='CISH Robotics',
      author_email='crt@cish.xyz',
      url='https://github.com/CISH-Robotics',
      keywords='robot worldskills mobile robotics',
      project_urls={
            'Source': 'https://github.com/CISH-Robotics/pyMobileRobotics',
      },
      packages=find_packages(),
      install_requires=[
            'oclock>=1.3.0',
            'coloredlogs>=15.0.1',
            'opencv-contrib-python>=4.1.0.25',
            'imutils>=0.5.4'
            ],
      python_requires='>=3'
     )