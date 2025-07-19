from setuptools import find_packages, setup

setup(
    name="dagproj",
    packages=find_packages(exclude=["dagproj_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
