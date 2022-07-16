from . import models

from flask import request, render_template, redirect, url_for, flash
from . import db

from flask_login import login_user, logout_user, login_required, current_user
from datetime import datetime
from app.models import Transaction

def get_transactions():
    transactions = models.Transaction.query.all()
    render_template("transactions.html", transactions=transactions)