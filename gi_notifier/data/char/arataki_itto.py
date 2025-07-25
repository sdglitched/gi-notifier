from urllib.parse import quote

from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.elegance import Elegance


class AratakiItto(CharacterBase):
    @property
    def name(self) -> str:
        return "Arataki Itto"

    @property
    def talent_book(self):
        return Elegance().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item=Item(
                "Riftborn Regalia",
                f"https://genshin-impact.fandom.com/wiki/{quote("Riftborn_Regalia")}",
            ),
            source=Source(
                "Golden Wolflord",
                f"https://genshin-impact.fandom.com/wiki/{quote("Golden_Wolflord")}",
            ),
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item=Item(
                "Ashen Heart",
                f"https://genshin-impact.fandom.com/wiki/{quote("Ashen_Heart")}",
            ),
            source=Source(
                "Narukami Island: Tenshukaku",
                f"https://genshin-impact.fandom.com/wiki/{quote("Narukami_Island:_Tenshukaku")}",
            ),
        )
