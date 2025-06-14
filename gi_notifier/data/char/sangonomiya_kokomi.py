from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.transience import Transience


class SangonomiyaKokomi(CharacterBase):
    @property
    def name(self) -> str:
        return "Sangonomiya Kokomi"

    @property
    def talent_book(self):
        return Transience().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Dew of Repudiation", "https://genshin-impact.fandom.com/wiki/Dew_of_Repudiation"),
            source = Source("Hydro Hypostases", "https://genshin-impact.fandom.com/wiki/Hydro_Hypostases")
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
