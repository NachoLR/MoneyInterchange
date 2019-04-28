import json

from InterChangeMoneyCore.ManagerDB.DBManager import DBManager
from InterChangeMoneyCore.DTOs.UserDto import UserDTO
from InterChangeMoneyCore.Serializers.JsonSerializer import JsonSerializer

class InterChangeMoneyLogic(object):
    """
    Main core for Application, which contains the logic to resolve requests
    """
    # ====================================
    #         *** CONSTRUCTOR ***
    # ====================================
    def __init__(self):
        self.db_manager = DBManager()

    # =====================================
    #       *** PRIVATE METHODS ***
    # =====================================


    def _parsetouserDTO(self, data_user):
        """
        From dict parse to DTO

        :param data_user: dict
        :return: UserDTO
        """
        return  JsonSerializer.DeserializeJson(JsonSerializer.SerializeObject(data_user), UserDTO())



    # ====================================
    #       *** PUBLIC METHODS ***
    # ====================================

    def CreateNewUser(self,name):
        """
        reates new user on DB and return user data serialized in JSON

        :param name: string
        :return:  JSON
        """
        new_user_id = self.db_manager.InsertData(name)
        self.db_manager.UpdateData(new_user_id,0)
        user_data = UserDTO()
        user_data.SetId(new_user_id)
        user_data.SetName(name)
        user_data.SetAmountMoney(0)

        return JsonSerializer.SerializeObject(user_data)


    def GetUserData(self, user_id):
        """
         Searches on database and returns a JSON encoded with the user data

        :param user_id: int
        :return: JSON
        """
        user_data = self.db_manager.GetData(user_id)
        user_data = self._parsetouserDTO(user_data)
        return JsonSerializer.DeserializeJson(user_data)


    def OperateAccount(self, user_id, amount_money):
        """
        Do tPerforms the increment and decrement operations in the user account selected by ID.
        If the operation leaves a balance less than 0 the account, rejects the operation.
        Use the OperateAccount () function which controls that the operations are within the balance above 0.


        :param user_id: int
        :param amount_money: int
        :return: JSON
        """
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
        """
        Starting from two user identifiers, one from the originating user to another destination
        that will receive the transfer, executes a requested money transfer.

        :param user_id_origin:  int
        :param user_id_beneficiary: int
        :param amount_money: int
        :return:  JSON
        """
        result_operation = self.OperateAccount(user_id_origin, (int(amount_money) * -1))
        if "Error:" in result_operation:
            return result_operation
        else:
            self.OperateAccount(user_id_beneficiary, amount_money)
            return result_operation







