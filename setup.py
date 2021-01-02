from setuptools import setup

setup(
    name='murli',
    version='0.1.0',
    py_modules=['murli'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        murli=murli.main:murli
    ''',
)