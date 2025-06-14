from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.equity import Equity


class Sigewinne(CharacterBase):
    @property
    def name(self) -> str:
        return "Sigewinne"

    @property
    def talent_book(self):
        return Equity().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Water That Failed To Transcend", "https://genshin-impact.fandom.com/wiki/Water_That_Failed_To_Transcend"),
            source = Source("Hydro Tulpa", "https://genshin-impact.fandom.com/wiki/Hydro_Tulpa")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Lightless Eye of the Maelstrom", "https://genshin-impact.fandom.com/wiki/Lightless_Eye_of_the_Maelstrom"),
            source = Source("All-Devouring Narwhal", "https://genshin-impact.fandom.com/wiki/All-Devouring_Narwhal")
        )

    @property
    def in_current_banner(self):
        """
        TODO: Might remove it if not getting used. Instantiating every character for just fetching couple of them is not efficient.
        """
        return False
