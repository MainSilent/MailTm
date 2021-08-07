import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Mail Tm",
    version="0.0.1",
    author="MainSilent",
    description="Temporary Email",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MainSilent/MailTm",
    project_urls={
        "Bug Tracker": "https://github.com/MainSilent/MailTm/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)