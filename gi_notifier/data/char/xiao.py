from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.prosperity import Prosperity


class Xiao(CharacterBase):
    @property
    def name(self) -> str:
        return "Xiao"

    @property
    def talent_book(self):
        return Prosperity().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item('Juvenile Jade', 'https://genshin-impact.fandom.com/wiki/Juvenile_Jade'),
            source = Source("Primo Geovishap", "https://genshin-impact.fandom.com/wiki/Primo_Geovishap")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Shadow of the Warrior", "https://genshin-impact.fandom.com/wiki/Shadow_of_the_Warrior"),
            source = Source("Enter the Golden House", "https://genshin-impact.fandom.com/wiki/Enter_the_Golden_House")
        )

    @property
    def in_current_banner(self):
        """
        TODO: Might remove it if not getting used. Instantiating every character for just fetching couple of them is not efficient.
        """
        return False
