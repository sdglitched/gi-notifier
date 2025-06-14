from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.light import Light


class YaeMiko(CharacterBase):
    @property
    def name(self) -> str:
        return "Yae Miko"

    @property
    def talent_book(self):
        return Light().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Dragonheir's False Fin", "https://genshin-impact.fandom.com/wiki/Dragonheir's_False_Fin"),
            source = Source("Coral Defenders", "https://genshin-impact.fandom.com/wiki/Coral_Defenders")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("The Meaning of Aeons", "https://genshin-impact.fandom.com/wiki/The_Meaning_of_Aeons"),
            source = Source("End of the Oneiric Euthymia", "https://genshin-impact.fandom.com/wiki/End_of_the_Oneiric_Euthymia")
        )

    @property
    def in_current_banner(self):
        """
        TODO: Might remove it if not getting used. Instantiating every character for just fetching couple of them is not efficient.
        """
        return False
