"""create user and blog tables

Revision ID: 0d7df13e3c01
Revises: 8a2e27f3229f
Create Date: 2023-09-05 17:18:18.224015

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0d7df13e3c01'
down_revision: Union[str, None] = '8a2e27f3229f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
