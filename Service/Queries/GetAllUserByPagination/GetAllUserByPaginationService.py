from Domain.Service.Queries.GetAllUserByPagination.IGetAllUserByPaginationService import IGetAllUserByPaginationService
from Service.Queries.GetAllUserByPagination.GetAllUserByPaginationFactory import GetAllUserByPaginationFactory
from Data.Repositories.UserRepository import get_all_by_pagination


class GetAllUserByPaginationService(IGetAllUserByPaginationService):

    def Execute(self, request):
        users = get_all_by_pagination(request.page, request.per_page)

        result = GetAllUserByPaginationFactory.Map_to_Response(users)

        return result
