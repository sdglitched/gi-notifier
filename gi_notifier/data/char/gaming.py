from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.prosperity import Prosperity


class Gaming(CharacterBase):
    @property
    def name(self) -> str:
        return "Gaming"

    @property
    def talent_book(self):
        return Prosperity().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Emperor's Resolution", "https://genshin-impact.fandom.com/wiki/Emperor's_Resolution"),
            source = Source("Emperor of Fire and Iron", "https://genshin-impact.fandom.com/wiki/Emperor_of_Fire_and_Iron")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Lightless Mass", "https://genshin-impact.fandom.com/wiki/Lightless_Mass"),
            source = Source("All-Devouring Narwhal", "https://genshin-impact.fandom.com/wiki/All-Devouring_Narwhal")
        )

    @property
    def in_current_banner(self):
        """
        TODO: Might remove it if not getting used. Instantiating every character for just fetching couple of them is not efficient.
        """
        return False
