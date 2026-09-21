from .data_manager import DataManager as Data


class OperationManager:
    def GetSource(sourcefile: str):
        try:
            return Data.source[sourcefile]
        except:
            return None
