from setuptools import setup

setup(
    name="coffee_katas",
    description="Some fun exercises to improve my skillz.",
    version=0.1,
    author="Victor Benavente",
    author_email="vbenavente@hotmail.com",
    license="MIT",
    py_modules=["linked_list"],
    package_dir={"": "src"},
    install_requires=[],
    extras_requires={"test": ["pytest", "pytest-watch", "pytest-cov", "tox"]},
    entry_points={
        "console_scripts": [
        ]
    }
)
