from setuptools import setup
VERSION = (0,3,'pre')

# Dynamically calculate the version based on VERSION tuple
if len(VERSION) > 2 and VERSION[2] is not None:
    str_version = "%s.%s_%s" % VERSION[:3]
else:
    str_version = "%s.%s" % VERSION[:2]

version = str_version

setup(
    name='nose_command_summary',
    version=version,
    description="A python nose plugin to print a summary of the commands to run failing tests.",
    long_description="A python nose plugin to print the commands necessary to rerun just the failing/erroring tests at the end of the printout.",
    author='Levon K Mkrtchyan',
    author_email='',
    url='https://github.com/levonmk/nose-command-summary',
    install_requires=[
        'nose==1.0.0',
    ],
    setup_requires=[],
    test_suite='nose.collector',
    zip_safe=False,
    py_modules=['nose_timer'],
    entry_points={
        'nose.plugins.0.10': [
            'nose_command_summary = nose_command_summary:CommandSummary',
        ]
    },
)
