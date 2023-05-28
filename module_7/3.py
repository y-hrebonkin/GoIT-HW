from setuptools import setup, find_namespace_packages

def do_setup(args_dict, requires, entry_points):
    args_dict['packages'] = find_namespace_packages()
    args_dict['install_requires'] = requires
    args_dict['entry_points'] = entry_points
    setup(**args_dict)


requires = ['markdown']

entry_points = {'console_scripts': ['helloworld = useful.some_code:hello_world']}