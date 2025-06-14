from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.resistance import Resistance


class Mona(CharacterBase):
    @property
    def name(self) -> str:
        return "Mona"

    @property
    def talent_book(self):
        return Resistance().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Cleansing Heart", "https://genshin-impact.fandom.com/wiki/Cleansing_Heart"),
            source = Source("Rhodeia of Loch", "https://genshin-impact.fandom.com/wiki/Rhodeia_of_Loch")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Ring of Boreas", "https://genshin-impact.fandom.com/wiki/Ring_of_Boreas"),
            source = Source("Wolf of the North Challenge", "https://genshin-impact.fandom.com/wiki/Wolf_of_the_North_Challenge")
        )

    @property
    def in_current_banner(self):
        """
        TODO: Might remove it if not getting used. Instantiating every character for just fetching couple of them is not efficient.
        """
        return False
