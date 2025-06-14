from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.transience import Transience


class Kirara(CharacterBase):
    @property
    def name(self) -> str:
        return "Kirara"

    @property
    def talent_book(self):
        return Transience().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Evergloom Ring", "https://genshin-impact.fandom.com/wiki/Evergloom_Ring"),
            source = Source("Iniquitous Baptist", "https://genshin-impact.fandom.com/wiki/Iniquitous_Baptist")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Everamber", "https://genshin-impact.fandom.com/wiki/Everamber"),
            source = Source("The Realm of Beginnings", "https://genshin-impact.fandom.com/wiki/The_Realm_of_Beginnings")
        )

    @property
    def in_current_banner(self):
        """
        TODO: Might remove it if not getting used. Instantiating every character for just fetching couple of them is not efficient.
        """
        return False
