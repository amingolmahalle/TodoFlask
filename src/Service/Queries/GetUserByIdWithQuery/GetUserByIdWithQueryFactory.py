from Domain.Service.Queries.GetUserByIdWithQuery.GetUserByIdWithQueryResponse import GetUserByIdWithQueryResponse, \
    AddressDto
from munch import munchify


class GetUserByIdWithQueryFactory:

    @staticmethod
    def Map_to_Response(user):
        addresses = []

        for item in user:
            address = AddressDto(munchify(item))
            addresses.append(address)

        response = GetUserByIdWithQueryResponse(munchify(user[0]), addresses)

        return response
