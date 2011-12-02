#!/usr/bin/env python
from distutils.core import setup
import os
from gadjo import VERSION


# taken from django-registration
# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)

for dirpath, dirnames, filenames in os.walk('admin_tools'):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if '__init__.py' in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)
    elif filenames:
        prefix = dirpath[12:] # Strip "admin_tools/" or "admin_tools\"
        for f in filenames:
            data_files.append(os.path.join(prefix, f))

#bitbucket_url = 'http://www.bitbucket.org/izi/django-admin-tools/'
#long_desc = '''
#%s
#
#%s
#''' % (open('README').read(), open('CHANGELOG').read())
long_description='gadjo.requestprovider solves the problem of accessing\
                 django\'s HTTPRequest object whenever is needed, without\
                 explicitely passing it down the path of code.',


setup(
    name='django-contrib-requestprovider',
    version=VERSION.replace(' ', '-'),
    description=long_description,
    long_description=long_description,
    author='django-contrib-requestprovider',
#    author_email='izimobil@gmail.com',
#    url=bitbucket_url,
#    download_url='%sdownloads/django-admin-tools-%s.tar.gz' % (bitbucket_url, VERSION),
    package_dir={'gadjo': 'gadjo'},
    packages=packages,
    package_data={'gadjo': data_files},
    license='BSD License',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
