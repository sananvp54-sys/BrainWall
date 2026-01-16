from flask import Blueprint, render_template
from brainwall.waf.log_reader import read_attack_logs
from brainwall.waf.stats_reader import get_request_stats, get_attack_type_counts

pages = Blueprint("pages", __name__)

@pages.route("/")
def home():
    return render_template("home.html")

@pages.route("/dashboard")
def dashboard():
    logs = read_attack_logs()
    total, blocked, safe = get_request_stats()
    attack_types = get_attack_type_counts()

    return render_template(
        "dashboard.html",
        total_requests=total,
        blocked_attacks=blocked,
        safe_requests=safe,
        logs=logs,
        attack_types=attack_types
    )
