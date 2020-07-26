from pymongo import MongoClient

def updateRackingLabor(wo):
    mongo_client = MongoClient()
    WO_Records = mongo_client.get_database("Tracker").get_collection("WorkOrder")
    execptions = ["900039800", "900039801", "900039795", "Overhead Signage", "Equipment Rentals",
                  "End Cap - Wayfinding", "Emergency Inspection", "900039797", "900039798", "Refusal of Service",
                  "900039813", "900039796", "Install Paint Cages", "900039792"]
    workOrder = WO_Records.find(wo)
    workOrder
