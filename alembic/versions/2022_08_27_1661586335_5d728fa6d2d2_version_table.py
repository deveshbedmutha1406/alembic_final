"""version table

Revision ID: 5d728fa6d2d2
Revises: 
Create Date: 2022-08-27 13:15:35.106202

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d728fa6d2d2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('versions',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('stamp', sa.DateTime(), nullable=True),
    sa.Column('revisionnum', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
    op.execute("INSERT INTO versions(revisionnum, stamp) VALUES ('5d728fa6d2d2', datetime())")



def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('versions')
    # ### end Alembic commands ###



