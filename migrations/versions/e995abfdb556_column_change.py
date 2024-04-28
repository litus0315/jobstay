"""column change

Revision ID: e995abfdb556
Revises: 07f701fed968
Create Date: 2024-04-07 14:45:19.956424

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e995abfdb556'
down_revision: Union[str, None] = '07f701fed968'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
