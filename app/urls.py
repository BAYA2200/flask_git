from app import app
from app import views

app.add_url_rule("/", view_func=views.get_transactions, methods=["GET"], endpoint="get_transactions")