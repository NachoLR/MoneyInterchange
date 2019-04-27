


class UserDTO(object):

    id = None
    name = None
    amount_money = None
    operations_history = []

    # ====================================
    #         *** CONSTRUCTOR ***
    # ====================================

    def __init__(self):
        pass


    # ====================================
    #       *** PUBLIC METHODS ***
    # ====================================

    def SetId(self, id):
        self.id = id

    def GetID(self):
        return self.id

    def SetUserName(self,name):
        self.name = name

    def GetUserName(self):
        return self.name

    def SetAmountMoney(self, amount_money):
        self.amount_money = amount_money

    def GetAmountMoney(self):
        return self.amount_money

    def SetOperationsHistory(self, operations_list):
        self.operations_history = operations_list

    def AddOperationToHistory(self, operation):
        self.operations_history.append(operation)

    def GetOperationsHistory(self):
        return self.operations_history

