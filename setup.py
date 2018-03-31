from setuptools import setup, find_packages

test_deps = ['pytest', 'pytest-runner', 'pytest-flask']

setup(
    name='PoliEdro Donation Website',
    version='0.1',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask', 'Flask-SQLAlchemy', 'paypalrestsdk==2.0.0rc1', 'flask-cors', 'Flask-Babel'] + test_deps,
    dependency_links=[
        "https://github.com/Depau/braintreehttp_python-noparseresponse/archive/noparse.zip#egg=braintreehttp-0.4.3"
    ],
    test_require=test_deps,
    entry_points={
        'console_scripts': [
            'poliedro_donate = poliedro_donate.cli:main',
        ]
    }
)
