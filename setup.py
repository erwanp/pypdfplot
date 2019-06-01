from setuptools import setup

setup(name='pypdfplot',
      version='1.0.0',
      description="Saves plots as PDF with embedded generating script",
      author='Dirk van den Bekerom',
      author_email='dcmvdbekerom@gmail.com',
      license='MIT',
      url = 'https://github.com/dcmvdbekerom/pypdfplot',
      packages=['pypdfplot'],
      install_requires=['matplotlib','PyPDF4'],
      zip_safe=False)
