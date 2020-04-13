"""new user fields

Revision ID: 510e040b407e
Revises: f743ab141e32
Create Date: 2020-02-06 15:51:29.767545

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '510e040b407e'
down_revision = 'f743ab141e32'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
