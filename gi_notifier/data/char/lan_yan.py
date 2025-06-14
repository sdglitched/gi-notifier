from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.diligence import Diligence


class LanYan(CharacterBase):
    @property
    def name(self) -> str:
        return "Lan Yan"

    @property
    def talent_book(self):
        return Diligence().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Gold-Inscribed Secret Source Core", "https://genshin-impact.fandom.com/wiki/Gold-Inscribed_Secret_Source_Core"),
            source = Source("Secret Source Automaton: Configuration Device", "https://genshin-impact.fandom.com/wiki/Secret_Source_Automaton:_Configuration_Device")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Eroded Sunfire", "https://genshin-impact.fandom.com/wiki/Eroded_Sunfire"),
            source = Source("Stone Stele Records", "https://genshin-impact.fandom.com/wiki/Stone_Stele_Records")
        )

    @property
    def in_current_banner(self):
        """
        TODO: Might remove it if not getting used. Instantiating every character for just fetching couple of them is not efficient.
        """
        return False
