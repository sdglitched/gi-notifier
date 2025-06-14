from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.resistance import Resistance


class Noelle(CharacterBase):
    @property
    def name(self) -> str:
        return "Noelle"

    @property
    def talent_book(self):
        return Resistance().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Basalt Pillar", "https://genshin-impact.fandom.com/wiki/Basalt_Pillar"),
            source = Source("Geo Hypostasis", "https://genshin-impact.fandom.com/wiki/Geo_Hypostasis")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Dvalin's Claw", "http://genshin-impact.fandom.com/wiki/Dvalin's_Claw"),
            source = Source("Confront Stormterror", "https://genshin-impact.fandom.com/wiki/Confront_Stormterror")
        )

    @property
    def in_current_banner(self):
        """
        TODO: Might remove it if not getting used. Instantiating every character for just fetching couple of them is not efficient.
        """
        return False
