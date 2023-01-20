# DESCRIPTION

    This template is can be used to create a dataset of services pricing of Google Cloud Platform
---

## Prerequiste

* Install Python3
* An Api key of pricing from GCP which is to be passed as environemnt value like:

```bash
export API_KEY=AIzaSyD39kaXRm3BTfW8rOCS-IYaVcNFivOfiN0ywd5646
```

## Steps

### 0. Clone the source code from github

```bash
git clone https://github.com/knoldus/gcp_pricing.git
cd gcp_prcing/
```

### 1. create python virtual_env

```bash
python3 -m venv ./venv
source ./venv/bin/activate
```

### 2. install dependencies

```bash
pip3 -r install ./requirements.txt
```

### 3. create the dataset

```bash
python3 pricing.py
```

* Note: First update the services required in code
