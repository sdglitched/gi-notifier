from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.conflict import Conflict


class Varesa(CharacterBase):
    @property
    def name(self) -> str:
        return "Varesa"

    @property
    def talent_book(self):
        return Conflict().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Sparkless Statue Core", "https://genshin-impact.fandom.com/wiki/Sparkless_Statue_Core"),
            source = Source("Lava Dragon Statue", "https://genshin-impact.fandom.com/wiki/Lava_Dragon_Statue")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Eroded Scale-Feather", "https://genshin-impact.fandom.com/wiki/Eroded_Scale-Feather"),
            source = Source("Lord of Eroded Primal Fire", "https://genshin-impact.fandom.com/wiki/Lord_of_Eroded_Primal_Fire")
        )

    @property
    def in_current_banner(self):
        """
        TODO: Might remove it if not getting used. Instantiating every character for just fetching couple of them is not efficient.
        """
        return False
