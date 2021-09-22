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

