from Class_Types.Labor_Items.article_number import ArticleNumber as AtclNum
from Class_Types.Labor_Items.article_number_state import ArticleNumberState as AtclNumSt
# TODO ONLY NEEDED FOR TESTING PRUPOSES CAN BE DELETED ONCE TESTING IS DONE
from PR_Skate import settings


def getPrices(state):
    prices = dict()
    if state.upper() == "WA":
        for item in AtclNum.objects:
            print(item)
            if item.articleNumber in prices:
                prices[item.articleNumber] = AtclNumSt.objects.find({"state": "WA"})
    print(AtclNum.objects.find_one({"usedByInspectionCompanyButNotPrSkate": False}))



if __name__ == '__main__':
    getPrices("WA")
