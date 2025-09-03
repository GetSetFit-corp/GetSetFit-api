from app.repositories.centers import CentersRepository
from app.models.center import CentersModel


class CentersService:
    def __init__(self, centers_repository: CentersRepository):
        self.centers_repository = centers_repository

    def query(self):
        return self.centers_repository.get_centers_list()

    def insert(self, center: CentersModel):
        return self.centers_repository.create_centers(center)
