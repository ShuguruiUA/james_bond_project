from setuptools import setup, find_namespace_packages

setup(
    name='james_bond_assistant',
    version='0.0.12',
    description='This is yours personal assistant, James Bond',
    author="Iurii, Serhii, Svitlana, Kristina, Daryna",
    url='https://github.com/ShuguruiUA',
    packages=find_namespace_packages(),
    install_requires=['prompt-toolkit==3.0.43', 'rich==13.7.0' ],
    include_package_data=True,
    entry_points={'console_scripts': ['007-assistant=james_bond_assistant.main:main']}
)
