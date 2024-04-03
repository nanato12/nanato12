import json
from abc import ABC
from typing import Self


class BaseModel(ABC):
    @classmethod
    def from_json_file(cls, json_path: str) -> list[Self]:
        with open(json_path) as f:
            j: list[dict[str, str]] = json.load(f)

        return [cls(**p) for p in j]
