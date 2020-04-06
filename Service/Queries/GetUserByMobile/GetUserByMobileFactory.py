from Domain.Service.Queries.GetUserByMobile.GetUserByMobileResponse import GetUserByMobileResponse, AddressDto


class GetUserByMobileFactory:

    @staticmethod
    def Map_to_Response(user):
        addresses = []

        if user.addresses is not None:
            for address in user.addresses:
                addresses.append(AddressDto(address))

        response = GetUserByMobileResponse(user, addresses)
        return response
