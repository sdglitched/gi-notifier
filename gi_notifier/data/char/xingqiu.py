from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.gold import Gold


class Xingqiu(CharacterBase):
    @property
    def name(self) -> str:
        return "Xingqiu"

    @property
    def talent_book(self):
        return Gold().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Cleansing Heart", "https://genshin-impact.fandom.com/wiki/Cleansing_Heart"),
            source = Source("Rhodeia of Loch", "https://genshin-impact.fandom.com/wiki/Rhodeia_of_Loch")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Tail of Boreas", "https://genshin-impact.fandom.com/wiki/Tail_of_Boreas"),
            source = Source("Andrius", "https://genshin-impact.fandom.com/wiki/Andrius")
        )

    @property
    def in_current_banner(self):
        """
        TODO: Might remove it if not getting used. Instantiating every character for just fetching couple of them is not efficient.
        """
        return False
