from api.v1.management.repositories.address_repository import AddressRepository


class AddressService:

    def __init__(self) -> None:
        self.repo = AddressRepository

    def get_one(self, id: int = None, filters: dict = None):
        if id:
            return self.repo.get_one(id=id)
        return self.repo.get_all(filters).first()

    def get_all(self, filters: dict = None):
        return self.repo.get_all(filters)
