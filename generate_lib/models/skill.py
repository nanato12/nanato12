from __future__ import annotations

import json
from dataclasses import dataclass
from urllib.parse import urljoin

from yattag import Doc

DEFAULT_ICON_HOST = (
    "https://raw.githubusercontent.com/devicons/devicon/master/icons/"
)


@dataclass
class Skill:
    name: str
    path: str
    host: str = DEFAULT_ICON_HOST
    width: str = "40"
    height: str = "40"

    @property
    def icon_url(self) -> str:
        if self.host == DEFAULT_ICON_HOST:
            return urljoin(self.host, f"{self.name}/{self.path}")
        else:
            return urljoin(self.host, self.path)

    @property
    def html_tag(self) -> str:
        doc, _, _ = Doc().tagtext()
        doc.stag(
            "img",
            src=self.icon_url,
            alt=self.name,
            width=self.width,
            height=self.height,
        )
        return doc.getvalue()  # type: ignore [no-any-return]

    @classmethod
    def from_json_file(cls, json_path: str) -> dict[str, list[Skill]]:
        with open(json_path) as f:
            j: dict[str, list[dict[str, str]]] = json.load(f)

        return {k: [cls(**s) for s in v] for k, v in j.items()}
