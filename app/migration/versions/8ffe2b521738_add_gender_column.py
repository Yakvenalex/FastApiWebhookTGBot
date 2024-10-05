"""add gender column

Revision ID: 8ffe2b521738
Revises: fa0bb3ac1481
Create Date: 2024-10-05 13:42:57.721661

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8ffe2b521738'
down_revision: Union[str, None] = 'fa0bb3ac1481'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('applications', sa.Column('gender', sa.Enum('male', 'female', name='genderenum'), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('applications', 'gender')
    # ### end Alembic commands ###
