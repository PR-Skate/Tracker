from pymongo import MongoClient
from Class_Types.Labor_Items import article_number
from Class_Types.Labor_Items import article_number_state


def getPrices(state):
    prices = dict()
    if state.upper() == "WA":
        for item in article_number.ArticleNumber.objects:
            print(item)
            if item.articleNumber in prices:
                prices[item.articleNumber] = article_number_state.ArticleNumberState.objects.find({"state": "WA"})
    print(AN.find_one({"usedByInspectionCompanyButNotPrSkate": False}))



if __name__ == '__main__':
    getPrices("WA")
