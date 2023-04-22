from scrapy import Item, Field
from itemloaders.processors import MapCompose, TakeFirst
from w3lib.html import remove_tags


class MatchItem(Item):
    team_1 = Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    team_2 = Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    winner = Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    margin = Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    ground = Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
    date = Field(input_processor=MapCompose(remove_tags), output_processor=TakeFirst())
