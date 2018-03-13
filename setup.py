from setuptools import setup, find_packages

setup(
    name='PoliEdro Donation Website',
    version='0.1',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask', 'Flask-SQLAlchemy', 'paypalrestsdk==2.0.0rc1', 'flask-cors'],
    dependency_links=[
        "https://github.com/paypal/PayPal-Python-SDK/archive/2.0-beta.zip"
    ],
    setup_requires=['pytest-runner'],
    test_requires=['pytest']
)
