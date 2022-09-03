"""Initial migration

Revision ID: 455f2a506f6f
Revises: bc77105d103d
Create Date: 2022-09-03 13:04:38.711381

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '455f2a506f6f'
down_revision = 'bc77105d103d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('recipe', sa.Column('diet_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'recipe', 'diet', ['diet_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'recipe', type_='foreignkey')
    op.drop_column('recipe', 'diet_id')
    # ### end Alembic commands ###
