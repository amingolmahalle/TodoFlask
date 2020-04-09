from Domain.Service.Queries.GetUserByMobile.IGetUserByMobileService import IGetUserByMobileService
from Service.Queries.GetUserByMobile.GetUserByMobileFactory import GetUserByMobileFactory
import Data.Repositories.UserRepository as UserRepository


class GetUserByMobileService(IGetUserByMobileService):

    def Execute(self, request):
        user = UserRepository.get_by_mobile(request.mobile)

        # TODO: Check User Has Value Before Mapping
        result = GetUserByMobileFactory.Map_to_Response(user)

        return result
