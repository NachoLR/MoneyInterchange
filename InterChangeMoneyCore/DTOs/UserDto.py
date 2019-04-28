

class UserDTO(object):
    """
    Class used as a data container. Data transfer object
    """
    id = None
    name = None
    amount_money = None

    # ====================================
    #       *** PUBLIC METHODS ***
    # ====================================

    def SetId(self, id):
        self.id = id

    def GetId(self):
        return self.id

    def SetName(self, name):
        self.name = name

    def GetName(self):
        return self.name

    def SetAmountMoney(self, amount_money):
        self.amount_money = amount_money

    def GetAmountMoney(self):
        return self.amount_money




