"""is active added

Revision ID: b7bc828679f8
Revises: 
Create Date: 2024-01-14 17:08:55.210808

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'b7bc828679f8'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('is_active', sa.Integer(), nullable=True))
    op.alter_column('users', 'email',
               existing_type=mysql.VARCHAR(length=500),
               type_=sa.String(length=50),
               existing_nullable=False)
    op.create_unique_constraint(None, 'users', ['email'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'users', type_='unique')
    op.alter_column('users', 'email',
               existing_type=sa.String(length=50),
               type_=mysql.VARCHAR(length=500),
               existing_nullable=False)
    op.drop_column('users', 'is_active')
    # ### end Alembic commands ###