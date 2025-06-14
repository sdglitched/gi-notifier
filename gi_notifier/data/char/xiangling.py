from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.diligence import Diligence


class Xiangling(CharacterBase):
    @property
    def name(self) -> str:
        return "Xiangling"

    @property
    def talent_book(self):
        return Diligence().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Everflame Seed", "https://genshin-impact.fandom.com/wiki/Everflame_Seed"),
            source = Source("Pyro Regisvine", "https://genshin-impact.fandom.com/wiki/Pyro_Regisvine")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Dvalin's Claw", "http://genshin-impact.fandom.com/wiki/Dvalin's_Claw"),
            source = Source("Confront Stormterror", "https://genshin-impact.fandom.com/wiki/Confront_Stormterror")
        )

    @property
    def in_current_banner(self):
        """
        TODO: Might remove it if not getting used. Instantiating every character for just fetching couple of them is not efficient.
        """
        return False
