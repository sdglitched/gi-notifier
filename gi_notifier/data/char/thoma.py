from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.transience import Transience


class Thoma(CharacterBase):
    @property
    def name(self) -> str:
        return "Thoma"

    @property
    def talent_book(self):
        return Transience().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item('Smoldering Pearl', 'https://genshin-impact.fandom.com/wiki/Smoldering_Pearl'),
            source = Source("Pyro Hypostasis", "https://genshin-impact.fandom.com/wiki/Pyro_Hypostasis")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Hellfire Butterfly", "https://genshin-impact.fandom.com/wiki/Hellfire_Butterfly"),
            source = Source("Narukami Island: Tenshukaku", "https://genshin-impact.fandom.com/wiki/Narukami_Island:_Tenshukaku")
        )

    @property
    def in_current_banner(self):
        """
        TODO: Might remove it if not getting used. Instantiating every character for just fetching couple of them is not efficient.
        """
        return False
