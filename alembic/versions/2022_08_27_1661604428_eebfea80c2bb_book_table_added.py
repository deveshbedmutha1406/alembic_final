"""book table added

Revision ID: eebfea80c2bb
Revises: b0646eb2f7c9
Create Date: 2022-08-27 18:17:08.228579

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eebfea80c2bb'
down_revision = 'b0646eb2f7c9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('qty', sa.Integer(), nullable=True),
    sa.Column('newcol', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###



def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('book')
    # ### end Alembic commands ###


