from setuptools import setup

setup(
    name='StakkrPhpCron',
    version='3.5',
    packages=['phpcron'],
    entry_points='''
        [stakkr.plugins]
        phpcron=phpcron.core:phpcron
    '''
)
