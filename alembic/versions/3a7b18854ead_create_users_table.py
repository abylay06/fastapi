"""create users table

Revision ID: 3a7b18854ead
Revises: 0f1769bd7fd9
Create Date: 2026-02-25 15:33:31.905170

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3a7b18854ead'
down_revision: Union[str, Sequence[str], None] = '0f1769bd7fd9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table("users", 
                    sa.Column('id', sa.Integer, primary_key=True),
                    sa.Column("email", sa.String, unique=True, nullable=False),
                    sa.Column("password", sa.String, nullable=False),
                    sa.Column("created_at", sa.TIMESTAMP(timezone=True),
                                server_default=sa.text('now()'), nullable=False),
                    )
    pass


def downgrade():
    op.drop_table("users")
    pass
