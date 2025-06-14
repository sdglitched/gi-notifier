from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.conflict import Conflict


class Chasca(CharacterBase):
    @property
    def name(self) -> str:
        return "Chasca"

    @property
    def talent_book(self):
        return Conflict().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Ensnaring Gaze", "https://genshin-impact.fandom.com/wiki/Ensnaring_Gaze"),
            source = Source("Tenebrous Papilla", "https://genshin-impact.fandom.com/wiki/Tenebrous_Papilla")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Silken Feather", "https://genshin-impact.fandom.com/wiki/Silken_Feather"),
            source = Source("The Knave", "https://genshin-impact.fandom.com/wiki/The_Knave")
        )

    @property
    def in_current_banner(self):
        """
        TODO: Might remove it if not getting used. Instantiating every character for just fetching couple of them is not efficient.
        """
        return False
