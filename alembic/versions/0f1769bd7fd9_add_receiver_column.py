"""add receiver column

Revision ID: 0f1769bd7fd9
Revises: aee7fc041ade
Create Date: 2026-02-25 15:21:23.327557

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0f1769bd7fd9'
down_revision: Union[str, Sequence[str], None] = 'aee7fc041ade'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column("deposits", sa.Column("receiver", sa.String, nullable=False))
    pass


def downgrade():
    op.drop_column("deposits", "receiver")
    pass
