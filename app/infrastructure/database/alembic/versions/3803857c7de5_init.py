"""init

Revision ID: 3803857c7de5
Revises: 
Create Date: 2023-04-08 21:13:25.703444

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3803857c7de5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('telegram_id', sa.BigInteger(), nullable=False),
    sa.Column('full_name', sa.String(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=True),
    sa.Column('status', sa.Enum('APPROVE', 'REJECT', name='status'), nullable=False),
    sa.Column('role', sa.Enum('SUPERADMIN', 'ADMIN', 'USER', name='role'), nullable=False),
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###