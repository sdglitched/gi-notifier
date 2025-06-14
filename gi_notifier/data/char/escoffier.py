from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.justice import Justice


class Escoffier(CharacterBase):
    @property
    def name(self) -> str:
        return "Escoffier"

    @property
    def talent_book(self):
        return Justice().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Secret Source Airflow Accumulator", "https://genshin-impact.fandom.com/wiki/Secret_Source_Airflow_Accumulator"),
            source = Source("Secret Source Automaton: Overseer Device", "https://genshin-impact.fandom.com/wiki/Secret_Source_Automaton:_Overseer_Device")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Eroded Horn", "https://genshin-impact.fandom.com/wiki/Eroded_Horn"),
            source = Source("Stone Stele Records", "https://genshin-impact.fandom.com/wiki/Stone_Stele_Records")
        )

    @property
    def in_current_banner(self):
        return True
