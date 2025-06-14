from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.elegance import Elegance


class KujouSara(CharacterBase):
    @property
    def name(self) -> str:
        return "Kujou Sara"

    @property
    def talent_book(self):
        return Elegance().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Storm Beads", "https://genshin-impact.fandom.com/wiki/Storm_Beads"),
            source = Source("Thunder Manifestation", "https://genshin-impact.fandom.com/wiki/Thunder_Manifestation")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Ashen Heart", "https://genshin-impact.fandom.com/wiki/Ashen_Heart"),
            source = Source("Narukami Island: Tenshukaku", "https://genshin-impact.fandom.com/wiki/Narukami_Island:_Tenshukaku")
        )

    @property
    def in_current_banner(self):
        """
        TODO: Might remove it if not getting used. Instantiating every character for just fetching couple of them is not efficient.
        """
        return False
