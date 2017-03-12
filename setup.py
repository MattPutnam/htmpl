from setuptools import setup


def readme():
    with open('README.md') as stream:
        return stream.read()


setup(name='htmpl',
      version='0.1',
      description='HTML template library',
      long_description=readme(),
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Licence :: Public Domain',
          'Programming Language :: Python :: 3',
          'Topic :: Software Development :: Libraries :: Python Modules'
      ],
      keywords='html template',
      url='https://github.com/MattPutnam/htmpl',
      author='Matt Putnam',
      packages=['htmpl'],
      install_requires=[
          'mistune'
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True,
      zip_safe=False)
