# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name='browser-agents',
    version='2.2.0+epic.1',
    author='Selwin Ong',
    author_email='selwin.ong@gmail.com',
    packages=['browser_agents'],
    url='https://github.com/selwin/python-user-agents',
    license='MIT',
    description='A library to identify devices (phones, tablets) and their capabilities by parsing browser user agent strings.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    zip_safe=False,
    include_package_data=True,
    package_data={'browser_agents': ['devices.json']},
    install_requires=['ua-parser>=0.10.0'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
