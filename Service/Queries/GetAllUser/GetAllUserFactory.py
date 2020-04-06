from Domain.Service.Queries.GetAllUser.GetAllUserResponse import GetAllUserResponse, AddressDto


class GetAllUserFactory:

    @staticmethod
    def Map_to_Response(users):
        response = []

        for user in users:
            addresses = []

            if user.addresses is not None:
                for address in user.addresses:
                    addresses.append(AddressDto(address))

            response.append(GetAllUserResponse(user, addresses))
        return response
