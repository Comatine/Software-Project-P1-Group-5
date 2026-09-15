from .data_manager import DataManager as Data

class OperationManager:

    def GetSource(sourcefile): #(String)
        match sourcefile:
            case "icon":
                print(Data.source["icon"])
                return Data.source["icon"]
        