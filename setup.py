from setuptools import setup

setup(
    name="notes",
    version="0.1",
    description="Utility for organising notes.",
    url="http://github.com/hot-leaf-juice/notes",
    author="Callum Oakley",
    author_email="c.oakley108@gmail.com",
    license="MIT",
    packages=["notes"],
    entry_points={
        "console_scripts": ["notes=notes.cmd:main"]
    },
    zip_safe=False
)
