from setuptools import setup, find_packages

setup(
    name="s3netcdfslf",
    version="1.0.0",
    author="Julien Cousineau",
    author_email="julien.cousineau@gmail.com",
    url="https://github.com/meracan/s3-netcdf-slf",
    packages=["s3netcdfslf"],
    include_package_data=True,
    install_requires=[
        'scipy',
        'numpy',
        'netcdf4',
        'tqdm'
    ],
    python_requires='>=3.6',
)
