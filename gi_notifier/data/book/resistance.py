from ...models.base import MaterialGroupBase
from ...models.models import Drop, Item, Source, Weekday


class Resistance(MaterialGroupBase):
    @property
    def drop(self) -> Drop:
        return Drop(
            item=Item("Resistance Books", "https://genshin-impact.fandom.com/wiki/Resistance_Book"),
            source=Source("Forsaken Rift", "https://genshin-impact.fandom.com/wiki/Forsaken_Rift")
        )

    @property
    def available_on(self) -> list[Weekday]:
        return [Weekday.TUE, Weekday.FRI, Weekday.SUN]
