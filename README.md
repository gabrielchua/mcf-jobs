# Unofficial MCF Jobs Python Wrapper

## Overview
This is a Python script designed for scraping job postings from the MyCareersFuture (MCF) API. It retrieves data about job listings and outputs the information to a CSV file.

## Features
- Retrieves job postings from the MCF API.
- Supports specifying the number of job postings to scrape.
- Outputs the scraped data to a CSV file for easy analysis and storage.
- Includes error handling to ensure robust scraping performance.

## Requirements
- Python 3
- `requests` library
- `tqdm` library

## Installation
Before running the script, ensure you have Python 3 installed on your system. You also need to install the required libraries. You can install these using pip:

```bash
pip install requests tqdm
```

## Usage
To use the script, navigate to the directory containing pull_mcf_jobs.py and run it from the command line. You need to specify the number of job postings you want to scrape using the -n argument.

```bash
python pull_mcf_jobs.py -n <number_of_jobs_to_scrape>
```

For example, to scrape 500 job postings, use:

```bash
python pull_mcf_jobs.py -n 500
```

## Help
If you need to see usage instructions, run:

```bash
python pull_mcf_jobs.py -h
```