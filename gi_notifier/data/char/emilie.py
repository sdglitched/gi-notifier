from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.order import Order


class Emilie(CharacterBase):
    @property
    def name(self) -> str:
        return "Emilie"

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
            item = Item("Silken Feather", "https://genshin-impact.fandom.com/wiki/Silken_Feather"),
            source = Source("The Knave", "https://genshin-impact.fandom.com/wiki/The_Knave")
        )

    @property
    def in_current_banner(self):
        """
        TODO: Might remove it if not getting used. Instantiating every character for just fetching couple of them is not efficient.
        """
        return False
