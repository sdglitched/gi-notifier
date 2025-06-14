from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.prosperity import Prosperity


class Qiqi(CharacterBase):
    @property
    def name(self) -> str:
        return "Qiqi"

    @property
    def talent_book(self):
        return Prosperity().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Hoarfrost Core", "https://genshin-impact.fandom.com/wiki/Hoarfrost_Core"),
            source = Source("Cryo Regisvine", "https://genshin-impact.fandom.com/wiki/Cryo_Regisvine")
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
