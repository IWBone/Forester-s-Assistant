import os
import sys
import sqlite3

def get_app_dir():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))


def get_db_path():
    """Возвращает путь к БД (ленивая инициализация)"""
    return os.path.join(get_app_dir(), "Database", "forester.db")


def get_db_dir():
    """Возвращает директорию БД (ленивая инициализация)"""
    return os.path.join(get_app_dir(), "Database")


# Для обратной совместимости
DB_DIR = None
DB_NAME = "forester.db"
DB_PATH = None


def get_db():
    # Возвращает контекстное подключение к единой базе данных SQLite
    db_dir = get_db_dir()
    os.makedirs(db_dir, exist_ok=True)
    return sqlite3.connect(get_db_path(), timeout=10)


def init_db():
    # Создаёт структуру всех 6 таблиц в единой базе при первом запуске
    db_dir = get_db_dir()
    os.makedirs(db_dir, exist_ok=True)
    with get_db() as db:
        cursor = db.cursor()
        cursor.executescript("""
        CREATE TABLE IF NOT EXISTS providers (
            provider VARCHAR,
            provider_email_acceptance VARCHAR,
            provider_email_order VARCHAR
        );

        CREATE TABLE IF NOT EXISTS branches (
            branch VARCHAR,
            code_branch VARCHAR
        );

        CREATE TABLE IF NOT EXISTS car_numbers (
            car_number VARCHAR,
            provider VARCHAR
        );

        CREATE TABLE IF NOT EXISTS outlook_email (
            outlook_email VARCHAR,
            outlook_email_pref VARCHAR
        );

        CREATE TABLE IF NOT EXISTS archive_acceptance (
            provider_acceptance VARCHAR,
            branch_acceptance VARCHAR,
            theme_acceptance VARCHAR,
            body_acceptance TEXT,
            date_acceptance DATE,
            board_value_acceptance VARCHAR,
            timber_value_acceptance VARCHAR
        );

        CREATE TABLE IF NOT EXISTS archive_orders (
            provider_order VARCHAR,
            branch_order VARCHAR,
            theme_order VARCHAR,
            body_order TEXT,
            date_order DATE,
            board_value_order VARCHAR,
            timber_value_order VARCHAR
        );
        """)
        db.commit()


if __name__ == "__main__":
    init_db()
    print(f"База данных успешно инициализирована: {get_db_path()}")