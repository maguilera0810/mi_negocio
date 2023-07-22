from api.v1.management.repositories.client_repository import ClientRepository


class ClientService:

    def __init__(self) -> None:
        self.repo = ClientRepository

    def get_one(self, id: int = None, filters: dict = None):
        if id:
            return self.repo.get_one(id=id)
        return self.repo.get_all(filters).first()

    def get_all(self, filters: dict = None):
        return self.repo.get_all(filters)
