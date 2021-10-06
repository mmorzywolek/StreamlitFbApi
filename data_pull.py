from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount


class Logowanie:

    def __init__(self, app_id, app_secret, access_token, ad_account,
                 level, date_preset, breakdowns):
        self.app_id = str(app_id)
        self.app_secret = str(app_secret)
        self.access_token = str(access_token)
        self.ad_account = str(ad_account)
        self.level = str(level)
        self.date_preset = str(date_preset)
        self.breakdowns = str(breakdowns)

    def login(self):
        FacebookAdsApi.init(self.app_id, self.app_secret, self.access_token)

        params = {'level': self.level,
                  'date_preset': self.date_preset,
                  'export_format': 'csv',
                  'breakdowns': [self.breakdowns]}

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


