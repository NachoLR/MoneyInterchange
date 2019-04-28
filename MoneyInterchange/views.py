from rest_framework.views import APIView
from rest_framework.response import Response

from InterChangeMoneyCore.InterChangeLogic import InterChangeMoneyLogic

ApplicationCore = InterChangeMoneyLogic()


class InterChangeMoneyUrls(APIView):

    def post(self, request):
        user_name = request.POST.get('user_name')
        new_user = ApplicationCore.CreateNewUser(user_name)
        return Response(new_user)

    def get(self, request):
        user_id = (request.GET.get('user_id'))
        user = ApplicationCore.GetUserData(user_id)
        return Response(user)


class MoneyOperations(APIView):

    def get(self, request):
        user_id = request.GET.get('user_id')
        user = ApplicationCore.GetUserBallance(user_id)
        return Response(user)

    def put(self, request):
        user_id = request.POST.get('user_id')
        amount_money = request.POST.get('amount_money')
        user_beneficiary_id = request.POST.get('user_beneficiary_id', None)
        if user_beneficiary_id is None:
            return Response(ApplicationCore.OperateAccount(user_id, amount_money))

        else:
            return Response(ApplicationCore.MakeMoneyTransfer(user_id, amount_money, user_beneficiary_id))




def post(self, request):
        user_id = request.POST.get('user_id')
        amount_money = request.POST.get('amount_money')
        description = request.POST.get('description', None)
        user_beneficiary_id = request.POST.get('user_beneficiary_id')
        ApplicationCore.MakeMoneyTransfer(user_id,amount_money,user_beneficiary_id, description)

        return Response('PUT from Django.')