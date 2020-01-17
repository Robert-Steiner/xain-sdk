import os.path
import sys

from setuptools import find_packages, setup

if sys.version_info < (3, 6):
    sys.exit("Please use Python version 3.6 or higher.")

project_dir = os.path.dirname(os.path.abspath(__file__))
version_file_path = os.path.join(project_dir, "xain_sdk/__version__.py")
readme_file_path = os.path.join(project_dir, "README.md")

# get version
version = {}
with open(version_file_path) as fp:
    exec(fp.read(), version)


# get readme
with open(readme_file_path, "r") as fp:
    readme = fp.read()

# License comments according to `pip-licenses`

install_requires = [
    "typing-extensions~=3.7",  # PSF
    "numpy~=1.15",  # BSD
    "grpcio~=1.23",  # Apache License 2.0
    "numproto~=0.3",  # Apache License 2.0
    "structlog==19.1.0",  # Apache License 2.0 & MIT License
    # TODO: change xain-proto requirement to "xain-proto==0.2.0" once it is released
    "xain-proto @ git+https://github.com/xainag/xain-proto.git@c78e86584c205fb56b5c1f03f052e0b623dcd25d#egg=xain_proto-0.1.0&subdirectory=python",  # Apache License 2.0
]

dev_require = [
    "black==19.10b0",  # MIT
    "mypy==0.740",  # MIT License
    "pylint==2.3.1",  # GPL
    "astroid<=2.2.5",  # LGPL
    "isort==4.3.20",  # MIT
    "pip-licenses==1.15.2",  # MIT License
    "twine==2.0.0",  # Apache License 2.0
    "wheel==0.33.6",  # MIT
]

tests_require = [
    "pytest==4.6.2",  # MIT license
    "pytest-cov==2.7.1",  # MIT
    "pytest-watch==4.2.0",  # MIT
]

docs_require = [
    "Sphinx==2.2.1",
    "m2r==0.2.1",
]

setup(
    name="xain-sdk",
    version=version["__version__"],
    description="XAIN is an open source framework for federated learning.",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/xainag/xain-sdk",
    author=["XAIN AG"],
    author_email="services@xain.io",
    license="Apache License Version 2.0",
    zip_safe=False,
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
    ],
    packages=find_packages(exclude=["tests"]),
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        "test": tests_require,
        "docs": docs_require,
        "dev": dev_require + tests_require + docs_require,
    },
)
