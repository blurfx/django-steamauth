from setuptools import setup, find_packages
import pathlib


def long_description():
    here = pathlib.Path(__file__).parent.resolve()
    return (here / 'README.md').read_text()


setup(
    name='django-steamauth',
    packages=find_packages('steamauth'),
    version='1.1.2.1',
    author='blurfx',
    author_email='iam@xo.dev',
    license='MIT License',
    url='https://github.com/blurfx/django-steamauth',
    description='Django integrated Steam OpenID auth library',
    long_description=long_description(),
    long_description_content_type='text/markdown',
    keywords=['django', 'steam', 'valve', 'steamid', 'openid'],
    python_requires='>=3',
    install_requires=[
        'django'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License'
    ],
    project_urls={  # Optional
        'Bug Reports': 'https://github.com/blurfx/django-steamauth/issues',
        'Source': 'https://github.com/blurfx/django-steamauth',
    },
)