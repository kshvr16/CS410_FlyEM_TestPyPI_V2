from setuptools import setup, find_packages


setup(
    name='CS410_FlyEM_V1',
    version='0.1',
    license='MIT',
    author="Sai Harshavardhan Reddy Kona",
    author_email='kshvr1699@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/kshvr16/CS410_FlyEM_TestPyPI_V2',
    keywords='Testing PyPi deployment',
    install_requires=[
          'matplotlib',
          'scikit-image'
      ],

)
