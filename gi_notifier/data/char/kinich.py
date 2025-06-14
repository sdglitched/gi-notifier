from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.kindling import Kindling


class Kinich(CharacterBase):
    @property
    def name(self) -> str:
        return "Kinich"

    @property
    def talent_book(self):
        return Kindling().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Lightning Prism", "https://genshin-impact.fandom.com/wiki/Lightning_Prism"),
            source = Source("Electro Hypostasis", "https://genshin-impact.fandom.com/wiki/Electro_Hypostasis")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Denial and Judgment", "https://genshin-impact.fandom.com/wiki/Denial_and_Judgment"),
            source = Source("The Knave", "https://genshin-impact.fandom.com/wiki/The_Knave")
        )

    @property
    def in_current_banner(self):
        """
        TODO: Might remove it if not getting used. Instantiating every character for just fetching couple of them is not efficient.
        """
        return False
