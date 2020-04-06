from Domain.Service.Queries.GetUserByIdWithQuery.IGetUserByIdWithQueryService import IGetUserByIdWithQueryService
from Service.Queries.GetUserByIdWithQuery.GetUserByIdWithQueryFactory import GetUserByIdWithQueryFactory
import Data.Repositories.UserRepository as UserRepository


class GetUserByIdWithQueryService(IGetUserByIdWithQueryService):

    def Execute(self, request):
        user = UserRepository.get_by_id_with_query(request.user_id)

        # TODO: Check User Has Value Before Mapping
        result = GetUserByIdWithQueryFactory.Map_to_Response(user)

        # result = None
        # response = userRepository.get_by_id_with_query(userId)
        #
        # if len(response) > 0:
        #     result = UserMapper.create(response)

        return result