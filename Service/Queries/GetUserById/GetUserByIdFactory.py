from Domain.Service.Queries.GetUserById.GetUserByIdResponse import GetUserByIdResponse, AddressDto


class GetUserByIdFactory:

    @staticmethod
    def Map_to_Response(user):
        addresses = []

        if user.addresses is not None:
            for address in user.addresses:
                addresses.append(AddressDto(address))

        response = GetUserByIdResponse(user, addresses)
        return response
