"""Renaming students to scholars

Revision ID: f1a984f3f42c
Revises: 791279dd0760
Create Date: 2023-06-04 14:20:17.639141

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f1a984f3f42c'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
