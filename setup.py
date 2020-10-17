import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cubeviz",  # Replace with your own username
    version="0.0.2",
    author="Jurgen Hanekom",
    author_email="jhanekom27@gmail.com",
    description="Package for VizCube App",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/jhanekom27/cube_viz",
    # package_dir={"": "src"},
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    extras_require={  # Optional
        # 'dev': ['check-manifest'],
        "test": ["coverage"],
    },
)
