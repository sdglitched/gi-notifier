from ...models.base import CharacterBase
from ...models.models import Drop, Item, Source
from ..book.light import Light


class Chiori(CharacterBase):
    @property
    def name(self) -> str:
        return "Chiori"

    @property
    def talent_book(self):
        return Light().as_material_group()

    @property
    def normal_boss_drop(self):
        return Drop(
            item = Item("Artificed Spare Clockwork Component — Coppelia", "https://genshin-impact.fandom.com/wiki/Artificed_Spare_Clockwork_Component_—_Coppelia"),
            source = Source("Icewind Suite: Dirge of Coppelia", "https://genshin-impact.fandom.com/wiki/Icewind_Suite:_Dirge_of_Coppelia")
        )

    @property
    def weekly_boss_drop(self):
        return Drop(
            item = Item("Lightless Silk String", "https://genshin-impact.fandom.com/wiki/Lightless_Silk_String"),
            source = Source("All-Devouring Narwhal", "https://genshin-impact.fandom.com/wiki/All-Devouring_Narwhal")
        )

    @property
    def in_current_banner(self):
        """
        TODO: Might remove it if not getting used. Instantiating every character for just fetching couple of them is not efficient.
        """
        return False
