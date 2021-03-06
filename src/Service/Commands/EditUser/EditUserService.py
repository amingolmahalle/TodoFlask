from Domain.Service.Commands.EditUser.IEditUserService import IEditUserService
from Service.Commands.EditUser.EditUserFactory import EditUserFactory
import Data.Repositories.UserRepository as UserRepository


class EditUserService(IEditUserService):

    def Execute(self, request):
        current_user = UserRepository.get_by_id(request.id)

        # for address in request.addresses:
        #     userRepository.add_address(address)

        edit_user = EditUserFactory.Map_to_Entity(request, current_user)

        UserRepository.commit()

        return edit_user
