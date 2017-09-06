"""adding submission date to games

Revision ID: 50763ee8dc6f
Revises: 9a244021c12d
Create Date: 2017-09-06 13:25:07.156305

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50763ee8dc6f'
down_revision = '9a244021c12d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('games', sa.Column('submission_date', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('games', 'submission_date')
    # ### end Alembic commands ###