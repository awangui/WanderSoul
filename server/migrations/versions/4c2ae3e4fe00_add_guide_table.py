"""add guide table

Revision ID: 4c2ae3e4fe00
Revises: 7b2dc83e75b4
Create Date: 2025-01-29 17:07:09.610399

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c2ae3e4fe00'
down_revision = '7b2dc83e75b4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('guides',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('bio', sa.String(length=500), nullable=False),
    sa.Column('languages', sa.String(length=200), nullable=False),
    sa.Column('contact_info', sa.String(length=200), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('guides')
    # ### end Alembic commands ###
