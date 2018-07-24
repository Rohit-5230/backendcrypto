"""empty message

Revision ID: b34d94b427a0
Revises: 
Create Date: 2018-07-20 10:42:42.359058

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b34d94b427a0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('profiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=20), nullable=True),
    sa.Column('mobile', sa.String(length=10), nullable=True),
    sa.Column('country', sa.String(length=15), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('username', sa.String(length=15), nullable=True),
    sa.Column('password', sa.String(length=80), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('id'),
    sa.UniqueConstraint('mobile'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('profiles')
    # ### end Alembic commands ###