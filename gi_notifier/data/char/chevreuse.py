from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.order import Order


class Chevreuse(CharacterBase):
    @property
    def name(self) -> str:
        return "Chevreuse"

    @property
    def talent_book(self):
        return Order().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Fontemer Unihorn", "https://genshin-impact.fandom.com/wiki/Fontemer_Unihorn"),
            source = Source("Millennial Pearl Seahorse", "https://genshin-impact.fandom.com/wiki/Millennial_Pearl_Seahorse")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Lightless Eye of the Maelstrom", "https://genshin-impact.fandom.com/wiki/Lightless_Eye_of_the_Maelstrom"),
            source = Source("All-Devouring Narwhal", "https://genshin-impact.fandom.com/wiki/All-Devouring_Narwhal")
        )

    @property
    def in_current_banner(self):
        """
        TODO: Might remove it if not getting used. Instantiating every character for just fetching couple of them is not efficient.
        """
        return False
