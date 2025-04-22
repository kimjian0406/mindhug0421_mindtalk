from flask import Blueprint, render_template, redirect, url_for, flash, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from app import db
from app.models.user import User

bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
        if existing_user:
            flash("이미 존재하는 사용자입니다.")
            return redirect(url_for("auth.register"))

        new_user = User(
            username=username,
            email=email,
            password=generate_password_hash(password)
        )
        db.session.add(new_user)
        db.session.commit()
        flash("회원가입 완료! 로그인 해주세요.")
        return redirect(url_for("auth.login"))

    return render_template("auth/register.html")


@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            flash("로그인 성공!")
            return redirect(url_for("main.index"))
        flash("이메일 또는 비밀번호가 잘못되었습니다.")
        return redirect(url_for("auth.login"))

    return render_template("auth/login.html")


@bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("로그아웃 되었습니다.")
    return redirect(url_for("auth.login"))

