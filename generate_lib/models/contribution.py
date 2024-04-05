from __future__ import annotations

from dataclasses import dataclass
from urllib.parse import ParseResult, urlencode, urljoin

from mdutils.mdutils import MdUtils

from generate_lib.models import BaseModel
from generate_lib.url import URL


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

    @property
    def card_url(self) -> str:
        params = {"username": self.username, "repo": self.repository}

        return ParseResult(
            scheme="https",
            netloc="github-readme-stats.vercel.app",
            path="api/pin",
            query=urlencode(params),
            fragment="",
            params="",
        ).geturl()

    @property
    def markdown(self) -> str:
        m = MdUtils("")
        image_md = m.new_inline_image(self.repository, self.card_url)
        return m.new_inline_link(  # type: ignore [no-any-return]
            urljoin(URL.GITHUB_HOST, f"{self.username}/{self.repository}"),
            image_md,
        )
