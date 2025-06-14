from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.justice import Justice


class Clorinde(CharacterBase):
    @property
    def name(self) -> str:
        return "Clorinde"

    @property
    def talent_book(self):
        return Justice().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Fontemer Unihorn", "https://genshin-impact.fandom.com/wiki/Fontemer_Unihorn"),
            source = Source("Millennial Pearl Seahorse", "https://genshin-impact.fandom.com/wiki/Millennial_Pearl_Seahorse")
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
