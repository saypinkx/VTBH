"""add office

Revision ID: 7045306cc113
Revises: 0994a4709387
Create Date: 2023-10-13 19:39:29.851688

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7045306cc113'
down_revision: Union[str, None] = '0994a4709387'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('office',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('latitude', sa.String(), nullable=True),
    sa.Column('longitude', sa.String(), nullable=True),
    sa.Column('office_type', sa.String(), nullable=True),
    sa.Column('sale_point_format', sa.String(), nullable=True),
    sa.Column('availability', sa.Boolean(), nullable=True),
    sa.Column('has_ramp', sa.Boolean(), nullable=True),
    sa.Column('metro_station', sa.String(), nullable=True),
    sa.Column('distance', sa.Integer(), nullable=True),
    sa.Column('kep', sa.Boolean(), nullable=True),
    sa.Column('my_branch', sa.Boolean(), nullable=True),
    sa.Column('open_hours', sa.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('office')
    # ### end Alembic commands ###