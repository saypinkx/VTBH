"""add office

Revision ID: 0a959c97365a
Revises: 7045306cc113
Create Date: 2023-10-13 21:07:56.317066

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0a959c97365a'
down_revision: Union[str, None] = '7045306cc113'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('office', sa.Column('open_hours_individual', sa.JSON(), nullable=True))
    op.add_column('office', sa.Column('rko', sa.Boolean(), nullable=True))
    op.add_column('office', sa.Column('status', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('office', 'status')
    op.drop_column('office', 'rko')
    op.drop_column('office', 'open_hours_individual')
    # ### end Alembic commands ###
