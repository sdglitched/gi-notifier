from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.ballad import Ballad


class Fischl(CharacterBase):
    @property
    def name(self) -> str:
        return "Fischl"

    @property
    def talent_book(self):
        return Ballad().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Lightning Prism", "https://genshin-impact.fandom.com/wiki/Lightning_Prism"),
            source = Source("Electro Hypostasis", "https://genshin-impact.fandom.com/wiki/Electro_Hypostasis")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Spirit Locket of Boreas", "https://genshin-impact.fandom.com/wiki/Spirit_Locket_of_Boreas"),
            source = Source("Wolf of the North Challenge", "https://genshin-impact.fandom.com/wiki/Wolf_of_the_North_Challenge")
        )

    @property
    def in_current_banner(self):
        """
        TODO: Might remove it if not getting used. Instantiating every character for just fetching couple of them is not efficient.
        """
        return False
