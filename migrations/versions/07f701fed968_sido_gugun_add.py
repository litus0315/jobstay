"""sido gugun add

Revision ID: 07f701fed968
Revises: f18b70e57ff1
Create Date: 2024-04-07 14:29:06.111602

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '07f701fed968'
down_revision: Union[str, None] = 'f18b70e57ff1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
