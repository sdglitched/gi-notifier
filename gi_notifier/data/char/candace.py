from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.admonition import Admonition


class Candace(CharacterBase):
    @property
    def name(self) -> str:
        return "Candace"

    @property
    def talent_book(self):
        return Admonition().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Light Guiding Tetrahedron", "https://genshin-impact.fandom.com/wiki/Light_Guiding_Tetrahedron"),
            source = Source("Algorithm of Semi-Intransient Matrix of Overseer Network", "https://genshin-impact.fandom.com/wiki/Algorithm_of_Semi-Intransient_Matrix_of_Overseer_Network")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Tears of the Calamitous God", "https://genshin-impact.fandom.com/wiki/Tears_of_the_Calamitous_God"),
            source = Source("End of the Oneiric Euthymia", "https://genshin-impact.fandom.com/wiki/End_of_the_Oneiric_Euthymia")
        )

    @property
    def in_current_banner(self):
        """
        TODO: Might remove it if not getting used. Instantiating every character for just fetching couple of them is not efficient.
        """
        return False
