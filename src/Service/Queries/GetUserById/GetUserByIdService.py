from Domain.Service.Queries.GetUserById.IGetUserByIdService import IGetUserByIdService
from Service.Queries.GetUserById.GetUserByIdFactory import GetUserByIdFactory
import Data.Repositories.UserRepository as UserRepository


class GetUserByIdService(IGetUserByIdService):

    def Execute(self, request):
        user = UserRepository.get_by_id(request.user_id)

        # TODO: Check User Has Value Before Mapping
        result = GetUserByIdFactory.Map_to_Response(user)

        return result
