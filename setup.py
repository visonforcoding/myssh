from setuptools import setup
setup(
    name='myssh',
    version='0.1',
    scripts=['./myssh'],
    keywords='ssh tool',
    description='a ssh tool for terminal',
    author='visonforcoding',
    author_email='visonforcoding@gmail.com',
    url='https://github.com/visonforcoding/myssh',
    install_requires=[
        'click>=6.7',
    ],
    package_data={
        "": ["dataset/server.db"],
    },
)
