"""empty message

Revision ID: 662a05813c74
Revises: 
Create Date: 2024-08-15 15:00:57.748901

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '662a05813c74'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('usuario',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('usuario')
    # ### end Alembic commands ###
