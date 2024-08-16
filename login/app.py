from app import app, db
from app.models import User

# Uncomment the line below to create the database tables
# db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
# pip install werkzeug==2.0.3
