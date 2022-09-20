from config import Config
from embed import buildWebhook
from leetcode import getRandomProblem


if __name__ == '__main__':
    buildWebhook(getRandomProblem(useDownloaded=True), Config.WEBHOOK_URL).execute()
    buildWebhook(getRandomProblem(useDownloaded=True), Config.WEBHOOK_URL2).execute()
