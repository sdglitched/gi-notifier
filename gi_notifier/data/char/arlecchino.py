from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.order import Order


class Arlecchino(CharacterBase):
    @property
    def name(self) -> str:
        return "Arlecchino"

    @property
    def talent_book(self):
        return Order().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Fragment of a Golden Melody", "https://genshin-impact.fandom.com/wiki/Fragment_of_a_Golden_Melody"),
            source = Source('"Statue of Marble and Brass"', 'https://genshin-impact.fandom.com/wiki/"Statue of Marble and Brass"')
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Fading Candle", "https://genshin-impact.fandom.com/wiki/Fading_Candle"),
            source = Source("The Knave", "https://genshin-impact.fandom.com/wiki/The_Knave")
        )

    @property
    def in_current_banner(self):
        """
        TODO: Might remove it if not getting used. Instantiating every character for just fetching couple of them is not efficient.
        """
        return False
