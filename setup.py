import setuptools

setuptools.setup(
    name="en",
    version=open("en/version").read().strip(),
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
