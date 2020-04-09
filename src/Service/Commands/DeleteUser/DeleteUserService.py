from Domain.Service.Commands.DeleteUser.IDeleteUserService import IDeleteUserService
import Data.Repositories.UserRepository as UserRepository


class DeleteUserService(IDeleteUserService):

    def Execute(self, request):
        user = UserRepository.get_by_id(request.user_id)

        UserRepository.delete(user)

        UserRepository.commit()
