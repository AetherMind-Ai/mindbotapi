from setuptools import setup, find_packages

setup(
    name='mindbotapi',
    version='0.1.0',
    packages=find_packages(),
    description='A simple library for interacting with the Gemini API.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/mindbotapi',  # Replace with your repo URL
    author='Your Name',
    author_email='youremail@example.com',
    license='MIT',
    install_requires=[
        'google-generativeai',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
)