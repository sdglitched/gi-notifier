from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.ballad import Ballad


class Venti(CharacterBase):
    @property
    def name(self) -> str:
        return "Venti"

    @property
    def talent_book(self):
        return Ballad().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Hurricane Seed", "https://genshin-impact.fandom.com/wiki/Hurricane_Seed"),
            source = Source("Anemo Hypostasis", "https://genshin-impact.fandom.com/wiki/Anemo_Hypostasis")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Tail of Boreas", "https://genshin-impact.fandom.com/wiki/Tail_of_Boreas"),
            source = Source("Andrius", "https://genshin-impact.fandom.com/wiki/Andrius")
        )

    @property
    def in_current_banner(self):
        """
        TODO: Might remove it if not getting used. Instantiating every character for just fetching couple of them is not efficient.
        """
        return False
