import os
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://parser:secret@localhost:5432/jobs_db")