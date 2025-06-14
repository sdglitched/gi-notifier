from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.prosperity import Prosperity


class Shenhe(CharacterBase):
    @property
    def name(self) -> str:
        return "Shenhe"

    @property
    def talent_book(self):
        return Prosperity().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Dragonheir's False Fin", "https://genshin-impact.fandom.com/wiki/Dragonheir's_False_Fin"),
            source = Source("Coral Defenders", "https://genshin-impact.fandom.com/wiki/Coral_Defenders")
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
