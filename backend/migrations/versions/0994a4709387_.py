"""empty message

Revision ID: 0994a4709387
Revises: 70090bfedffa
Create Date: 2023-10-13 19:36:03.358740

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0994a4709387'
down_revision: Union[str, None] = '70090bfedffa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
