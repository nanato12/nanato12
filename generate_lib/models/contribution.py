from __future__ import annotations

from dataclasses import dataclass
from urllib.parse import ParseResult, urlencode

from generate_lib.models import BaseModel


@dataclass
class Contribution(BaseModel):
    username: str
    repository: str

    @property
    def author_pr_url(self) -> str:
        params = {"q": "is:pr is:closed author:nanato12"}

        return ParseResult(
            scheme="https",
            netloc="github.com",
            path=f"{self.username}/{self.repository}/pulls",
            query=urlencode(params),
            fragment="",
            params="",
        ).geturl()
