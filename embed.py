import discord

from leetcode import ProblemDifficulty, LeetcodeProblemInfo


def difficultyToColor(difficulty: ProblemDifficulty) -> int:
    if difficulty == ProblemDifficulty.Easy:
        return 0x44CF6C
    elif difficulty == ProblemDifficulty.Medium:
        return 0xF0C808
    elif difficulty == ProblemDifficulty.Hard:
        return 0xDD1C1A
    else:
        return 0x9CAFB7


def buildEmbed(problem: LeetcodeProblemInfo) -> discord.Embed:
    embed = discord.Embed(title=f'[{problem["question_id"]}] ' + problem['question__title'],
                          color=difficultyToColor(problem['difficulty']))
    embed.add_field(name='URL', value=problem['url'], inline=False)
    embed.add_field(name='Difficulty', value=problem['difficulty'].name, inline=True)

    acceptanceRate = problem['total_acceptance'] / problem['total_submitted'] * 100
    embed.add_field(name='Acceptance Rate', value=f'{acceptanceRate:.2f}%', inline=True)

    embed.set_footer(text='by mink#8888')
    return embed
