from __future__ import annotations

from dataclasses import dataclass

from mdutils.mdutils import MdUtils

from generate_lib.models import BaseModel


@dataclass
class Budge(BaseModel):
    alt: str
    icon_url: str
    destination: str

    @property
    def markdown(self) -> str:
        m = MdUtils("")

        return m.new_inline_link(  # type: ignore [no-any-return]
            self.destination, m.new_inline_image(self.alt, self.icon_url)
        )
