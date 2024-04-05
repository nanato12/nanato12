from __future__ import annotations

from dataclasses import dataclass

from mdutils.mdutils import MdUtils

from generate_lib.models import BaseModel


@dataclass
class Summary(BaseModel):
    url: str

    @property
    def markdown(self) -> str:
        m = MdUtils("")

        return m.new_inline_image(self.url, self.url)  # type: ignore [no-any-return]
