from Domain.Service.Commands.AddUser.IAddUserService import IAddUserService
from Service.Commands.AddUser.AddUserFactory import AddUserFactory
import Data.Repositories.UserRepository as UserRepository
import Service.Commands.AddUser.AddUserValidation as AddUserValidation


class AddUserService(IAddUserService):

    def Execute(self, request):
        AddUserValidation.validation(request)

        new_user = AddUserFactory.Map_to_Entity(request)

        UserRepository.add(new_user)

        UserRepository.commit()

        return new_user
