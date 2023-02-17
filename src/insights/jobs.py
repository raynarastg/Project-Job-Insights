import csv
from functools import lru_cache
from typing import Dict, List


@lru_cache
def read(path: str) -> List[Dict]:
    list = []
    with open(path) as file:
        myFiles = csv.DictReader(file)
        for i in myFiles:
            list.append(i)
    return list


def get_unique_job_types(path: str) -> List[str]:
    jobs = set()
    valuesList = read(path)
    for i in valuesList:
        jobs.add(i['job_type'])
    return jobs


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    jobFilter = []
    for job in jobs:
        if job['job_type'] == job_type:
            jobFilter.append(job)
    return jobFilter
