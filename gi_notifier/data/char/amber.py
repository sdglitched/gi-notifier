from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.freedom import Freedom


class Amber(CharacterBase):
    @property
    def name(self) -> str:
        return "Amber"

    @property
    def talent_book(self):
        return Freedom().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Everflame Seed", "https://genshin-impact.fandom.com/wiki/Everflame_Seed"),
            source = Source("Pyro Regisvines", "https://genshin-impact.fandom.com/wiki/Pyro_Regisvines")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Dvalin's Sigh", "https://genshin-impact.fandom.com/wiki/Dvalin's_Sigh"),
            source = Source("Confront Stormterror", "https://genshin-impact.fandom.com/wiki/Confront_Stormterror")
        )

    @property
    def in_current_banner(self):
        """
        TODO: Might remove it if not getting used. Instantiating every character for just fetching couple of them is not efficient.
        """
        return False
