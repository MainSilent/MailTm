import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MailTm",
    version="0.0.7",
    author="MainSilent",
    description="Temporary Email",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=['mail', 'email', 'temporary mail', 'temporary email', 'mailtm'],
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
    install_requires=['requests']
)
