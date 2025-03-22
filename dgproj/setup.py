from setuptools import find_packages, setup

setup(
    name="dgproj",
    packages=find_packages(exclude=["dgproj_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
