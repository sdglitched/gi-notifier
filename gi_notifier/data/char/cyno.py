from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.admonition import Admonition


class Cyno(CharacterBase):
    @property
    def name(self) -> str:
        return "Cyno"

    @property
    def talent_book(self):
        return Admonition().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Thunderclap Fruitcore", "https://genshin-impact.fandom.com/wiki/Thunderclap_Fruitcore"),
            source = Source("Electro Regisvines", "https://genshin-impact.fandom.com/wiki/Electro_Regisvines")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Mudra of the Malefic General", "https://genshin-impact.fandom.com/wiki/Mudra_of_the_Malefic_General"),
            source = Source("End of the Oneiric Euthymia", "https://genshin-impact.fandom.com/wiki/End_of_the_Oneiric_Euthymia")
        )

    @property
    def in_current_banner(self):
        """
        TODO: Might remove it if not getting used. Instantiating every character for just fetching couple of them is not efficient.
        """
        return False
