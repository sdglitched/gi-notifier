from ...models.base import MaterialGroupBase
from ...models.models import Drop, Item, Source, Weekday


class Praxis(MaterialGroupBase):
    @property
    def drop(self) -> Drop:
        return Drop(
            item=Item("Praxis Books", "https://genshin-impact.fandom.com/wiki/Praxis_Book"),
            source=Source("Steeple of Ignorance", "https://genshin-impact.fandom.com/wiki/Steeple_of_Ignorance")
        )

    @property
    def available_on(self) -> list[Weekday]:
        return [Weekday.WED, Weekday.SAT, Weekday.SUN]
