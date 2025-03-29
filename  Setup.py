 from setuptools import setup, find_packages

setup(
    name='stressmeter',
    version='0.1.0',
    description='A Python library to analyze stress levels based on various indicators.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Krishna Rakholiya',   
    author_email='krishnarakholiya001@gmail.com',   
    url='https://github.com/krishnarakholiya20/StressMeter/', 
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Healthcare Professionals',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    install_requires=[],  # Add any dependencies your library needs here
    python_requires='>=3.6',
)