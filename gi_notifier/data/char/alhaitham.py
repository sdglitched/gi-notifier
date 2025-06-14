from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.ingenuity import Ingenuity


class Alhaitham(CharacterBase):
    @property
    def name(self) -> str:
        return "Alhaitham"

    @property
    def talent_book(self):
        return Ingenuity().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Pseudo-Stamens", "https://genshin-impact.fandom.com/wiki/Pseudo-Stamens"),
            source = Source("Setekh Wenut", "https://genshin-impact.fandom.com/wiki/Setekh_Wenut")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Mirror of Mushin", "https://genshin-impact.fandom.com/wiki/Mirror_of_Mushin"),
            source = Source("Joururi Workshop", "https://genshin-impact.fandom.com/wiki/Joururi_Workshop")
        )

    @property
    def in_current_banner(self):
        """
        TODO: Might remove it if not getting used. Instantiating every character for just fetching couple of them is not efficient.
        """
        return False
