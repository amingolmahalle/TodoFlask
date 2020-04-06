from Domain.Service.Queries.GetAllUserByPagination.GetAllUserByPaginationResponse import GetAllUserByPaginationResponse, AddressDto


class GetAllUserByPaginationFactory:

    @staticmethod
    def Map_to_Response(users):
        response = []

        for user in users:
            addresses = []

            if user.addresses is not None:
                for address in user.addresses:
                    addresses.append(AddressDto(address))

            response.append(GetAllUserByPaginationResponse(user, addresses))
        return response
