from setuptools import setup, find_packages

setup(
    name='tw2.dyntext',
    version='0.0.3',
    description='Dynamic Text widget for TW2. Allows text to be pulled from JSON objects live.',
    author='Greg Jurman',
    author_email='gdj2214@rit.edu',
    url='http://github.com/gregjurman/tw2.dyntext',
    install_requires=[
        "tw2.core",
        "tw2.jquery",
        "mako"
        ## Add other requirements here
        # "Genshi",
        ],
    packages=find_packages(exclude=['ez_setup', 'tests']),
    namespace_packages = ['tw2'],
    zip_safe=False,
    include_package_data=True,
    tests_require = [
        'nose',
        'BeautifulSoup',
        'Genshi',
        'mako',
        # formencode isn't actually needed, but is just here to patch up
        # tw2.forms,
        'formencode',
        'strainer',
        'WebTest'
    ],
    test_suite = 'nose.collector',
    entry_points="""
        [tw2.widgets]
        # Register your widgets so they can be listed in the WidgetBrowser
        widgets = tw2.dyntext
    """,
    keywords = [
        'toscawidgets.widgets',
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Environment :: Web Environment :: ToscaWidgets',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Widget Sets',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
