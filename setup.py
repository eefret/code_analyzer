from setuptools import setup, find_packages

setup(
    name="code-analyzer",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "openai",
    ],
    entry_points={
        "console_scripts": [
            'code-analyzer=code_analyzer.analyze:main',
        ],
    },
)
