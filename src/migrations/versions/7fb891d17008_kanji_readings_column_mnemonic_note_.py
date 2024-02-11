"""kanji_readings column mnemonic_note rename to mnemonic_hint

Revision ID: 7fb891d17008
Revises: 9e38c88a50a8
Create Date: 2024-02-11 16:03:37.482810

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7fb891d17008'
down_revision: Union[str, None] = '9e38c88a50a8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('kanji_readings', sa.Column('mnemonic_hint', sa.String(), nullable=True))
    op.drop_column('kanji_readings', 'mnemonic_note')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('kanji_readings', sa.Column('mnemonic_note', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_column('kanji_readings', 'mnemonic_hint')
    # ### end Alembic commands ###
