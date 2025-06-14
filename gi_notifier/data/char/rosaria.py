from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.ballad import Ballad


class Rosaria(CharacterBase):
    @property
    def name(self) -> str:
        return "Rosaria"

    @property
    def talent_book(self):
        return Ballad().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Hoarfrost Core", "https://genshin-impact.fandom.com/wiki/Hoarfrost_Core"),
            source = Source("Cryo Regisvine", "https://genshin-impact.fandom.com/wiki/Cryo_Regisvine")
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
