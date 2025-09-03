from app.models.center import CentersModel


class CentersRepository:
    def __init__(self, db_client):
        self.db_client = db_client

    def create_centers(self, center: CentersModel):
        self.db_client.add(center)
        self.db_client.commit()
        self.db_client.refresh(center)
        return center

    def get_centers_list(self):
        return self.db_client.query(CentersModel).all()
