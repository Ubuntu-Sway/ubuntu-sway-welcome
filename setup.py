from importlib.metadata import entry_points
from setuptools import setup, find_packages

setup(
    name='ubuntu-sway-welcome',
    version='1.4.3',
    description='welcome app for Ubuntu Sway',
    license='GPL-3',
    author='Aleksey Samoilov',
    author_email='samoilov.lex@gmail.com',
    url='https://github.com/Ubuntu-Sway/ubuntu-sway-welcome',
    packages=find_packages(),
    include_package_data=True,
    package_data={"": ["resources/*", "ui/*"]},
    data_files=[
        ('share/applications', ['ubuntu_sway_welcome/resources/ubuntu-sway-welcome.desktop']),
        ('share/icons/hicolor/256x256/apps', ['ubuntu_sway_welcome/resources/ubuntu-sway.png']),
    ],
    install_requires=[],
    entry_points={
        'gui_scripts': [
            'ubuntu-sway-welcome = ubuntu_sway_welcome.main:main'
        ]
    }
)
