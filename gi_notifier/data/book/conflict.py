from ...models.base import MaterialGroupBase
from ...models.models import Drop, Item, Source, Weekday


class Conflict(MaterialGroupBase):
    @property
    def drop(self) -> Drop:
        return Drop(
            item=Item("Conflict Books", "https://genshin-impact.fandom.com/wiki/Conflict_Book"),
            source=Source("Blazing Ruins", "https://genshin-impact.fandom.com/wiki/Blazing_Ruins")
        )

    @property
    def available_on(self) -> list[Weekday]:
        return [Weekday.WED, Weekday.SAT, Weekday.SUN]
