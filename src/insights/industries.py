from typing import Dict, List

from .jobs import read


def get_unique_industries(path: str) -> List[str]:
    filterJobs = set()
    jobsList = read(path)
    for jobs in jobsList:
        if jobs['industry'] != '':
            filterJobs.add(jobs['industry'])
    return filterJobs


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    jobFilterIndustry = []
    for job in jobs:
        if job['industry'] == industry:
            jobFilterIndustry.append(job)
    return jobFilterIndustry
