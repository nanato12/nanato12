from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Optional

BADGE_BASE = "https://img.shields.io/badge"


@dataclass
class Skill:
    name: str
    skill_icon: Optional[str] = None
    badge: Optional[dict[str, str]] = field(default=None)

    @property
    def badge_html(self) -> str:
        if not self.badge:
            return ""
        label = self.badge.get("label", self.name).replace(" ", "%20")
        color = self.badge.get("color", "grey")
        logo = self.badge.get("logo", "")
        logo_color = self.badge.get("logoColor", "white")
        url = f"{BADGE_BASE}/-{label}-{color}?style=for-the-badge"
        if logo:
            url += f"&logo={logo}&logoColor={logo_color}"
        return f'<img src="{url}" alt="{self.name}" height="32" />'

    @classmethod
    def from_json_file(cls, json_path: str) -> dict[str, list[Skill]]:
        with open(json_path) as f:
            j: dict[str, list[dict[str, object]]] = json.load(f)

        return {k: [cls(**s) for s in v] for k, v in j.items()}  # type: ignore[arg-type]
