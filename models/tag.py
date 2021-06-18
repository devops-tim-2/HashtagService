from common.database import db
from dataclasses import dataclass, asdict


@dataclass
class Tag(db.Model):
    id: int
    value: str

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    value = db.Column(db.String(100), nullable=False)


    def get_dict(self):
        return asdict(self)


    def __str__(self) -> str:
        return f'Tag: id={self.id}, value={self.value}'
