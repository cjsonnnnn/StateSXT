import setuptools

with open("README.md", encoding="utf8") as file:
    LONG_DESC = file.read()

setuptools.setup(
    name="statesxt",
    version="0.1.2",
    description="A project template for testing your website application.",
    long_description=LONG_DESC,
    long_description_content_type="text/markdown",
    url="https://test.pypi.org/project/statesxt/",
    author="Jason Caleb",
    author_email="cjsonnnnn@gmail.com",
    license="MIT License",
    project_urls={
        "Source": "https://github.com/jsonnnnn/statesxt",
        "Documentation": "https://statesxt.readthedocs.io/en/latest/"
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        "Framework :: Pytest",
        "Intended Audience :: Developers",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Topic :: Software Development :: Testing",
        "Topic :: Utilities",
    ],
    entry_points={
        "console_scripts": [
            "statesxt=statesxt.main:main",
        ],
    },
    keywords=[
        "Selenium",
        "Pytest",
        "Python",
        "project template",
        "template",
        "Testing",
        "Framework",
    ],
    python_requires=">=3.10, <3.12",
    install_requires=[
        "cryptography==41.0.4",
        "faker==19.11.0",
        "google-api-python-client==2.104.0",
        "gspread==5.11.3",
        "pandas==2.1.1",
        "pip-autoremove==0.10.0",
        "psycopg2==2.9.9",
        "pytest==7.4.2",
        "python-dotenv==1.0.0",
        "selenium==4.14.0",
        "selenium-wire==5.1.0",
        "softest==1.2.0.0",
        "sshtunnel==0.4.0",
        "webdriver-manager==4.0.1",
    ],
    packages=setuptools.find_packages(),
    include_package_data=True,
    setup_requires=["setuptools-git"],
)
