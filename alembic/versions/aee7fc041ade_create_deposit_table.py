"""create_deposit_table

Revision ID: aee7fc041ade
Revises: 
Create Date: 2026-02-25 13:16:30.224662

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'aee7fc041ade'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table("deposits", sa.Column("id", sa.Integer(), primary_key=True, nullable=False), 
                     sa.Column("purpose", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table("deposits")
    pass
