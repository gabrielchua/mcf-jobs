"""
pull_mcf_jobs.py 
"""
import os
import sys
import csv
import time
from typing import List, Dict

import requests
from tqdm import tqdm

BASE_URL: str = 'https://api.mycareersfuture.gov.sg/v2/jobs/'
LIMIT: int = 100  # Number of items per page
CSV_FILE: str = 'mcf_jobs.csv'

def get_total_pages(total_count: int) -> int:
    """
    Calculate the total number of pages based on the total count and the limit per page.

    Args:
    total_count (int): The total count of items.

    Returns:
    int: The total number of pages.
    """
    return (total_count // LIMIT) + (1 if total_count % LIMIT else 0)

def scrape_job_postings(total_count: int) -> List[Dict]:
    """
    Scrape job postings from the MCF API.

    Args:
    total_count (int): The total count of job postings.

    Returns:
    List[Dict]: A list of dictionaries containing the scraped job postings.
    """
    total_pages = get_total_pages(total_count)
    all_data = []

    for page_num in tqdm(range(total_pages), desc="Scraping job postings"):
        url = f"{BASE_URL}?limit={LIMIT}&offset={page_num * LIMIT}"
        response = requests.get(url)
        response.raise_for_status()
        data_page = response.json()['results']
        all_data.extend(data_page)
        time.sleep(1)  # Simulating a delay for demonstration purposes

    return all_data

def write_to_csv(data: List[Dict]) -> None:
    """
    Write the scraped job postings to a CSV file.

    Args:
    data (List[Dict]): A list of dictionaries containing the job postings data.
    """
    if data and isinstance(data[0], dict):
        with open(CSV_FILE, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
            print(f"Data written to {CSV_FILE}")
    else:
        print("No data to write or data is not in expected format.")

def print_usage():
    """
    Print usage instructions for the script.
    """
    print("Usage: python pull_mcf_jobs.py -n <number_of_jobs_to_scrape>")
    print("Options:")
    print("  -n             Specify the total count of job postings")
    print("  -h, --help     Show this help message and exit")

if __name__ == "__main__":
    if len(sys.argv) < 3 or sys.argv[1] in ['-h', '--help'] or sys.argv[1] != '-n':
        print_usage()
        sys.exit(0)

    try:
        number_of_jobs = int(sys.argv[2])
    except ValueError:
        print("Invalid total_count argument. Please provide a valid number.")
        sys.exit(1)

    if not os.path.exists('data'):
        os.makedirs('data')

    job_data = scrape_job_postings(number_of_jobs)
    write_to_csv(job_data)
