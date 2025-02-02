"""Added event_datetime column

Revision ID: b15c8e2a057b
Revises: fc6ca9121bed
Create Date: 2025-02-02 12:39:01.456280

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b15c8e2a057b'
down_revision = 'fc6ca9121bed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('events', schema=None) as batch_op:
        batch_op.add_column(sa.Column('event_datetime', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('events', schema=None) as batch_op:
        batch_op.drop_column('event_datetime')

    # ### end Alembic commands ###
