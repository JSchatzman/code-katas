"""Setup for code-katas."""

from setuptools import setup


setup(
    name='code-katas',
    description='snow-day assignment',
    version=0.1,
    author='Jordan Schatzman',
    author_email='j.schatzman@outlook.com',
    license='MIT',
    # package={'': 'src'},
    #  py_module=['ackermann'],
    # install_requires=['numpy'],
    extras_require={'test': ['pytest', 'pytest-watch', 'pytest-cov', 'tox']}
    # entry_points={'console scripts': ['ackermann = ackerman:ackermann']}
)
