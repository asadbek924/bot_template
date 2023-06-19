from .admin import AdminFilter
from .group_filtr import isgroup
from .private_filtr import ISPRIVATE
from config import dp
if __name__=="filters":
    dp.filters_factory.bind(AdminFilter)
    dp.filters_factory.bind(isgroup)
    dp.filters_factory.bind(ISPRIVATE)