from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup (
        name='django-steamauth',
        packages=['steamauth'],
        version='1.1.1',
        author='blurfx',
        author_email='pipsit@gmail.com',
        license='MIT License',
        url='https://github.com/blurfx/django-steamauth',
        description='Django integrated Steam OpenID auth library',
        long_description=readme(),
        keywords=['django', 'steam', 'valve', 'steamid', 'openid'],
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
)