from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.freedom import Freedom


class Sucrose(CharacterBase):
    @property
    def name(self) -> str:
        return "Sucrose"

    @property
    def talent_book(self):
        return Freedom().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Hurricane Seed", "https://genshin-impact.fandom.com/wiki/Hurricane_Seed"),
            source = Source("Anemo Hypostasis", "https://genshin-impact.fandom.com/wiki/Anemo_Hypostasis")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Spirit Locket of Boreas", "https://genshin-impact.fandom.com/wiki/Spirit_Locket_of_Boreas"),
            source = Source("Andrius", "https://genshin-impact.fandom.com/wiki/Andrius")
        )

    @property
    def in_current_banner(self):
        """
        TODO: Might remove it if not getting used. Instantiating every character for just fetching couple of them is not efficient.
        """
        return False
