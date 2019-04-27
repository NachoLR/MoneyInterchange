from InterChangeMoneyCore.Enums import OperationTypeEnum


class UserOperationDTO(object):
    data_operation = None
    previous_operation_balance = None
    new_balance = None
    operation_type = None
    operation_description = None

    # ===================================
    #         *** CONSTRUCTOR ***
    # ===================================

    def __init__(self):
        pass

    # ===================================
    #       *** PUBLIC METHODS ***
    # ===================================

    def SetDataOperation(self, data_operation):
        self.data_operation = data_operation

    def GetDataOperation(self):
        return self.data_operation

    def SetPreviousBalance(self, previous_balance):
        self.previous_operation_balance = previous_balance

    def GetPreviousBalance(self):
        return self.previous_operation_balance

    def SetNewBalance(self, new_balance):
        self.new_balance = new_balance

    def GetNewBalance(self):
        return self.new_balance

    def SetOperationType(self, operation_type):
        self.operation_type = operation_type

    def GetOperationType(self):
        return self.operation_type

    def SetOperationDescription(self, description):
        self.operation_description = description

    def GetOperationDescription(self):
        return self.operation_description
