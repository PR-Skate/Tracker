from Class_Types.Work_Order.work_order import WorkOrder as WrkOrdr
from Class_Types.Labor_Items.article_number import ArticleNumber as AtclNum
from Class_Types.ScopeOfWork.scope_of_work import ScopeOfWork as ScpWrkStts
from Class_Types.Functions.getPrices import getPrices

def updateRackingLabor(wo):
    exceptions = ["900039800", "900039801", "900039795", "Overhead Signage", "Equipment Rentals",
                  "End Cap - Wayfinding", "Emergency Inspection", "900039797", "900039798", "Refusal of Service",
                  "900039813", "900039796", "Install Paint Cages", "900039792"]
    workOrder = WrkOrdr.objects.get(workOrderName=wo)
    prices = getPrices(workOrder.fkStoreNumber.address.state)
    items = dict
    proceed = False
    for item in AtclNum.objects.filter(usedByInspectionCompanyButNotPrSkate=False):
        items[item.articleNumber] = 0.0
    biggestGB = 0
    for sow in ScpWrkStts.objects.filter(fkWorkOrderName=workOrder.workOrderName and ScpWrkStts.fkStatusID.status):
        proceed = True
        if biggestGB < sow.GB_Counter:
            biggestGB = sow.GB_Counter
        biggestItem = ""




if __name__ == '__main__':
    updateRackingLabor("myWO")
