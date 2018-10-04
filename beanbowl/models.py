from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import json

author = 'Philipp Chapkovski'

doc = """
Proto-app for bean bowl game
"""


class Constants(BaseConstants):
    name_in_url = 'beanbowl'
    players_per_group = None
    num_rounds = 1
    initial_bubbleset = {
        "US": {"name": "United States", "count": 18569},
        "CN": {"name": "China", "count": 11218},
        "JP": {"name": "Japan", "count": 4938},
        "DE": {"name": "Germany", "count": 3466},
        "UK": {
            "name": "United Kingdom",
            "count": 2629,
            "css": {
                ".bubbles_bubble": {"background-color": "DarkSeaGreen", "color": "#006400"},
                ".bubbles_bubble:hover": {"background-color": "#000", "color": "hotpink"}
            }
        },
        "FR": {"name": "France", "count": 2463},
        "IN": {"name": "India", "count": 2256},
        "IT": {"name": "Italy", "count": 1851},
        "BR": {"name": "Brazil", "count": 1799},
        "CA": {"name": "Canada", "count": 1529},
        "KR": {"name": "South Korea", "count": 1411},
        "RS": {"name": "Russia", "count": 1281},
        "AU": {"name": "Australia", "count": 1259},
        "ES": {"name": "Spain", "count": 1233},
        "MX": {"name": "Mexico", "count": 1046},
        "ID": {"name": "Indonesia", "count": 932},
        "TR": {"name": "Turkey", "count": 857},
        "NL": {"name": "Netherlands", "count": 771},
        "CH": {"name": "Switzerland", "count": 660},
        "SA": {"name": "Saudi Arabia", "count": 640}
    }


class Subsession(BaseSubsession):
    def creating_session(self):
        for g in self.get_groups():
            g.bubbleset = json.dumps(Constants.initial_bubbleset)


class Group(BaseGroup):
    bubbleset = models.LongStringField(doc='to store the most recent state of bubbles')

    def get_channel_group_name(self):
        return 'bubble_group_{}'.format(self.pk)


class Player(BasePlayer):
    pass



    # class BubbleSet(djmodels.Model):
    #     group = djmodels.ForeignKey(to=Group, related_name='offers')
    #     bubbleset = models.LongStringField(doc='to store the most recent state of bubbles')
