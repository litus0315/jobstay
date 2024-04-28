"""column change4

Revision ID: afb91fc64e46
Revises: b811aa492fb9
Create Date: 2024-04-07 15:11:07.683171

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'afb91fc64e46'
down_revision: Union[str, None] = 'b811aa492fb9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
