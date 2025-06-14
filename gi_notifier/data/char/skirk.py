from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.contention import Contention


class Skirk(CharacterBase):
    @property
    def name(self) -> str:
        return "Skirk"

    @property
    def talent_book(self):
        return Contention().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Ensnaring Gaze", "https://genshin-impact.fandom.com/wiki/Ensnaring_Gaze"),
            source = Source("Tenebrous Papilla", "https://genshin-impact.fandom.com/wiki/Tenebrous_Papilla")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Ascended Sample: Knight", "https://genshin-impact.fandom.com/wiki/Ascended_Sample:_Knight"),
            source = Source("Unresolved Chess Game", "https://genshin-impact.fandom.com/wiki/Unresolved_Chess_Game")
        )

    @property
    def in_current_banner(self):
        return True
