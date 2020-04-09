from Domain.Service.Queries.GetAllUser.IGetAllUserService import IGetAllUserService
from Service.Queries.GetAllUser.GetAllUserFactory import GetAllUserFactory
import Data.Repositories.UserRepository as UserRepository


class GetAllUserService(IGetAllUserService):

    def Execute(self):
        users = UserRepository.get_all()

        result = GetAllUserFactory.Map_to_Response(users)

        return result
