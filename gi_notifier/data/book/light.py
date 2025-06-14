from ...models.base import MaterialGroupBase
from ...models.models import Drop, Item, Source, Weekday


class Light(MaterialGroupBase):
    @property
    def drop(self) -> Drop:
        return Drop(
            item=Item("Light Books", "https://genshin-impact.fandom.com/wiki/Light_Book"),
            source=Source("Violet Court", "https://genshin-impact.fandom.com/wiki/Violet_Court")
        )

    @property
    def available_on(self) -> list[Weekday]:
        return [Weekday.WED, Weekday.SAT, Weekday.SUN]
