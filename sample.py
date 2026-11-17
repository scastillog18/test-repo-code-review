"""Sample service to test the AI PR review pipeline.

This file has intentional problems so each reviewer has something to point at.
"""
import os
import subprocess
import sqlite3

# Security: hardcoded secret (fake value)
API_KEY = "sk-test-1234567890abcdef"


def run_command(user_input):
    # Security: shell injection
    return subprocess.run("echo " + user_input, shell=True, capture_output=True)


def get_user(db_path, username):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    # Security: SQL injection
    cursor.execute("SELECT * FROM users WHERE name = '" + username + "'")
    return cursor.fetchone()


def calculate_total(items):
    # Code quality: unpythonic loop, no type hints, no docstring
    t = 0
    for i in range(len(items)):
        t = t + items[i]["price"] * items[i]["qty"]
    return t


def process(data):
    # Code quality: deep nesting, magic numbers, bare except
    try:
        if data:
            if len(data) > 0:
                if data[0] > 42:
                    print("big")
                    return data[0] * 3.14159
    except:
        pass
    return None


def unused_function():
    x = os.getenv("UNUSED")
    return x