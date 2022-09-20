import os

from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    PROBLEM_INTERVAL = 60 * 60 * 24  # 1 day
    DISCORD_TOKEN = os.environ['DISCORD_TOKEN']
    DISCORD_CHANNEL = int(os.environ['DISCORD_CHANNEL'])
    SERVER_ID = int(os.environ['SERVER_ID'])
    LEETCODE_ROLE = int(os.environ['LEETCODE_ROLE'])
    WEBHOOK_URL = os.environ['WEBHOOK_URL']
    WEBHOOK_URL2 = os.environ['WEBHOOK_URL2']
