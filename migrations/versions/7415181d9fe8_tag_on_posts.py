"""tag on posts

Revision ID: 7415181d9fe8
Revises: 5e0ac934a718
Create Date: 2020-02-25 20:36:56.844696

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7415181d9fe8'
down_revision = '5e0ac934a718'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('tag', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'tag')
    # ### end Alembic commands ###