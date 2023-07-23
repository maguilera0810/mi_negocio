
from random import choice, randint

from factory import Factory, Iterator, LazyAttribute, SubFactory
from factory.django import DjangoModelFactory
from faker import Faker
from slugify import slugify

from apps.management.models import Address, Client
from mi_negocio.enums import IdentificationType

faker = Faker('es_MX')
SAMPLES = 1000
IDENTIFICATION_TYPES = [IdentificationType.RUC.value,
                        IdentificationType.DNI.value]


class ClientModelFactory(Factory):

    class Meta:
        model = Client

    first_name = Iterator((faker.first_name() for i in range(SAMPLES)))
    last_name = Iterator((faker.last_name() for i in range(SAMPLES)))
    email = LazyAttribute(
        lambda obj: f"{slugify(obj.first_name)}.{slugify(obj.last_name.lower())}@example.com")
    identification_type = Iterator(
        (choice(IDENTIFICATION_TYPES) for i in range(SAMPLES)))
    identification = Iterator(
        (str(randint(1000000000, 9999999999)) for i in range(SAMPLES)))
    cellphone = Iterator((faker.phone_number() for i in range(SAMPLES)))


class AddressModelFactory(DjangoModelFactory):
    class Meta:
        model = Address

    province = Iterator((faker.city() for i in range(SAMPLES)))
    city = Iterator((faker.city() for i in range(SAMPLES)))
    address = Iterator((faker.address() for i in range(SAMPLES)))
    is_matriz = Iterator((bool(randint(0, 1)) for i in range(SAMPLES)))


class AddressFactory():

    def __init__(self, province=None, city=None, address=None, is_matriz=None) -> None:
        self.province = province or faker.city()
        self.city = city or faker.city()
        self.address = address or faker.address()
        self.is_matriz = bool(randint(0, 1)) if is_matriz is None else is_matriz
