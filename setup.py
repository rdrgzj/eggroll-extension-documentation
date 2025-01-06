from setuptools import setup, find_packages

setup(
    name="Eggroll Game",
    version="0.1.0",
    author="Leandro Asunan and Jana Rodriguez",
    description="Guide the eggs 🥚 to the nests 🪹 before you run out of moves. Avoid obstacles like frying pans 🍳.",
    url="https://github.com/rdrgzj/eggroll-extension-documentation",
    classifiers=[
        "Programming Language :: Python :: 3.13",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "sphinx==8.1.3",
        "sphinx-rtd-theme==3.0.2",
    ],
    extras_require={
        'docs': [
            'sphinx',
            'sphinx-rtd-theme',
            'sphinx-autodoc-typehints',
        ],
        'dev': [
            'pyright',
            'termcolor',
            'mypy',
            'pytest',
        ],
    }
)