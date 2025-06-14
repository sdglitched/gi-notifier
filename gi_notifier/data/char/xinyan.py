from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.gold import Gold


class Xinyan(CharacterBase):
    @property
    def name(self) -> str:
        return "Xinyan"

    @property
    def talent_book(self):
        return Gold().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Everflame Seed", "https://genshin-impact.fandom.com/wiki/Everflame_Seed"),
            source = Source("Pyro Regisvine", "https://genshin-impact.fandom.com/wiki/Pyro_Regisvine")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Tusk of Monoceros Caeli", "https://genshin-impact.fandom.com/wiki/Tusk_of_Monoceros_Caeli"),
            source = Source("Enter the Golden House", "https://genshin-impact.fandom.com/wiki/Enter_the_Golden_House")
        )

    @property
    def in_current_banner(self):
        """
        TODO: Might remove it if not getting used. Instantiating every character for just fetching couple of them is not efficient.
        """
        return False
