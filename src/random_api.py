from typing import List

import requests

from .config import settings
from .schemas import Question


class RandomApi:
    def __init__(self, url: str):
        self.url = url

    def get_questions(self, count: int) -> List[Question]:
        response = requests.get(
            url=self.url,
            params={"count": count}
        )

        content = response.json()

        questions = []

        for row in content:
            questions.append(Question(**row))

        return questions


random_api = RandomApi(url=settings.RANDOM_API_URL)
