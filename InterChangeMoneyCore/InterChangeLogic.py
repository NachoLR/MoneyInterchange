import time
from time import sleep

from InterChangeMoneyCore.ManagerDB.DBManager import DBManager
from InterChangeMoneyCore.DTOs.UserDto import UserDTO
from InterChangeMoneyCore.Serializers.JsonSerializer import JsonSerializer

class InterChangeMoneyLogic(object):

    # ====================================
    #         *** CONSTRUCTOR ***
    # ====================================
    def __init__(self):
        self.db_manager = DBManager()

    # =====================================
    #       *** PRIVATE METHODS ***
    # =====================================


    def _parsetouserDTO(self, data_user):
        return  JsonSerializer.DeserializeJson(JsonSerializer.SerializeObject(data_user), UserDTO())



    # ====================================
    #       *** PUBLIC METHODS ***
    # ====================================

    def CreateNewUser(self,name):
        new_user_id = self.db_manager.InsertData(name)
        self.db_manager.UpdateData(new_user_id,0)
        user_data = UserDTO()
        user_data.SetId(new_user_id)
        user_data.SetName(name)
        user_data.SetAmountMoney(0)

        return JsonSerializer.SerializeObject(user_data)


    def GetUserData(self, user_id):
        user_data_dto = self.db_manager.GetData(user_id)

    def GetUserBallance(self, user_id):
        print(user_id)

    def OperateAccount(self, user_id, amount_money):
        user_data = self.db_manager.GetData(user_id)
        user_data = self._parsetouserDTO(user_data)
        old_balance = user_data.GetAmountMoney()
        new_balance = int(old_balance) + int(amount_money)
        if new_balance >= 0:
            user_data.SetAmountMoney(new_balance)
            self.db_manager.UpdateData(user_id, user_data.GetAmountMoney())
            return JsonSerializer.SerializeObject(user_data)
        else:
            return "{\"ERROR\":\"Operation denied insufficient money\"}"



    def MakeMoneyTransfer(self, user_id_origin, user_id_beneficiary, amount_money):
        result_operation = self.OperateAccount(user_id_origin, (int(amount_money) * -1))
        if "Error:" in result_operation:
            return result_operation
        else:
            self.OperateAccount(user_id_beneficiary, amount_money)
            return result_operation







