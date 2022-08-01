import json
import enum
import random
import requests

from datetime import datetime
from typing import Dict, TypedDict, Union, List

PROBLEM_URL = 'https://leetcode.com/problems/'
GET_PROBLEMS_URL = 'https://leetcode.com/api/problems/algorithms/'
# flake8: noqa
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'


class ProblemDifficulty(enum.Enum):
    Easy = 1
    Medium = 2
    Hard = 3


class LeetcodeStat(TypedDict):
    question_id: str
    question__article__live: Union[str, None]
    question__article__slug: Union[str, None]
    question__article__has_video_solution: Union[str, None]
    question__title: str
    question__title_slug: str
    question__hide: bool
    total_acs: int
    total_submitted: int
    frontend_question_id: int
    is_new_question: bool


class LeetcodeProblem(TypedDict):
    stat: LeetcodeStat
    status: Union[str, None]
    difficulty: Dict[str, ProblemDifficulty]
    paid_only: bool
    is_favor: bool
    frequency: int
    progress: int


class LeetcodeAPIResponse(TypedDict):
    user_name: str
    num_solved: int
    num_total: int
    ac_easy: int
    ac_medium: int
    ac_hard: int
    stat_status_pairs: List[LeetcodeProblem]
    frequency_high: int
    frequency_mid: int
    category_slug: str


class LeetcodeProblemInfo(TypedDict):
    url: str
    question_id: int
    question__title: str
    total_acceptance: int
    total_submitted: int
    difficulty: ProblemDifficulty


def getAllProblems(useDownloaded: bool = False) -> List[LeetcodeProblemInfo]:
    """
        Get all problems from leetcode, then format them into a readable list of dicts.
    """
    if useDownloaded:
        with open('problems.json', 'r') as f:
            problems = json.load(f)
    else:
        problems: LeetcodeAPIResponse = requests.get(GET_PROBLEMS_URL, headers={
            'User-Agent': USER_AGENT
        }).json()

    # Format the problems
    problemsFormatted: List[LeetcodeProblemInfo] = []
    for problem in problems['stat_status_pairs']:
        # Only get the free problems
        if problem['paid_only']:
            continue

        problemsFormatted.append({
            'url': PROBLEM_URL + problem['stat']['question__title_slug'],
            'question_id': problem['stat']['question_id'],
            'question__title': problem['stat']['question__title'],
            'total_acceptance': problem['stat']['total_acs'],
            'total_submitted': problem['stat']['total_submitted'],
            'difficulty': ProblemDifficulty(problem['difficulty']['level']),  # Convert to enum
        })

    return problemsFormatted


def getRandomProblem(difficulty: ProblemDifficulty = None, useDownloaded: bool = False) -> LeetcodeProblemInfo:
    # Select random difficulty if not specified
    if not difficulty:
        curDay = datetime.today().weekday()
        # Monday is 0, Sunday is 6
        if curDay in [0, 2]:
            difficulty = ProblemDifficulty.Easy
        elif curDay in [1, 3, 4, 6]:
            difficulty = ProblemDifficulty.Medium
        else:
            difficulty = ProblemDifficulty.Hard

    problems = getAllProblems(useDownloaded)
    filteredProblems = [problem for problem in problems if problem['difficulty'] == difficulty]
    return random.choice(filteredProblems)


if __name__ == '__main__':
    print(getRandomProblem())
