"""adding img url to users

Revision ID: bb5ef27893de
Revises: 07b41a2c6618
Create Date: 2017-09-02 23:02:49.080826

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bb5ef27893de'
down_revision = '07b41a2c6618'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('image_url', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'image_url')
    # ### end Alembic commands ###