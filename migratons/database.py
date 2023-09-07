import sqlalchemy as db
import os
from sqlalchemy.orm import sessionmaker ,scoped_session
from sqlalchemy.pool import StaticPool

if os.environ['stage']=='local':
    engine=db.create_engine('postgresql'://postgres:root@localhost:5432/personalinformationdb,echo=True)
else:
    engine=db.create_engine('postgresql://'+':'.join([os.environ['RDS_USER'],os.environ['RDS_PASS']])+'localhost:5432')
db_session=scoped_session(sessionmaker(engine))
