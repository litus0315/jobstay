"""column change3

Revision ID: b811aa492fb9
Revises: 4aafe052f72c
Create Date: 2024-04-07 15:09:52.802774

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b811aa492fb9'
down_revision: Union[str, None] = '4aafe052f72c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
