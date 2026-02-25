"""add last few columns to deposits table


Revision ID: af070ea52dfe
Revises: 0d66c409b3cf
Create Date: 2026-02-25 16:24:49.298200

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'af070ea52dfe'
down_revision: Union[str, Sequence[str], None] = '0d66c409b3cf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column("deposits", sa.Column("created_at", sa.TIMESTAMP(timezone=True),
                                server_default=sa.text('now()'), nullable=False))
    op.add_column("deposits", sa.Column("amount", sa.NUMERIC, nullable=False))

    pass


def downgrade():
    op.drop_column("deposits", "amount")
    op.drop_column("deposits", "created_at")
    pass
