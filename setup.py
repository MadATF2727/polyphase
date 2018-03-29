from distutils.core import setup

setup(name='polyphase',
      version='1.0',
      description='Polyphase Filter Decimate',
      author='Arna Friend',
      author_email='madatf2727@gmail.com',
      url='https://github.com/MadATF2727/polyphase',
      packages=['src', 'test'],
      install_requires=['math','numpy', 'scipy', 'matplotlib'],
     )