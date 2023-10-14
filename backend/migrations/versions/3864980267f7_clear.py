"""clear

Revision ID: 3864980267f7
Revises: fe299ec4b4d3
Create Date: 2023-10-14 12:50:04.265475

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3864980267f7'
down_revision: Union[str, None] = 'fe299ec4b4d3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Atm',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('latitude', sa.String(), nullable=True),
    sa.Column('longitude', sa.String(), nullable=True),
    sa.Column('is_all_day', sa.Boolean(), nullable=True),
    sa.Column('wheelchair', sa.Boolean(), nullable=True),
    sa.Column('blind', sa.Boolean(), nullable=True),
    sa.Column('nfc_for_bank_cards', sa.Boolean(), nullable=True),
    sa.Column('qr_read', sa.Boolean(), nullable=True),
    sa.Column('supports_usd', sa.Boolean(), nullable=True),
    sa.Column('supports_charge_rub', sa.Boolean(), nullable=True),
    sa.Column('supports_eur', sa.Boolean(), nullable=True),
    sa.Column('supports_rub', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('User',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('registered_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('is_superuser', sa.Boolean(), nullable=True),
    sa.Column('is_entity', sa.Boolean(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
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
    sa.Column('open_hours_individual', sa.JSON(), nullable=True),
    sa.Column('rko', sa.Boolean(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('office')
    op.drop_table('User')
    op.drop_table('Atm')
    # ### end Alembic commands ###