from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.order import Order


class Wriothesley(CharacterBase):
    @property
    def name(self) -> str:
        return "Wriothesley"

    @property
    def talent_book(self):
        return Order().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item('"Tourbillon Device"', 'https://genshin-impact.fandom.com/wiki/"Tourbillon_Device"'),
            source = Source("Prototype Cal. Breguet", "https://genshin-impact.fandom.com/wiki/Prototype_Cal._Breguet")
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
