from distutils.core import setup
import wepay

long_description = open('README.rst').read()

version_str = '%s.%s.%s' % (
    wepay.VERSION[0],
    wepay.VERSION[1],
    wepay.VERSION[2]
)

setup(
    name='wepay',
    version=version_str,
    packages=['wepay'],
    description='A Python SDK for our WePay API.',
    long_description=long_description,
    author='Bryce Culhane',
    author_email='bryce@wepay.com',
    license='MIT License',
    url='https://github.com/wepay/Python-SDK',
    platforms=["any"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
