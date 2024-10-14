from setuptools import setup, find_packages

setup(
    name='deauth.wifi',
    version='1.0',
    packages=find_packages(),
    install_requires=['scapy'],
    entry_points={
        'console_scripts': [
            'deauth.wifi=deauth_wifi:main',
        ],
    },
    description='A Scapy script for deauthing and manipulating WiFi networks',
)
