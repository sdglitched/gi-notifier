from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.equity import Equity


class Neuvillette(CharacterBase):
    @property
    def name(self) -> str:
        return "Neuvillette"

    @property
    def talent_book(self):
        return Equity().as_material_group()

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
