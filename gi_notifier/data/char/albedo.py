from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.ballad import Ballad


class Albedo(CharacterBase):
    @property
    def name(self) -> str:
        return "Albedo"

    @property
    def talent_book(self):
        return Ballad().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Basalt Pillar", "https://genshin-impact.fandom.com/wiki/Basalt_Pillar"),
            source = Source("Geo Hypostasis", "https://genshin-impact.fandom.com/wiki/Geo_Hypostasis")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Tusk of Monoceros Caeli", "https://genshin-impact.fandom.com/wiki/Tusk_of_Monoceros_Caeli"),
            source = Source("Enter the Golden House", "https://genshin-impact.fandom.com/wiki/Enter_the_Golden_House")
        )

    @property
    def in_current_banner(self):
        """
        TODO: Might remove it if not getting used. Instantiating every character for just fetching couple of them is not efficient.
        """
        return False
