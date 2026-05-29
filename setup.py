from setuptools import setup, find_packages

setup(
    name="unpaste",
    version="0.1.0",
    description="Cross-platform background utility to paste plain text by default",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Femirins",
    url="https://github.com/femirins/unpaste",
    packages=find_packages(),
    install_requires=[
        "pyperclip>=1.8.2",
        "pynput>=1.7.6",
        "click>=8.1.3",
    ],
    entry_points={
        "console_scripts": [
            "unpaste=unpaste.cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
)