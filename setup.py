from setuptools import setup, find_packages

setup (
        name    =   'django-steamauth',
        packages = ['steamauth'],
        version     = '1.0.0',
        author  = 'mystika',
        author_email    = 'pipsit@gmail.com',
        license          = 'MIT License',
        url         = 'https://github.com/Mystika/django-steamsignin',
        description = 'steam login library for django',
        keywords=['django', 'steam', 'valve', 'steamid', 'openid'],
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Operating System :: OS Independent',
            'Intended Audience :: Developers',
            'Framework :: Django',
            'Framework :: Django :: 1.8',
            'License :: OSI Approved :: MIT License'
        ],
)