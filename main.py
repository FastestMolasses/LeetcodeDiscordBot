import embed
import discord
import leetcode

from typing import Union
from config import Config
from discord.ext import tasks
from discord.abc import GuildChannel, PrivateChannel


class LeetBot(discord.Client):
    async def on_ready(self):
        self.guild: discord.Guild = self.get_guild(Config.SERVER_ID)
        self.leetcodeRole = discord.utils.get(self.guild.roles, id=Config.LEETCODE_ROLE)
        self.channel: Union[GuildChannel, PrivateChannel] = self.get_channel(Config.DISCORD_CHANNEL)

        self.getProblem.start()

    @tasks.loop(seconds=Config.PROBLEM_INTERVAL)
    async def getProblem(self):
        problem = leetcode.getRandomProblem()
        await self.channel.send(embed=embed.buildEmbed(problem))
        await self.channel.send(self.leetcodeRole.mention)

    @getProblem.before_loop
    async def before_my_task(self):
        """
            Waits until the bot is ready before starting the task.
        """
        await self.wait_until_ready()


def main():
    client = LeetBot()
    client.run(Config.DISCORD_TOKEN)


if __name__ == '__main__':
    main()
