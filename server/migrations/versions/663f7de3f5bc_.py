"""empty message

Revision ID: 663f7de3f5bc
Revises: 58edc3cf6dd1
Create Date: 2021-12-23 14:38:08.525251

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '663f7de3f5bc'
down_revision = '58edc3cf6dd1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'characters_read',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('user', 'chapters_read',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('user', 'books_read',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('user', 'shows_watched',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'shows_watched',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('user', 'books_read',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('user', 'chapters_read',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('user', 'characters_read',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###