from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.transience import Transience


class YumemizukiMizuki(CharacterBase):
    @property
    def name(self) -> str:
        return "Yumemizuki Mizuki"

    @property
    def talent_book(self):
        return Transience().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item('Talisman of the Enigmatic Land', 'https://genshin-impact.fandom.com/wiki/Talisman_of_the_Enigmatic_Land'),
            source = Source("Wayward Hermetic Spiritspeaker", "https://genshin-impact.fandom.com/wiki/Wayward_Hermetic_Spiritspeaker")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Fading Candle", "https://genshin-impact.fandom.com/wiki/Fading_Candle"),
            source = Source("The Knave", "https://genshin-impact.fandom.com/wiki/The_Knave")
        )

    @property
    def in_current_banner(self):
        """
        TODO: Might remove it if not getting used. Instantiating every character for just fetching couple of them is not efficient.
        """
        return False
