"""Renaming student to scholars

Revision ID: 61ac1e11713d
Revises: 791279dd0760
Create Date: 2025-08-03 19:40:11.506234

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61ac1e11713d'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
    op.rename_table('scholars', 'students')
