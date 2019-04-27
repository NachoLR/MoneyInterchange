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

    def CreateNewUser(self,name):
        print(name)


    def GetUserData(self, user_id):
        print (user_id)

    def GetUserBallance(self, user_id):
        print(user_id)

    def AddMoneyToAcount(self, user_id, amount_money, description=None):
        print(user_id)
        print(amount_money)
        print(description)


    def MakeMoneyTransfer(self, user_id_origin, user_id_beneficiary, amount_money, description=None):
        print(user_id_origin)
        print(amount_money)
        print(user_id_beneficiary)
        print(description)

