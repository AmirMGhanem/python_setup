"""priority a7md

Revision ID: 471bcf46ea6c
Revises: 47f18cd16061
Create Date: 2024-01-14 17:52:01.130851

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '471bcf46ea6c'
down_revision: Union[str, None] = '47f18cd16061'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('priority', sa.Integer(), nullable=False,default=0))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todos', 'priority')
    # ### end Alembic commands ###
