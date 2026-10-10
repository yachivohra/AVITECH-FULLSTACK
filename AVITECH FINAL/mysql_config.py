"""AVITECH MySQL configuration.

Supports AVITECH_* variables (local/manual hosting) and Railway's standard
MYSQLHOST/MYSQLPORT/MYSQLUSER/MYSQLPASSWORD/MYSQLDATABASE variables.
Never put database credentials directly in this file.
"""
import os


def _env(primary, railway_name, default=None):
    value = os.getenv(primary)
    if value is None or value == "":
        value = os.getenv(railway_name)
    return default if value is None or value == "" else value


MYSQL_HOST = _env("AVITECH_DB_HOST", "MYSQLHOST", "localhost")
MYSQL_PORT = int(_env("AVITECH_DB_PORT", "MYSQLPORT", "3306"))
MYSQL_USER = _env("AVITECH_DB_USER", "MYSQLUSER", "root")
MYSQL_PASSWORD = _env("AVITECH_DB_PASSWORD", "MYSQLPASSWORD")
MYSQL_DATABASE = _env("AVITECH_DB_NAME", "MYSQLDATABASE", "avitec")
