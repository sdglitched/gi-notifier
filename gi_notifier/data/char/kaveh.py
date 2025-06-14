from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.ingenuity import Ingenuity


class Kaveh(CharacterBase):
    @property
    def name(self) -> str:
        return "Kaveh"

    @property
    def talent_book(self):
        return Ingenuity().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Quelled Creeper", "https://genshin-impact.fandom.com/wiki/Quelled_Creeper"),
            source = Source("Dendro Hypostasis", "https://genshin-impact.fandom.com/wiki/Dendro_Hypostasis")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Primordial Greenbloom", "https://genshin-impact.fandom.com/wiki/Primordial_Greenbloom"),
            source = Source("The Realm of Beginnings", "https://genshin-impact.fandom.com/wiki/The_Realm_of_Beginnings")
        )

    @property
    def in_current_banner(self):
        """
        TODO: Might remove it if not getting used. Instantiating every character for just fetching couple of them is not efficient.
        """
        return False
