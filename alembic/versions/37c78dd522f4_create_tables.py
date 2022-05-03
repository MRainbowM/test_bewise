"""Create tables

Revision ID: 37c78dd522f4
Revises: 
Create Date: 2022-05-02 19:09:51.018146

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '37c78dd522f4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'category',
        sa.Column('id', sa.BigInteger(), nullable=False),
        sa.Column('title', sa.String(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('clues_count', sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint('id', name=op.f('pk__category'))
    )
    op.create_table(
        'question',
        sa.Column('id', sa.BigInteger(), nullable=False),
        sa.Column('answer', sa.String(), nullable=True),
        sa.Column('question', sa.String(), nullable=True),
        sa.Column('value', sa.Integer(), nullable=True),
        sa.Column('airdate', sa.DateTime(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('updated_at', sa.DateTime(), nullable=True),
        sa.Column('category_id', sa.BigInteger(), nullable=True),
        sa.Column('game_id', sa.Integer(), nullable=True),
        sa.Column('invalid_count', sa.Integer(), nullable=True),
        sa.Column('saved_at', sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(['category_id'], ['category.id'],
                                name=op.f('fk__question__category_id__category')),
        sa.PrimaryKeyConstraint('id', name=op.f('pk__question'))
    )


def downgrade():
    op.drop_table('question')
    op.drop_table('category')
