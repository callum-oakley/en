from setuptools import setup

setup(
    name="en",
    version="0.3",
    description="Utility for organising notes.",
    url="http://github.com/hot-leaf-juice/en",
    author="Callum Oakley",
    author_email="c.oakley108@gmail.com",
    license="MIT",
    packages=["en"],
    entry_points={
        "console_scripts": ["en=en.cmd:main"]
    },
    zip_safe=True
)
