import scrapy
from scrapy.loader import ItemLoader

from ..items import MatchItem


class MatchesSpider(scrapy.Spider):
    name = "matches"
    allowed_domains = ["espncricinfo.com"]
    start_urls = ["https://stats.espncricinfo.com/ci/engine/records/team/match_results.html?id=14452;type=tournament"]

    def parse(self, response):
        matches = response.css("table.engineTable > tbody > tr.data1")
        
        for match in matches:
            field = ItemLoader(item=MatchItem(), selector=match)
            
            field.add_css("team_1", "td:nth-child(1) > a")
            field.add_css("team_2", "td:nth-child(2) > a")
            field.add_css("winner", "td:nth-child(3) > a")
            field.add_css("margin", "td:nth-child(4)")
            field.add_css("ground", "td:nth-child(5) > a")
            field.add_css("date", "td:nth-child(6)")
            
            yield field.load_item()
