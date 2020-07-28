from Class_Types.Labor_Items.article_number import ArticleNumber as AtclNum
from Class_Types.Labor_Items.article_number_state import ArticleNumberState as AtclNumSt
# TODO ONLY NEEDED FOR TESTING PURPOSES CAN BE DELETED ONCE TESTING IS DONE
from PR_Skate import settings


def getPrices(state):
    prices = dict()
    for item in AtclNum.objects.filter(usedByInspectionCompanyButNotPrSkate=False):
        if item.articleNumber not in prices:
            prices[item.articleNumber] = AtclNumSt.objects.get(state=state).price
    return prices
