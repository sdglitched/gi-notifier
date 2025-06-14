from ...models.base import MaterialGroupBase
from ...models.models import Drop, Item, Source, Weekday


class Ballad(MaterialGroupBase):
    @property
    def drop(self) -> Drop:
        return Drop(
            item=Item("Ballad Books", "https://genshin-impact.fandom.com/wiki/Ballad_Book"),
            source=Source("Forsaken Rift", "https://genshin-impact.fandom.com/wiki/Forsaken_Rift")
        )

    @property
    def available_on(self) -> list[Weekday]:
        return [Weekday.WED, Weekday.SAT, Weekday.SUN]
