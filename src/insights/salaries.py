from typing import Dict, List, Union

from .jobs import read


def get_max_salary(path: str) -> int:
    jobs = read(path)
    listMaxSalaries = []
    for job in jobs:
        if job['max_salary'].isnumeric():
            listMaxSalaries.append(int(job['max_salary']))

    return max(listMaxSalaries)


def get_min_salary(path: str) -> int:
    jobs = read(path)
    listMinSalaries = []
    for job in jobs:
        if job['min_salary'].isnumeric():
            listMinSalaries.append(int(job['min_salary']))

    return min(listMinSalaries)


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        int(salary)
        min_salary, max_salary = job['min_salary'], job['max_salary']
        if int(min_salary) > int(max_salary):
            raise ValueError('min_salary > max_salary')
    except Exception:
        raise ValueError
    return int(salary) >= int(min_salary) and int(salary) <= int(max_salary)


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    salariesJob = []
    try:
        int(salary)
        for job in jobs:
            min_salary, max_salary = job['min_salary'], job['max_salary']
            if int(min_salary) <= int(salary) <= int(max_salary):
                salariesJob.append(job)
    except Exception:
        ValueError

    return salariesJob
