"""add description and image fields to service table

Revision ID: 659062c95111
Revises: 997f642564e7
Create Date: 2022-07-04 20:30:36.546088

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '659062c95111'
down_revision = '997f642564e7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('service', sa.Column('description', sa.String(length=256), nullable=True))
    op.add_column('service', sa.Column('image', sa.String(length=256), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('service', 'image')
    op.drop_column('service', 'description')
    # ### end Alembic commands ###
