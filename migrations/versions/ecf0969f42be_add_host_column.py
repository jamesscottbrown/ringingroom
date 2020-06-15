"""add host column

Revision ID: ecf0969f42be
Revises: 157fdb8511bf
Create Date: 2020-06-11 08:39:47.620975

"""
from alembic import op
import sqlalchemy as sa
from app import db
from app.models import UserTowerRelation


# revision identifiers, used by Alembic.
revision = 'ecf0969f42be'
down_revision = '157fdb8511bf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_tower_relation', sa.Column('host', sa.Boolean(), nullable=True))
    rels_to_update = UserTowerRelation.query.filter_by(creator=True).all()
    for rel in rels_to_update:
        rel.host = True
    db.session.commit()

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("user_tower_relation") as batch_op:
        batch_op.drop_column('host')
    # ### end Alembic commands ###
