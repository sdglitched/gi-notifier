from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.equity import Equity


class Lyney(CharacterBase):
    @property
    def name(self) -> str:
        return "Lyney"

    @property
    def talent_book(self):
        return Equity().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Emperor's Resolution", "https://genshin-impact.fandom.com/wiki/Emperor's_Resolution"),
            source = Source("Emperor of Fire and Iron", "https://genshin-impact.fandom.com/wiki/Emperor_of_Fire_and_Iron")
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
