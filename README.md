# UVIC-BCSWAN API
UVIC-BCSWAN API read and store SWAN results (third-generation wave model) from/to AWS S3. 

## Installation
#### Using pip
```bash
git clone https://github.com/meracan/s3-netcdf.git
pip install ./s3-netcdf
git clone https://github.com/meracan/netcdf-swan.git
pip install ./netcdf-swan
```

#### Using conda env
```bash
conda create -n polar python=3.8
conda activate polar
git clone https://github.com/meracan/s3-netcdf.git
pip install -e ./s3-netcdf
git clone https://github.com/meracan/s3-netcdf-slf.git
pip install -e ./s3-netcdf-slf
```

## Usage





## Doc and development
[Docs](doc/README.md)

## AWS S3 Credentials
Credentials (for example), `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_DEFAULT_REGION` needs to be save in environment variables. 
For more information, check [link](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html).
Please contact `{name}`

### Data License
[License](LICENSE)

### Code License
[License](LICENSE)