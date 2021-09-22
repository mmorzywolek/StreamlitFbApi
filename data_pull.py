from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount


class Logowanie:

    def __init__(self, app_id, app_secret, access_token, ad_account):
        self.app_id = str(app_id)
        self.app_secret = str(app_secret)
        self.access_token = str(access_token)
        self.ad_account = str(ad_account)

    def login(self):
        FacebookAdsApi.init(self.app_id, self.app_secret, self.access_token)

        params = {'level': 'ad',
                  'date_preset': 'last_30d',
                  'sort': 'spend_descending',
                  'export_format': 'csv',
                  'breakdowns': ['region']}

        fields = ["account_id",
                  'ad_id',
                  "buying_type",
                  "campaign_id",
                  "objective",
                  "reach",
                  "campaign_name",
                  "impressions",
                  "cpm",
                  "spend",
                  "clicks"]

        insights = list(AdAccount(self.ad_account).get_insights(params=params, fields=fields))
        return insights

app_id = '532305021344703'
app_secret = '9fbda64b62bfab71fc6826faef634be9'
access_token = 'EAAHkIOu1m78BAH2xIFshMOdw8ScCP2Xfhr95XCOZCK7BsBeVWJ9LLVkGfvqu8wuGd0R1tHCW7kVZCKsdeLXgrM6Fc9HZC8jNKKs5lZBsyZB1AlZBkBoXPBZBWRzSyqYpKlUCLR9VGZBelZBlqQcNnZC0ljwYFq2MxlI3pZCnAnqZARZAu6BqU1ZClvTRCgZBmGNMQNZBJ0PG18e3Dwj0hwZDZD'
AdAccount = 'act_1721373204544762'
