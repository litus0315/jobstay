"""column change2

Revision ID: 4aafe052f72c
Revises: e995abfdb556
Create Date: 2024-04-07 14:46:10.730346

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4aafe052f72c'
down_revision: Union[str, None] = 'e995abfdb556'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
