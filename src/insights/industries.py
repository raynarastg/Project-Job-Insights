from typing import List, Dict
from .jobs import read


def get_unique_industries(path: str) -> List[str]:
    filterJobs = set()
    jobsList = read(path)
    for jobs in jobsList:
        if jobs['industry'] != '':
            filterJobs.add(jobs['industry'])
    return filterJobs


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError
