from InterChangeMoneyCore.Enums import OperationTypeEnum

class InterChangeMoneyLogic(object):

    # ====================================
    #         *** CONSTRUCTOR ***
    # ====================================
    def __init__(self):
        pass

    # =====================================
    #       *** PRIVATE METHODS ***
    # =====================================


    # ====================================
    #       *** PUBLIC METHODS ***
    # ====================================

    def CreateNewUser(self,name, email):
        pass

    def GetUserData(self, user_id):
        pass

    def AddMoneyToAcount(self, user_id, amount_money, description=None):
        pass

    def DecreaseMoney(self,user_id, amount_money, description=None):
        pass

    def MakeMoneyTransfer(self, user_id_origin, user_id_destination, amount_money, description=None):
        pass

