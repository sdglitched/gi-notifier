from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.elegance import Elegance


class KamisatoAyato(CharacterBase):
    @property
    def name(self) -> str:
        return "Kamisato Ayato"

    @property
    def talent_book(self):
        return Elegance().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Dew of Repudiation", "https://genshin-impact.fandom.com/wiki/Dew_of_Repudiation"),
            source = Source("Hydro Hypostases", "https://genshin-impact.fandom.com/wiki/Hydro_Hypostases")
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
