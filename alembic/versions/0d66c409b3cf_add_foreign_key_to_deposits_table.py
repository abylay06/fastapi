"""add foreign key to deposits table

Revision ID: 0d66c409b3cf
Revises: 3a7b18854ead
Create Date: 2026-02-25 16:12:52.500401

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0d66c409b3cf'
down_revision: Union[str, Sequence[str], None] = '3a7b18854ead'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column("deposits", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key("deposits_users_fk", source_table="deposits", referent_table="users",
                          local_cols=["owner_id"], remote_cols=["id"], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint("deposits_users_fk", table_name="deposits")
    op.drop_column("deposits", "owner_id")
    pass
