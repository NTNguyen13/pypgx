from setuptools import setup, find_packages

exec(open("pypgx/version.py").read())

requirements = ["requests>=2", "pandas>=1.0.0", "bs4>=0.0.1",
    "lxml>=4.5.0", "pysam>=0.16.0",]

setup(
    name="pypgx",
    version=__version__,
    author='Seung-been "Steven" Lee',
    author_email="sbstevenlee@gmail.com",
    description="A Python package for pharmacogenomics research",
    long_description=open("README.rst").read(),
    long_description_content_type="text/x-rst",
    url="https://github.com/pypgx/pypgx/",
    packages=find_packages(),
    package_data={
        "pypgx.resources.cpic": ["cpicPairs.csv"],
        "pypgx.resources.sg": [
            "gene_table.txt",
            "phenotype_table.txt",
            "snp_table.txt",
            "star_table.txt",
        ],
        "pypgx.resources.pgkb": ["action_table.txt"],
        "pypgx.resources.r": ["cpa.R", "plotcov.R"],
    },
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    entry_points={"console_scripts": ["pypgx=pypgx.__main__:main"]}
)
