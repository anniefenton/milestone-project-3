"""Initial migration

Revision ID: 763980f45cc7
Revises: 
Create Date: 2022-09-03 10:31:57.531226

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '763980f45cc7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_name')
    op.drop_column('user', 'first_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('first_name', sa.VARCHAR(length=30), autoincrement=False, nullable=False))
    op.add_column('user', sa.Column('last_name', sa.VARCHAR(length=30), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
